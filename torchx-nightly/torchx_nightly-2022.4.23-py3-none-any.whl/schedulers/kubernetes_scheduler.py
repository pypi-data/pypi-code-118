#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

"""

This contains the TorchX Kubernetes scheduler which can be used to run TorchX
components on a Kubernetes cluster.

Prerequisites
==============

TorchX kubernetes scheduler depends on volcano and requires etcd intalled for distributed job execution.

Install volcano 1.4.0 version

.. code:: bash

    kubectl apply -f https://raw.githubusercontent.com/volcano-sh/volcano/v1.4.0/installer/volcano-development.yaml

TorchX uses `torch.distributed.run <https://pytorch.org/docs/stable/elastic/run.html>`_ to run distributed training.
This requires the installation of etcd service on your kubernetes cluster:

.. code:: bash

    kubectl apply -f https://github.com/pytorch/torchx/blob/main/resources/etcd.yaml


Learn more about running distributed trainers :py:mod:`torchx.components.dist`

"""

import json
import logging
import re
import warnings
from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING, Any, Dict, Iterable, Mapping, Optional, Tuple

import torchx
import yaml
from torchx.schedulers.api import (
    AppDryRunInfo,
    DescribeAppResponse,
    Scheduler,
    Stream,
    filter_regex,
    split_lines,
)
from torchx.schedulers.ids import make_unique
from torchx.specs.api import (
    AppDef,
    AppState,
    CfgVal,
    ReplicaState,
    ReplicaStatus,
    RetryPolicy,
    Role,
    RoleStatus,
    macros,
    runopts,
    BindMount,
    VolumeMount,
    DeviceMount,
)
from torchx.workspace.docker_workspace import DockerWorkspace


if TYPE_CHECKING:
    from docker import DockerClient
    from kubernetes.client import ApiClient, CustomObjectsApi
    from kubernetes.client.models import (  # noqa: F401 imported but unused
        V1Pod,
        V1PodSpec,
        V1Container,
        V1EnvVar,
        V1ResourceRequirements,
        V1ContainerPort,
    )
    from kubernetes.client.rest import ApiException

logger: logging.Logger = logging.getLogger(__name__)

# Kubernetes reserves a small amount of resources per host for the system. For
# TorchX we always assume the entire host is being requested so we adjust the
# requested numbers account for the node reserved resources.
#
# https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/
RESERVED_MILLICPU = 100
RESERVED_MEMMB = 1024

RETRY_POLICIES: Mapping[str, Iterable[Mapping[str, str]]] = {
    RetryPolicy.REPLICA: [],
    RetryPolicy.APPLICATION: [
        {"event": "PodEvicted", "action": "RestartJob"},
        {"event": "PodFailed", "action": "RestartJob"},
    ],
}

JOB_STATE: Dict[str, AppState] = {
    # Pending is the phase that job is pending in the queue, waiting for
    # scheduling decision
    "Pending": AppState.PENDING,
    # Aborting is the phase that job is aborted, waiting for releasing pods
    "Aborting": AppState.RUNNING,
    # Aborted is the phase that job is aborted by user or error handling
    "Aborted": AppState.CANCELLED,
    # Running is the phase that minimal available tasks of Job are running
    "Running": AppState.RUNNING,
    # Restarting is the phase that the Job is restarted, waiting for pod
    # releasing and recreating
    "Restarting": AppState.RUNNING,
    # Completed is the phase that all tasks of Job are completed successfully
    "Completed": AppState.SUCCEEDED,
    # Terminating is the phase that the Job is terminated, waiting for releasing
    # pods
    "Terminating": AppState.RUNNING,
    # Teriminated is the phase that the job is finished unexpected, e.g. events
    "Terminated": AppState.FAILED,
    "Failed": ReplicaState.FAILED,
}

TASK_STATE: Dict[str, ReplicaState] = {
    # Pending means the task is pending in the apiserver.
    "Pending": ReplicaState.PENDING,
    # Allocated means the scheduler assigns a host to it.
    "Allocated": ReplicaState.PENDING,
    # Pipelined means the scheduler assigns a host to wait for releasing
    # resource.
    "Pipelined": ReplicaState.PENDING,
    # Binding means the scheduler send Bind request to apiserver.
    "Binding": ReplicaState.PENDING,
    # Bound means the task/Pod bounds to a host.
    "Bound": ReplicaState.PENDING,
    # Running means a task is running on the host.
    "Running": ReplicaState.RUNNING,
    # Releasing means a task/pod is deleted.
    "Releasing": ReplicaState.RUNNING,
    # Succeeded means that all containers in the pod have voluntarily
    # terminated with a container exit code of 0, and the system is not
    # going to restart any of these containers.
    "Succeeded": ReplicaState.SUCCEEDED,
    # Failed means that all containers in the pod have terminated, and at
    # least one container has terminated in a failure (exited with a
    # non-zero exit code or was stopped by the system).
    "Failed": ReplicaState.FAILED,
    # Unknown means the status of task/pod is unknown to the scheduler.
    "Unknown": ReplicaState.UNKNOWN,
}

LABEL_VERSION = "torchx.pytorch.org/version"
LABEL_APP_NAME = "torchx.pytorch.org/app-name"
LABEL_ROLE_INDEX = "torchx.pytorch.org/role-index"
LABEL_ROLE_NAME = "torchx.pytorch.org/role-name"
LABEL_REPLICA_ID = "torchx.pytorch.org/replica-id"

ANNOTATION_ISTIO_SIDECAR = "sidecar.istio.io/inject"

LABEL_INSTANCE_TYPE = "node.kubernetes.io/instance-type"


def sanitize_for_serialization(obj: object) -> object:
    from kubernetes import client

    api = client.ApiClient()
    return api.sanitize_for_serialization(obj)


def role_to_pod(name: str, role: Role, service_account: Optional[str]) -> "V1Pod":
    from kubernetes.client.models import (  # noqa: F811 redefinition of unused
        V1Pod,
        V1PodSpec,
        V1Container,
        V1EnvVar,
        V1ResourceRequirements,
        V1ContainerPort,
        V1ObjectMeta,
        V1VolumeMount,
        V1Volume,
        V1HostPathVolumeSource,
        V1PersistentVolumeClaimVolumeSource,
        V1EmptyDirVolumeSource,
        V1SecurityContext,
    )

    # limits puts an upper cap on the resources a pod may consume.
    # requests is how much the scheduler allocates. We assume that the jobs will
    # be allocation the whole machine so requests is slightly lower than the
    # requested resources to account for the Kubernetes node reserved resources.
    limits = {}
    requests = {}

    resource = role.resource
    if resource.cpu > 0:
        mcpu = int(resource.cpu * 1000)
        limits["cpu"] = f"{mcpu}m"
        request_mcpu = max(mcpu - RESERVED_MILLICPU, 0)
        requests["cpu"] = f"{request_mcpu}m"
    if resource.memMB > 0:
        limits["memory"] = f"{int(resource.memMB)}M"
        request_memMB = max(int(resource.memMB) - RESERVED_MEMMB, 0)
        requests["memory"] = f"{request_memMB}M"
    if resource.gpu > 0:
        requests["nvidia.com/gpu"] = limits["nvidia.com/gpu"] = str(resource.gpu)

    for device_name, device_limit in resource.devices.items():
        limits[device_name] = str(device_limit)

    resources = V1ResourceRequirements(
        limits=limits,
        requests=requests,
    )

    node_selector: Dict[str, str] = {}
    if LABEL_INSTANCE_TYPE in resource.capabilities:
        node_selector[LABEL_INSTANCE_TYPE] = resource.capabilities[LABEL_INSTANCE_TYPE]

    # To support PyTorch dataloaders we need to set /dev/shm to larger than the
    # 64M default so we mount an unlimited sized tmpfs directory on it.
    SHM_VOL = "dshm"
    volumes = [
        V1Volume(
            name=SHM_VOL,
            empty_dir=V1EmptyDirVolumeSource(
                medium="Memory",
            ),
        ),
    ]
    volume_mounts = [
        V1VolumeMount(name=SHM_VOL, mount_path="/dev/shm"),
    ]
    security_context = V1SecurityContext()

    for i, mount in enumerate(role.mounts):
        mount_name = f"mount-{i}"
        if isinstance(mount, BindMount):
            volumes.append(
                V1Volume(
                    name=mount_name,
                    host_path=V1HostPathVolumeSource(
                        path=mount.src_path,
                    ),
                )
            )
            volume_mounts.append(
                V1VolumeMount(
                    name=mount_name,
                    mount_path=mount.dst_path,
                    read_only=mount.read_only,
                )
            )
        elif isinstance(mount, VolumeMount):
            volumes.append(
                V1Volume(
                    name=mount_name,
                    persistent_volume_claim=V1PersistentVolumeClaimVolumeSource(
                        claim_name=mount.src,
                    ),
                )
            )
            volume_mounts.append(
                V1VolumeMount(
                    name=mount_name,
                    mount_path=mount.dst_path,
                    read_only=mount.read_only,
                )
            )
        elif isinstance(mount, DeviceMount):
            volumes.append(
                V1Volume(
                    name=mount_name,
                    host_path=V1HostPathVolumeSource(
                        path=mount.src_path,
                    ),
                )
            )
            volume_mounts.append(
                V1VolumeMount(
                    name=mount_name,
                    mount_path=mount.dst_path,
                    read_only=(
                        "w" not in mount.permissions and "m" not in mount.permissions
                    ),
                )
            )
            security_context.privileged = True
        else:
            raise TypeError(f"unknown mount type {mount}")

    container = V1Container(
        command=[role.entrypoint] + role.args,
        image=role.image,
        name=name,
        env=[
            V1EnvVar(
                name=name,
                value=value,
            )
            for name, value in role.env.items()
        ],
        resources=resources,
        ports=[
            V1ContainerPort(
                name=name,
                container_port=port,
            )
            for name, port in role.port_map.items()
        ],
        volume_mounts=volume_mounts,
        security_context=security_context,
    )

    return V1Pod(
        spec=V1PodSpec(
            containers=[container],
            restart_policy="Never",
            service_account_name=service_account,
            volumes=volumes,
            node_selector=node_selector,
        ),
        metadata=V1ObjectMeta(
            annotations={
                # Disable the istio sidecar as it prevents the containers from
                # exiting once finished.
                ANNOTATION_ISTIO_SIDECAR: "false",
            },
            labels={},
        ),
    )


def cleanup_str(data: str) -> str:
    """
    Invokes ``lower`` on thes string and removes all
    characters that do not satisfy ``[a-z0-9]`` pattern.
    This method is mostly used to make sure kubernetes scheduler gets
    the job name that does not violate its validation.
    """
    if data.startswith("-"):
        data = data[1:]
    pattern = r"[a-z0-9\-]"
    return "".join(re.findall(pattern, data.lower()))


def app_to_resource(
    app: AppDef, queue: str, service_account: Optional[str]
) -> Dict[str, object]:
    """
    app_to_resource creates a volcano job kubernetes resource definition from
    the provided AppDef. The resource definition can be used to launch the
    app on Kubernetes.

    To support macros we generate one task per replica instead of using the
    volcano `replicas` field since macros change the arguments on a per
    replica basis.

    Volcano has two levels of retries: one at the task level and one at the
    job level. When using the APPLICATION retry policy, the job level retry
    count is set to the minimum of the max_retries of the roles.
    """
    tasks = []
    unique_app_id = cleanup_str(make_unique(app.name))
    for role_idx, role in enumerate(app.roles):
        for replica_id in range(role.num_replicas):
            values = macros.Values(
                img_root="",
                app_id=unique_app_id,
                replica_id=str(replica_id),
                rank0_env=f"VC_{cleanup_str(app.roles[0].name)}_0_HOSTS".upper(),
            )
            if role_idx == 0 and replica_id == 0:
                values.rank0_env = "TORCHX_RANK0_HOST"
            name = cleanup_str(f"{role.name}-{replica_id}")
            replica_role = values.apply(role)
            if role_idx == 0 and replica_id == 0:
                replica_role.env["TORCHX_RANK0_HOST"] = "localhost"

            pod = role_to_pod(name, replica_role, service_account)
            pod.metadata.labels.update(pod_labels(app, role_idx, role, replica_id))
            task: Dict[str, Any] = {
                "replicas": 1,
                "name": name,
                "template": pod,
            }
            if role.max_retries > 0:
                task["maxRetry"] = role.max_retries
                task["policies"] = RETRY_POLICIES[role.retry_policy]
                msg = f"""
Role {role.name} configured with restarts: {role.max_retries}. As of 1.4.0 Volcano
does NOT support retries correctly. More info: https://github.com/volcano-sh/volcano/issues/1651
                """
                warnings.warn(msg)
            tasks.append(task)

    job_retries = min(role.max_retries for role in app.roles)
    resource: Dict[str, object] = {
        "apiVersion": "batch.volcano.sh/v1alpha1",
        "kind": "Job",
        "metadata": {"name": f"{unique_app_id}"},
        "spec": {
            "schedulerName": "volcano",
            "queue": queue,
            "tasks": tasks,
            "maxRetry": job_retries,
            "plugins": {
                # https://github.com/volcano-sh/volcano/issues/533
                "svc": ["--publish-not-ready-addresses"],
                "env": [],
            },
        },
    }
    return resource


@dataclass
class KubernetesJob:
    images_to_push: Dict[str, Tuple[str, str]]
    resource: Dict[str, object]

    def __str__(self) -> str:
        return yaml.dump(sanitize_for_serialization(self.resource))

    def __repr__(self) -> str:
        return str(self)


class KubernetesScheduler(Scheduler, DockerWorkspace):
    """
    KubernetesScheduler is a TorchX scheduling interface to Kubernetes.

    Important: Volcano is required to be installed on the Kubernetes cluster.
    TorchX requires gang scheduling for multi-replica/multi-role execution
    and Volcano is currently the only supported scheduler with Kubernetes.
    For installation instructions see: https://github.com/volcano-sh/volcano

    This has been confirmed to work with Volcano v1.3.0 and Kubernetes versions
    v1.18-1.21. See https://github.com/pytorch/torchx/issues/120 which is
    tracking Volcano support for Kubernetes v1.22.

    .. note::

        AppDefs that have more than 0 retries may not be displayed as pods if they failed.
        This occurs due to known bug in Volcano(as per 1.4.0 release):
        https://github.com/volcano-sh/volcano/issues/1651


    .. code-block:: bash

        $ pip install torchx[kubernetes]
        $ torchx run --scheduler kubernetes --scheduler_args namespace=default,queue=test utils.echo --image alpine:latest --msg hello
        kubernetes://torchx_user/1234
        $ torchx status kubernetes://torchx_user/1234
        ...

    **Config Options**

    .. runopts::
        class: torchx.schedulers.kubernetes_scheduler.KubernetesScheduler

    **Mounts**

    Mounting external filesystems/volumes is via the HostPath and
    PersistentVolumeClaim support.

    * hostPath volumes: ``type=bind,src=<host path>,dst=<container path>[,readonly]``
    * PersistentVolumeClaim: ``type=volume,src=<claim>,dst=<container path>[,readonly]``
    * host devices: ``type=device,src=/dev/foo[,dst=<container path>][,perm=rwm]``
      If you specify a host device the job will run in privileged mode since
      Kubernetes doesn't expose a way to pass `--device` to the underlying
      container runtime. Users should prefer to use device plugins.

    See :py:func:`torchx.specs.parse_mounts` for more info.

    External docs: https://kubernetes.io/docs/concepts/storage/persistent-volumes/

    **Resources / Allocation**

    To select a specific machine type you can add a capability to your resources
    with ``node.kubernetes.io/instance-type`` which will constrain the launched
    jobs to nodes of that instance type.

    >>> from torchx import specs
    >>> specs.Resource(
    ...     cpu=4,
    ...     memMB=16000,
    ...     gpu=2,
    ...     capabilities={
    ...         "node.kubernetes.io/instance-type": "<cloud instance type>",
    ...     },
    ... )
    Resource(...)

    Kubernetes may reserve some memory for the host. TorchX assumes you're
    scheduling on whole hosts and thus will automatically reduce the resource
    request by a small amount to account for the node reserved CPU and memory.
    If you run into scheduling issues you may need to reduce the requested CPU
    and memory from the host values.

    **Compatibility**

    .. compatibility::
        type: scheduler
        features:
            cancel: true
            logs: true
            distributed: true
            describe: |
                Partial support. KubernetesScheduler will return job and replica
                status but does not provide the complete original AppSpec.
            workspaces: true
            mounts: true
    """

    def __init__(
        self,
        session_name: str,
        client: Optional["ApiClient"] = None,
        docker_client: Optional["DockerClient"] = None,
    ) -> None:
        Scheduler.__init__(self, "kubernetes", session_name)
        DockerWorkspace.__init__(self, docker_client)

        self._client = client

    def _api_client(self) -> "ApiClient":
        from kubernetes import client, config

        c = self._client
        if c is None:
            configuration = client.Configuration()
            try:
                config.load_kube_config(client_configuration=configuration)
            except config.ConfigException as e:
                warnings.warn(f"failed to load kube config: {e}")

            c = self._client = client.ApiClient(configuration)

        return c

    def _custom_objects_api(self) -> "CustomObjectsApi":
        from kubernetes import client

        return client.CustomObjectsApi(self._api_client())

    def _get_job_name_from_exception(self, e: "ApiException") -> Optional[str]:
        try:
            return json.loads(e.body)["details"]["name"]
        except Exception as e:
            logger.exception("Unable to retrieve job name, got exception", e)
            return None

    def schedule(self, dryrun_info: AppDryRunInfo[KubernetesJob]) -> str:
        from kubernetes.client.rest import ApiException

        cfg = dryrun_info._cfg
        assert cfg is not None, f"{dryrun_info} missing cfg"
        namespace = cfg.get("namespace") or "default"

        images_to_push = dryrun_info.request.images_to_push
        self._push_images(images_to_push)

        resource = dryrun_info.request.resource
        try:
            resp = self._custom_objects_api().create_namespaced_custom_object(
                group="batch.volcano.sh",
                version="v1alpha1",
                namespace=namespace,
                plural="jobs",
                body=resource,
            )
        except ApiException as e:
            if e.status == 409 and e.reason == "Conflict":
                job_name = self._get_job_name_from_exception(e)
                raise ValueError(
                    f"Job `{job_name}` already exists. This seems like a transient exception, try resubmitting job"
                ) from e
            else:
                raise

        return f'{namespace}:{resp["metadata"]["name"]}'

    def _submit_dryrun(
        self, app: AppDef, cfg: Mapping[str, CfgVal]
    ) -> AppDryRunInfo[KubernetesJob]:
        queue = cfg.get("queue")
        if not isinstance(queue, str):
            raise TypeError(f"config value 'queue' must be a string, got {queue}")

        # map any local images to the remote image
        images_to_push = self._update_app_images(app, cfg)

        service_account = cfg.get("service_account")
        assert service_account is None or isinstance(
            service_account, str
        ), "service_account must be a str"

        resource = app_to_resource(app, queue, service_account)
        req = KubernetesJob(
            resource=resource,
            images_to_push=images_to_push,
        )
        info = AppDryRunInfo(req, repr)
        info._app = app
        info._cfg = cfg
        return info

    def _validate(self, app: AppDef, scheduler: str) -> None:
        # Skip validation step
        pass

    def _cancel_existing(self, app_id: str) -> None:
        namespace, name = app_id.split(":")
        self._custom_objects_api().delete_namespaced_custom_object(
            group="batch.volcano.sh",
            version="v1alpha1",
            namespace=namespace,
            plural="jobs",
            name=name,
        )

    def run_opts(self) -> runopts:
        opts = runopts()
        opts.add(
            "namespace",
            type_=str,
            help="Kubernetes namespace to schedule job in",
            default="default",
        )
        opts.add(
            "queue",
            type_=str,
            help="Volcano queue to schedule job in",
            required=True,
        )
        opts.add(
            "image_repo",
            type_=str,
            help="The image repository to use when pushing patched images, must have push access. Ex: example.com/your/container",
        )
        opts.add(
            "service_account",
            type_=str,
            help="The service account name to set on the pod specs",
        )
        return opts

    def describe(self, app_id: str) -> Optional[DescribeAppResponse]:
        namespace, name = app_id.split(":")
        roles = {}
        roles_statuses = {}
        resp = self._custom_objects_api().get_namespaced_custom_object_status(
            group="batch.volcano.sh",
            version="v1alpha1",
            namespace=namespace,
            plural="jobs",
            name=name,
        )
        status = resp.get("status")
        if status:
            state_str = status["state"]["phase"]
            app_state = JOB_STATE[state_str]

            TASK_STATUS_COUNT = "taskStatusCount"

            if TASK_STATUS_COUNT in status:
                for name, status in status[TASK_STATUS_COUNT].items():
                    role, _, idx = name.rpartition("-")

                    state_str = next(iter(status["phase"].keys()))
                    state = TASK_STATE[state_str]

                    if role not in roles:
                        roles[role] = Role(name=role, num_replicas=0, image="")
                        roles_statuses[role] = RoleStatus(role, [])
                    roles[role].num_replicas += 1
                    roles_statuses[role].replicas.append(
                        ReplicaStatus(id=int(idx), role=role, state=state, hostname="")
                    )
        else:
            app_state = AppState.UNKNOWN
        return DescribeAppResponse(
            app_id=app_id,
            roles=list(roles.values()),
            roles_statuses=list(roles_statuses.values()),
            state=app_state,
        )

    def log_iter(
        self,
        app_id: str,
        role_name: str,
        k: int = 0,
        regex: Optional[str] = None,
        since: Optional[datetime] = None,
        until: Optional[datetime] = None,
        should_tail: bool = False,
        streams: Optional[Stream] = None,
    ) -> Iterable[str]:
        assert until is None, "kubernetes API doesn't support until"

        if streams not in (None, Stream.COMBINED):
            raise ValueError("KubernetesScheduler only supports COMBINED log stream")

        from kubernetes import client, watch

        namespace, name = app_id.split(":")

        pod_name = cleanup_str(f"{name}-{role_name}-{k}-0")

        args: Dict[str, object] = {
            "name": pod_name,
            "namespace": namespace,
            "timestamps": True,
        }
        if since is not None:
            args["since_seconds"] = (datetime.now() - since).total_seconds()

        core_api = client.CoreV1Api(self._api_client())
        if should_tail:
            w = watch.Watch()
            iterator = w.stream(core_api.read_namespaced_pod_log, **args)
        else:
            resp = core_api.read_namespaced_pod_log(**args)
            iterator = split_lines(resp)

        if regex:
            return filter_regex(regex, iterator)
        else:
            return iterator


def create_scheduler(session_name: str, **kwargs: Any) -> KubernetesScheduler:
    return KubernetesScheduler(
        session_name=session_name,
    )


def pod_labels(
    app: AppDef, role_idx: int, role: Role, replica_id: int
) -> Dict[str, str]:
    return {
        LABEL_VERSION: torchx.__version__,
        LABEL_APP_NAME: app.name,
        LABEL_ROLE_INDEX: str(role_idx),
        LABEL_ROLE_NAME: role.name,
        LABEL_REPLICA_ID: str(replica_id),
    }
