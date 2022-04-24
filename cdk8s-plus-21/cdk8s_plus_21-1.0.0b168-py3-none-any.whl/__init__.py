'''
# cdk8s+ (cdk8s-plus)

### High level constructs for Kubernetes

![Stability:Beta](https://img.shields.io/badge/stability-beta-orange)
[![cdk8s-plus-22](https://img.shields.io/github/workflow/status/cdk8s-team/cdk8s-plus/release-k8s.22?label=cdk8s-plus-22&logo=GitHub)](https://github.com/cdk8s-team/cdk8s-plus/actions/workflows/release-k8s.22.yml)
[![cdk8s-plus-21](https://img.shields.io/github/workflow/status/cdk8s-team/cdk8s-plus/release-k8s.21?label=cdk8s-plus-21&logo=GitHub)](https://github.com/cdk8s-team/cdk8s-plus/actions/workflows/release-k8s.21.yml)
[![cdk8s-plus-20](https://img.shields.io/github/workflow/status/cdk8s-team/cdk8s-plus/release-k8s.20?label=cdk8s-plus-20&logo=GitHub)](https://github.com/cdk8s-team/cdk8s-plus/actions/workflows/release-k8s.20.yml)

| k8s version | npm (JS/TS) | PyPI (Python) | NuGet (C#) | Maven (Java) | Go |
| --- | --- | --- | --- | --- | --- |
| 1.20.0 | [Link](https://www.npmjs.com/package/cdk8s-plus-20) | [Link](https://pypi.org/project/cdk8s-plus-20/) | [Link](https://www.nuget.org/packages/Org.Cdk8s.Plus20) | [Link](https://search.maven.org/artifact/org.cdk8s/cdk8s-plus-20) | [Link](https://github.com/cdk8s-team/cdk8s-plus-go/tree/k8s.20) |
| 1.21.0 | [Link](https://www.npmjs.com/package/cdk8s-plus-21) | [Link](https://pypi.org/project/cdk8s-plus-21/) | [Link](https://www.nuget.org/packages/Org.Cdk8s.Plus21) | [Link](https://search.maven.org/artifact/org.cdk8s/cdk8s-plus-21) | [Link](https://github.com/cdk8s-team/cdk8s-plus-go/tree/k8s.21) |
| 1.22.0 | [Link](https://www.npmjs.com/package/cdk8s-plus-22) | [Link](https://pypi.org/project/cdk8s-plus-22/) | [Link](https://www.nuget.org/packages/Org.Cdk8s.Plus22) | [Link](https://search.maven.org/artifact/org.cdk8s/cdk8s-plus-22) | [Link](https://github.com/cdk8s-team/cdk8s-plus-go/tree/k8s.22) |

**cdk8s+** is a software development framework that provides high level
abstractions for authoring Kubernetes applications. Built on top of the auto
generated building blocks provided by [cdk8s](../cdk8s), this library includes a
hand crafted *construct* for each native kubernetes object, exposing richer
API's with reduced complexity.

## :books: Documentation

See [cdk8s.io](https://cdk8s.io/docs/latest/plus).

## :raised_hand: Contributing

If you'd like to add a new feature or fix a bug, please visit
[CONTRIBUTING.md](CONTRIBUTING.md)!

## :balance_scale: License

This project is distributed under the [Apache License, Version 2.0](./LICENSE).

This module is part of the [cdk8s project](https://github.com/cdk8s-team).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import cdk8s
import constructs


@jsii.data_type(
    jsii_type="cdk8s-plus-21.AddDirectoryOptions",
    jsii_struct_bases=[],
    name_mapping={"exclude": "exclude", "key_prefix": "keyPrefix"},
)
class AddDirectoryOptions:
    def __init__(
        self,
        *,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        key_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options for ``configmap.addDirectory()``.

        :param exclude: Glob patterns to exclude when adding files. Default: - include all files
        :param key_prefix: A prefix to add to all keys in the config map. Default: ""
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if exclude is not None:
            self._values["exclude"] = exclude
        if key_prefix is not None:
            self._values["key_prefix"] = key_prefix

    @builtins.property
    def exclude(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Glob patterns to exclude when adding files.

        :default: - include all files
        '''
        result = self._values.get("exclude")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def key_prefix(self) -> typing.Optional[builtins.str]:
        '''A prefix to add to all keys in the config map.

        :default: ""
        '''
        result = self._values.get("key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AddDirectoryOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.AwsElasticBlockStoreVolumeOptions",
    jsii_struct_bases=[],
    name_mapping={
        "fs_type": "fsType",
        "name": "name",
        "partition": "partition",
        "read_only": "readOnly",
    },
)
class AwsElasticBlockStoreVolumeOptions:
    def __init__(
        self,
        *,
        fs_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options of ``Volume.fromAwsElasticBlockStore``.

        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Default: 'ext4'
        :param name: The volume name. Default: - auto-generated
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). Default: - No partition.
        :param read_only: Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". Default: false
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if name is not None:
            self._values["name"] = name
        if partition is not None:
            self._values["partition"] = partition
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type of the volume that you want to mount.

        Tip: Ensure that the filesystem type is supported by the host operating system.

        :default: 'ext4'

        :see: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The volume name.

        :default: - auto-generated
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition(self) -> typing.Optional[jsii.Number]:
        '''The partition in the volume that you want to mount.

        If omitted, the default is to mount by volume name.
        Examples: For volume /dev/sda1, you specify the partition as "1".
        Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).

        :default: - No partition.
        '''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_only(self) -> typing.Optional[builtins.bool]:
        '''Specify "true" to force and set the ReadOnly property in VolumeMounts to "true".

        :default: false

        :see: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsElasticBlockStoreVolumeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk8s-plus-21.AzureDiskPersistentVolumeCachingMode")
class AzureDiskPersistentVolumeCachingMode(enum.Enum):
    '''Azure disk caching modes.'''

    NONE = "NONE"
    '''None.'''
    READ_ONLY = "READ_ONLY"
    '''ReadOnly.'''
    READ_WRITE = "READ_WRITE"
    '''ReadWrite.'''


@jsii.enum(jsii_type="cdk8s-plus-21.AzureDiskPersistentVolumeKind")
class AzureDiskPersistentVolumeKind(enum.Enum):
    '''Azure Disk kinds.'''

    SHARED = "SHARED"
    '''Multiple blob disks per storage account.'''
    DEDICATED = "DEDICATED"
    '''Single blob disk per storage account.'''
    MANAGED = "MANAGED"
    '''Azure managed data disk.'''


@jsii.data_type(
    jsii_type="cdk8s-plus-21.AzureDiskVolumeOptions",
    jsii_struct_bases=[],
    name_mapping={
        "caching_mode": "cachingMode",
        "fs_type": "fsType",
        "kind": "kind",
        "name": "name",
        "read_only": "readOnly",
    },
)
class AzureDiskVolumeOptions:
    def __init__(
        self,
        *,
        caching_mode: typing.Optional[AzureDiskPersistentVolumeCachingMode] = None,
        fs_type: typing.Optional[builtins.str] = None,
        kind: typing.Optional[AzureDiskPersistentVolumeKind] = None,
        name: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options of ``Volume.fromAzureDisk``.

        :param caching_mode: Host Caching mode. Default: - AzureDiskPersistentVolumeCachingMode.NONE.
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Default: 'ext4'
        :param kind: Kind of disk. Default: AzureDiskPersistentVolumeKind.SHARED
        :param name: The volume name. Default: - auto-generated
        :param read_only: Force the ReadOnly setting in VolumeMounts. Default: false
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if caching_mode is not None:
            self._values["caching_mode"] = caching_mode
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if kind is not None:
            self._values["kind"] = kind
        if name is not None:
            self._values["name"] = name
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def caching_mode(self) -> typing.Optional[AzureDiskPersistentVolumeCachingMode]:
        '''Host Caching mode.

        :default: - AzureDiskPersistentVolumeCachingMode.NONE.
        '''
        result = self._values.get("caching_mode")
        return typing.cast(typing.Optional[AzureDiskPersistentVolumeCachingMode], result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system.

        :default: 'ext4'
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[AzureDiskPersistentVolumeKind]:
        '''Kind of disk.

        :default: AzureDiskPersistentVolumeKind.SHARED
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[AzureDiskPersistentVolumeKind], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The volume name.

        :default: - auto-generated
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(self) -> typing.Optional[builtins.bool]:
        '''Force the ReadOnly setting in VolumeMounts.

        :default: false
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AzureDiskVolumeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.ConfigMapVolumeOptions",
    jsii_struct_bases=[],
    name_mapping={
        "default_mode": "defaultMode",
        "items": "items",
        "name": "name",
        "optional": "optional",
    },
)
class ConfigMapVolumeOptions:
    def __init__(
        self,
        *,
        default_mode: typing.Optional[jsii.Number] = None,
        items: typing.Optional[typing.Mapping[builtins.str, "PathMapping"]] = None,
        name: typing.Optional[builtins.str] = None,
        optional: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options for the ConfigMap-based volume.

        :param default_mode: Mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. Default: 644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
        :param items: If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. Default: - no mapping
        :param name: The volume name. Default: - auto-generated
        :param optional: Specify whether the ConfigMap or its keys must be defined. Default: - undocumented
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if default_mode is not None:
            self._values["default_mode"] = default_mode
        if items is not None:
            self._values["items"] = items
        if name is not None:
            self._values["name"] = name
        if optional is not None:
            self._values["optional"] = optional

    @builtins.property
    def default_mode(self) -> typing.Optional[jsii.Number]:
        '''Mode bits to use on created files by default.

        Must be a value between 0 and
        0777. Defaults to 0644. Directories within the path are not affected by
        this setting. This might be in conflict with other options that affect the
        file mode, like fsGroup, and the result can be other mode bits set.

        :default:

        644. Directories within the path are not affected by this
        setting. This might be in conflict with other options that affect the file
        mode, like fsGroup, and the result can be other mode bits set.
        '''
        result = self._values.get("default_mode")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def items(self) -> typing.Optional[typing.Mapping[builtins.str, "PathMapping"]]:
        '''If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value.

        If specified, the listed keys will be projected
        into the specified paths, and unlisted keys will not be present. If a key
        is specified which is not present in the ConfigMap, the volume setup will
        error unless it is marked optional. Paths must be relative and may not
        contain the '..' path or start with '..'.

        :default: - no mapping
        '''
        result = self._values.get("items")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "PathMapping"]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The volume name.

        :default: - auto-generated
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optional(self) -> typing.Optional[builtins.bool]:
        '''Specify whether the ConfigMap or its keys must be defined.

        :default: - undocumented
        '''
        result = self._values.get("optional")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigMapVolumeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Container(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-21.Container"):
    '''A single application container that you want to run within a pod.'''

    def __init__(
        self,
        *,
        image: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, "EnvValue"]] = None,
        image_pull_policy: typing.Optional["ImagePullPolicy"] = None,
        lifecycle: typing.Optional["ContainerLifecycle"] = None,
        liveness: typing.Optional["Probe"] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        readiness: typing.Optional["Probe"] = None,
        resources: typing.Optional["Resources"] = None,
        security_context: typing.Optional["ContainerSecurityContextProps"] = None,
        startup: typing.Optional["Probe"] = None,
        volume_mounts: typing.Optional[typing.Sequence["VolumeMount"]] = None,
        working_dir: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param image: Docker image name.
        :param args: Arguments to the entrypoint. The docker image's CMD is used if ``command`` is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. Default: []
        :param command: Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell Default: - The docker image's ENTRYPOINT.
        :param env: List of environment variables to set in the container. Cannot be updated. Default: - No environment variables.
        :param image_pull_policy: Image pull policy for this container. Default: ImagePullPolicy.ALWAYS
        :param lifecycle: Describes actions that the management system should take in response to container lifecycle events.
        :param liveness: Periodic probe of container liveness. Container will be restarted if the probe fails. Default: - no liveness probe is defined
        :param name: Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. Default: 'main'
        :param port: Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. Default: - No port is exposed.
        :param readiness: Determines when the container is ready to serve traffic. Default: - no readiness probe is defined
        :param resources: Compute resources (CPU and memory requests and limits) required by the container.
        :param security_context: SecurityContext defines the security options the container should be run with. If set, the fields override equivalent fields of the pod's security context. Default: ensureNonRoot: false privileged: false readOnlyRootFilesystem: false
        :param startup: StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully Default: - no startup probe is defined.
        :param volume_mounts: Pod volumes to mount into the container's filesystem. Cannot be updated.
        :param working_dir: Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. Default: - The container runtime's default.
        '''
        props = ContainerProps(
            image=image,
            args=args,
            command=command,
            env=env,
            image_pull_policy=image_pull_policy,
            lifecycle=lifecycle,
            liveness=liveness,
            name=name,
            port=port,
            readiness=readiness,
            resources=resources,
            security_context=security_context,
            startup=startup,
            volume_mounts=volume_mounts,
            working_dir=working_dir,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="addEnv")
    def add_env(self, name: builtins.str, value: "EnvValue") -> None:
        '''Add an environment value to the container.

        The variable value can come
        from various dynamic sources such a secrets of config maps.

        :param name: - The variable name.
        :param value: - The variable value.

        :see: EnvValue.fromXXX
        '''
        return typing.cast(None, jsii.invoke(self, "addEnv", [name, value]))

    @jsii.member(jsii_name="mount")
    def mount(
        self,
        path: builtins.str,
        storage: "IStorage",
        *,
        propagation: typing.Optional["MountPropagation"] = None,
        read_only: typing.Optional[builtins.bool] = None,
        sub_path: typing.Optional[builtins.str] = None,
        sub_path_expr: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Mount a volume to a specific path so that it is accessible by the container.

        Every pod that is configured to use this container will autmoatically have access to the volume.

        :param path: - The desired path in the container.
        :param storage: - The storage to mount.
        :param propagation: Determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. Mount propagation allows for sharing volumes mounted by a Container to other Containers in the same Pod, or even to other Pods on the same node. Default: MountPropagation.NONE
        :param read_only: Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false. Default: false
        :param sub_path: Path within the volume from which the container's volume should be mounted.). Default: "" the volume's root
        :param sub_path_expr: Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to "" (volume's root). ``subPathExpr`` and ``subPath`` are mutually exclusive. Default: "" volume's root.
        '''
        options = MountOptions(
            propagation=propagation,
            read_only=read_only,
            sub_path=sub_path,
            sub_path_expr=sub_path_expr,
        )

        return typing.cast(None, jsii.invoke(self, "mount", [path, storage, options]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="env")
    def env(self) -> typing.Mapping[builtins.str, "EnvValue"]:
        '''The environment variables for this container.

        Returns a copy. To add environment variables use ``addEnv()``.
        '''
        return typing.cast(typing.Mapping[builtins.str, "EnvValue"], jsii.get(self, "env"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="image")
    def image(self) -> builtins.str:
        '''The container image.'''
        return typing.cast(builtins.str, jsii.get(self, "image"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imagePullPolicy")
    def image_pull_policy(self) -> "ImagePullPolicy":
        '''Image pull policy for this container.'''
        return typing.cast("ImagePullPolicy", jsii.get(self, "imagePullPolicy"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mounts")
    def mounts(self) -> typing.List["VolumeMount"]:
        '''Volume mounts configured for this container.'''
        return typing.cast(typing.List["VolumeMount"], jsii.get(self, "mounts"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the container.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityContext")
    def security_context(self) -> "ContainerSecurityContext":
        '''The security context of the container.'''
        return typing.cast("ContainerSecurityContext", jsii.get(self, "securityContext"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="args")
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Arguments to the entrypoint.

        :return: a copy of the arguments array, cannot be modified.
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "args"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="command")
    def command(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Entrypoint array (the command to execute when the container starts).

        :return: a copy of the entrypoint array, cannot be modified
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "command"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="port")
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port this container exposes.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "port"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resources")
    def resources(self) -> typing.Optional["Resources"]:
        '''Compute resources (CPU and memory requests and limits) required by the container.

        :see: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
        '''
        return typing.cast(typing.Optional["Resources"], jsii.get(self, "resources"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="workingDir")
    def working_dir(self) -> typing.Optional[builtins.str]:
        '''The working directory inside the container.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workingDir"))


@jsii.data_type(
    jsii_type="cdk8s-plus-21.ContainerLifecycle",
    jsii_struct_bases=[],
    name_mapping={"post_start": "postStart", "pre_stop": "preStop"},
)
class ContainerLifecycle:
    def __init__(
        self,
        *,
        post_start: typing.Optional["Handler"] = None,
        pre_stop: typing.Optional["Handler"] = None,
    ) -> None:
        '''Container lifecycle properties.

        :param post_start: This hook is executed immediately after a container is created. However, there is no guarantee that the hook will execute before the container ENTRYPOINT. Default: - No post start handler.
        :param pre_stop: This hook is called immediately before a container is terminated due to an API request or management event such as a liveness/startup probe failure, preemption, resource contention and others. A call to the PreStop hook fails if the container is already in a terminated or completed state and the hook must complete before the TERM signal to stop the container can be sent. The Pod's termination grace period countdown begins before the PreStop hook is executed, so regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period. No parameters are passed to the handler. Default: - No pre stop handler.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if post_start is not None:
            self._values["post_start"] = post_start
        if pre_stop is not None:
            self._values["pre_stop"] = pre_stop

    @builtins.property
    def post_start(self) -> typing.Optional["Handler"]:
        '''This hook is executed immediately after a container is created.

        However,
        there is no guarantee that the hook will execute before the container ENTRYPOINT.

        :default: - No post start handler.
        '''
        result = self._values.get("post_start")
        return typing.cast(typing.Optional["Handler"], result)

    @builtins.property
    def pre_stop(self) -> typing.Optional["Handler"]:
        '''This hook is called immediately before a container is terminated due to an API request or management event such as a liveness/startup probe failure, preemption, resource contention and others.

        A call to the PreStop hook fails if the container is already in a terminated or completed state
        and the hook must complete before the TERM signal to stop the container can be sent.
        The Pod's termination grace period countdown begins before the PreStop hook is executed,
        so regardless of the outcome of the handler, the container will eventually terminate
        within the Pod's termination grace period. No parameters are passed to the handler.

        :default: - No pre stop handler.

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination
        '''
        result = self._values.get("pre_stop")
        return typing.cast(typing.Optional["Handler"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerLifecycle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.ContainerProps",
    jsii_struct_bases=[],
    name_mapping={
        "image": "image",
        "args": "args",
        "command": "command",
        "env": "env",
        "image_pull_policy": "imagePullPolicy",
        "lifecycle": "lifecycle",
        "liveness": "liveness",
        "name": "name",
        "port": "port",
        "readiness": "readiness",
        "resources": "resources",
        "security_context": "securityContext",
        "startup": "startup",
        "volume_mounts": "volumeMounts",
        "working_dir": "workingDir",
    },
)
class ContainerProps:
    def __init__(
        self,
        *,
        image: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, "EnvValue"]] = None,
        image_pull_policy: typing.Optional["ImagePullPolicy"] = None,
        lifecycle: typing.Optional[ContainerLifecycle] = None,
        liveness: typing.Optional["Probe"] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        readiness: typing.Optional["Probe"] = None,
        resources: typing.Optional["Resources"] = None,
        security_context: typing.Optional["ContainerSecurityContextProps"] = None,
        startup: typing.Optional["Probe"] = None,
        volume_mounts: typing.Optional[typing.Sequence["VolumeMount"]] = None,
        working_dir: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for creating a container.

        :param image: Docker image name.
        :param args: Arguments to the entrypoint. The docker image's CMD is used if ``command`` is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. Default: []
        :param command: Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell Default: - The docker image's ENTRYPOINT.
        :param env: List of environment variables to set in the container. Cannot be updated. Default: - No environment variables.
        :param image_pull_policy: Image pull policy for this container. Default: ImagePullPolicy.ALWAYS
        :param lifecycle: Describes actions that the management system should take in response to container lifecycle events.
        :param liveness: Periodic probe of container liveness. Container will be restarted if the probe fails. Default: - no liveness probe is defined
        :param name: Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. Default: 'main'
        :param port: Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. Default: - No port is exposed.
        :param readiness: Determines when the container is ready to serve traffic. Default: - no readiness probe is defined
        :param resources: Compute resources (CPU and memory requests and limits) required by the container.
        :param security_context: SecurityContext defines the security options the container should be run with. If set, the fields override equivalent fields of the pod's security context. Default: ensureNonRoot: false privileged: false readOnlyRootFilesystem: false
        :param startup: StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully Default: - no startup probe is defined.
        :param volume_mounts: Pod volumes to mount into the container's filesystem. Cannot be updated.
        :param working_dir: Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. Default: - The container runtime's default.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = ContainerLifecycle(**lifecycle)
        if isinstance(resources, dict):
            resources = Resources(**resources)
        if isinstance(security_context, dict):
            security_context = ContainerSecurityContextProps(**security_context)
        self._values: typing.Dict[str, typing.Any] = {
            "image": image,
        }
        if args is not None:
            self._values["args"] = args
        if command is not None:
            self._values["command"] = command
        if env is not None:
            self._values["env"] = env
        if image_pull_policy is not None:
            self._values["image_pull_policy"] = image_pull_policy
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if liveness is not None:
            self._values["liveness"] = liveness
        if name is not None:
            self._values["name"] = name
        if port is not None:
            self._values["port"] = port
        if readiness is not None:
            self._values["readiness"] = readiness
        if resources is not None:
            self._values["resources"] = resources
        if security_context is not None:
            self._values["security_context"] = security_context
        if startup is not None:
            self._values["startup"] = startup
        if volume_mounts is not None:
            self._values["volume_mounts"] = volume_mounts
        if working_dir is not None:
            self._values["working_dir"] = working_dir

    @builtins.property
    def image(self) -> builtins.str:
        '''Docker image name.'''
        result = self._values.get("image")
        assert result is not None, "Required property 'image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Arguments to the entrypoint. The docker image's CMD is used if ``command`` is not provided.

        Variable references $(VAR_NAME) are expanded using the container's
        environment. If a variable cannot be resolved, the reference in the input
        string will be unchanged. The $(VAR_NAME) syntax can be escaped with a
        double $$, ie: $$(VAR_NAME). Escaped references will never be expanded,
        regardless of whether the variable exists or not.

        Cannot be updated.

        :default: []

        :see: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell
        '''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def command(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Entrypoint array.

        Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment.
        If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME).
        Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated.
        More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell

        :default: - The docker image's ENTRYPOINT.
        '''
        result = self._values.get("command")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def env(self) -> typing.Optional[typing.Mapping[builtins.str, "EnvValue"]]:
        '''List of environment variables to set in the container.

        Cannot be updated.

        :default: - No environment variables.
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "EnvValue"]], result)

    @builtins.property
    def image_pull_policy(self) -> typing.Optional["ImagePullPolicy"]:
        '''Image pull policy for this container.

        :default: ImagePullPolicy.ALWAYS
        '''
        result = self._values.get("image_pull_policy")
        return typing.cast(typing.Optional["ImagePullPolicy"], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[ContainerLifecycle]:
        '''Describes actions that the management system should take in response to container lifecycle events.'''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[ContainerLifecycle], result)

    @builtins.property
    def liveness(self) -> typing.Optional["Probe"]:
        '''Periodic probe of container liveness.

        Container will be restarted if the probe fails.

        :default: - no liveness probe is defined
        '''
        result = self._values.get("liveness")
        return typing.cast(typing.Optional["Probe"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the container specified as a DNS_LABEL.

        Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.

        :default: 'main'
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Number of port to expose on the pod's IP address.

        This must be a valid port number, 0 < x < 65536.

        :default: - No port is exposed.
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def readiness(self) -> typing.Optional["Probe"]:
        '''Determines when the container is ready to serve traffic.

        :default: - no readiness probe is defined
        '''
        result = self._values.get("readiness")
        return typing.cast(typing.Optional["Probe"], result)

    @builtins.property
    def resources(self) -> typing.Optional["Resources"]:
        '''Compute resources (CPU and memory requests and limits) required by the container.

        :see: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["Resources"], result)

    @builtins.property
    def security_context(self) -> typing.Optional["ContainerSecurityContextProps"]:
        '''SecurityContext defines the security options the container should be run with.

        If set, the fields override equivalent fields of the pod's security context.

        :default:

        ensureNonRoot: false
        privileged: false
        readOnlyRootFilesystem: false

        :see: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
        '''
        result = self._values.get("security_context")
        return typing.cast(typing.Optional["ContainerSecurityContextProps"], result)

    @builtins.property
    def startup(self) -> typing.Optional["Probe"]:
        '''StartupProbe indicates that the Pod has successfully initialized.

        If specified, no other probes are executed until this completes successfully

        :default: - no startup probe is defined.
        '''
        result = self._values.get("startup")
        return typing.cast(typing.Optional["Probe"], result)

    @builtins.property
    def volume_mounts(self) -> typing.Optional[typing.List["VolumeMount"]]:
        '''Pod volumes to mount into the container's filesystem.

        Cannot be updated.
        '''
        result = self._values.get("volume_mounts")
        return typing.cast(typing.Optional[typing.List["VolumeMount"]], result)

    @builtins.property
    def working_dir(self) -> typing.Optional[builtins.str]:
        '''Container's working directory.

        If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.

        :default: - The container runtime's default.
        '''
        result = self._values.get("working_dir")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerSecurityContext(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-21.ContainerSecurityContext",
):
    '''Container security attributes and settings.'''

    def __init__(
        self,
        *,
        ensure_non_root: typing.Optional[builtins.bool] = None,
        group: typing.Optional[jsii.Number] = None,
        privileged: typing.Optional[builtins.bool] = None,
        read_only_root_filesystem: typing.Optional[builtins.bool] = None,
        user: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param ensure_non_root: Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. Default: false
        :param group: The GID to run the entrypoint of the container process. Default: - Group configured by container runtime
        :param privileged: Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Default: false
        :param read_only_root_filesystem: Whether this container has a read-only root filesystem. Default: false
        :param user: The UID to run the entrypoint of the container process. Default: - User specified in image metadata
        '''
        props = ContainerSecurityContextProps(
            ensure_non_root=ensure_non_root,
            group=group,
            privileged=privileged,
            read_only_root_filesystem=read_only_root_filesystem,
            user=user,
        )

        jsii.create(self.__class__, self, [props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ensureNonRoot")
    def ensure_non_root(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "ensureNonRoot"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="privileged")
    def privileged(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "privileged"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="readOnlyRootFilesystem")
    def read_only_root_filesystem(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "readOnlyRootFilesystem"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="group")
    def group(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "group"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="user")
    def user(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "user"))


@jsii.data_type(
    jsii_type="cdk8s-plus-21.ContainerSecurityContextProps",
    jsii_struct_bases=[],
    name_mapping={
        "ensure_non_root": "ensureNonRoot",
        "group": "group",
        "privileged": "privileged",
        "read_only_root_filesystem": "readOnlyRootFilesystem",
        "user": "user",
    },
)
class ContainerSecurityContextProps:
    def __init__(
        self,
        *,
        ensure_non_root: typing.Optional[builtins.bool] = None,
        group: typing.Optional[jsii.Number] = None,
        privileged: typing.Optional[builtins.bool] = None,
        read_only_root_filesystem: typing.Optional[builtins.bool] = None,
        user: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for ``ContainerSecurityContext``.

        :param ensure_non_root: Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. Default: false
        :param group: The GID to run the entrypoint of the container process. Default: - Group configured by container runtime
        :param privileged: Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Default: false
        :param read_only_root_filesystem: Whether this container has a read-only root filesystem. Default: false
        :param user: The UID to run the entrypoint of the container process. Default: - User specified in image metadata
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if ensure_non_root is not None:
            self._values["ensure_non_root"] = ensure_non_root
        if group is not None:
            self._values["group"] = group
        if privileged is not None:
            self._values["privileged"] = privileged
        if read_only_root_filesystem is not None:
            self._values["read_only_root_filesystem"] = read_only_root_filesystem
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def ensure_non_root(self) -> typing.Optional[builtins.bool]:
        '''Indicates that the container must run as a non-root user.

        If true, the Kubelet will validate the image at runtime to ensure that it does
        not run as UID 0 (root) and fail to start the container if it does.

        :default: false
        '''
        result = self._values.get("ensure_non_root")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def group(self) -> typing.Optional[jsii.Number]:
        '''The GID to run the entrypoint of the container process.

        :default: - Group configured by container runtime
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def privileged(self) -> typing.Optional[builtins.bool]:
        '''Run container in privileged mode.

        Processes in privileged containers are essentially equivalent to root on the host.

        :default: false
        '''
        result = self._values.get("privileged")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def read_only_root_filesystem(self) -> typing.Optional[builtins.bool]:
        '''Whether this container has a read-only root filesystem.

        :default: false
        '''
        result = self._values.get("read_only_root_filesystem")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def user(self) -> typing.Optional[jsii.Number]:
        '''The UID to run the entrypoint of the container process.

        :default: - User specified in image metadata
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerSecurityContextProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Cpu(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-21.Cpu"):
    '''Represents the amount of CPU.

    The amount can be passed as millis or units.
    '''

    @jsii.member(jsii_name="millis") # type: ignore[misc]
    @builtins.classmethod
    def millis(cls, amount: jsii.Number) -> "Cpu":
        '''
        :param amount: -
        '''
        return typing.cast("Cpu", jsii.sinvoke(cls, "millis", [amount]))

    @jsii.member(jsii_name="units") # type: ignore[misc]
    @builtins.classmethod
    def units(cls, amount: jsii.Number) -> "Cpu":
        '''
        :param amount: -
        '''
        return typing.cast("Cpu", jsii.sinvoke(cls, "units", [amount]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="amount")
    def amount(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "amount"))

    @amount.setter
    def amount(self, value: builtins.str) -> None:
        jsii.set(self, "amount", value)


@jsii.data_type(
    jsii_type="cdk8s-plus-21.CpuResources",
    jsii_struct_bases=[],
    name_mapping={"limit": "limit", "request": "request"},
)
class CpuResources:
    def __init__(self, *, limit: Cpu, request: Cpu) -> None:
        '''CPU request and limit.

        :param limit: 
        :param request: 
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "limit": limit,
            "request": request,
        }

    @builtins.property
    def limit(self) -> Cpu:
        result = self._values.get("limit")
        assert result is not None, "Required property 'limit' is missing"
        return typing.cast(Cpu, result)

    @builtins.property
    def request(self) -> Cpu:
        result = self._values.get("request")
        assert result is not None, "Required property 'request' is missing"
        return typing.cast(Cpu, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CpuResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DeploymentStrategy(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-21.DeploymentStrategy",
):
    '''Deployment strategies.'''

    @jsii.member(jsii_name="recreate") # type: ignore[misc]
    @builtins.classmethod
    def recreate(cls) -> "DeploymentStrategy":
        '''All existing Pods are killed before new ones are created.

        :see: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#recreate-deployment
        '''
        return typing.cast("DeploymentStrategy", jsii.sinvoke(cls, "recreate", []))

    @jsii.member(jsii_name="rollingUpdate") # type: ignore[misc]
    @builtins.classmethod
    def rolling_update(
        cls,
        *,
        max_surge: typing.Optional["PercentOrAbsolute"] = None,
        max_unavailable: typing.Optional["PercentOrAbsolute"] = None,
    ) -> "DeploymentStrategy":
        '''
        :param max_surge: The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding up. This can not be 0 if ``maxUnavailable`` is 0. Example: when this is set to 30%, the new ReplicaSet can be scaled up immediately when the rolling update starts, such that the total number of old and new pods do not exceed 130% of desired pods. Once old pods have been killed, new ReplicaSet can be scaled up further, ensuring that total number of pods running at any time during the update is at most 130% of desired pods. Default: '25%'
        :param max_unavailable: The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0 if ``maxSurge`` is 0. Example: when this is set to 30%, the old ReplicaSet can be scaled down to 70% of desired pods immediately when the rolling update starts. Once new pods are ready, old ReplicaSet can be scaled down further, followed by scaling up the new ReplicaSet, ensuring that the total number of pods available at all times during the update is at least 70% of desired pods. Default: '25%'
        '''
        options = DeploymentStrategyRollingUpdateOptions(
            max_surge=max_surge, max_unavailable=max_unavailable
        )

        return typing.cast("DeploymentStrategy", jsii.sinvoke(cls, "rollingUpdate", [options]))


@jsii.data_type(
    jsii_type="cdk8s-plus-21.DeploymentStrategyRollingUpdateOptions",
    jsii_struct_bases=[],
    name_mapping={"max_surge": "maxSurge", "max_unavailable": "maxUnavailable"},
)
class DeploymentStrategyRollingUpdateOptions:
    def __init__(
        self,
        *,
        max_surge: typing.Optional["PercentOrAbsolute"] = None,
        max_unavailable: typing.Optional["PercentOrAbsolute"] = None,
    ) -> None:
        '''Options for ``DeploymentStrategy.rollingUpdate``.

        :param max_surge: The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding up. This can not be 0 if ``maxUnavailable`` is 0. Example: when this is set to 30%, the new ReplicaSet can be scaled up immediately when the rolling update starts, such that the total number of old and new pods do not exceed 130% of desired pods. Once old pods have been killed, new ReplicaSet can be scaled up further, ensuring that total number of pods running at any time during the update is at most 130% of desired pods. Default: '25%'
        :param max_unavailable: The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0 if ``maxSurge`` is 0. Example: when this is set to 30%, the old ReplicaSet can be scaled down to 70% of desired pods immediately when the rolling update starts. Once new pods are ready, old ReplicaSet can be scaled down further, followed by scaling up the new ReplicaSet, ensuring that the total number of pods available at all times during the update is at least 70% of desired pods. Default: '25%'
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if max_surge is not None:
            self._values["max_surge"] = max_surge
        if max_unavailable is not None:
            self._values["max_unavailable"] = max_unavailable

    @builtins.property
    def max_surge(self) -> typing.Optional["PercentOrAbsolute"]:
        '''The maximum number of pods that can be scheduled above the desired number of pods.

        Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%).
        Absolute number is calculated from percentage by rounding up.
        This can not be 0 if ``maxUnavailable`` is 0.

        Example: when this is set to 30%, the new ReplicaSet can be scaled up immediately when the rolling update
        starts, such that the total number of old and new pods do not exceed 130% of desired pods.
        Once old pods have been killed, new ReplicaSet can be scaled up further, ensuring that
        total number of pods running at any time during the update is at most 130% of desired pods.

        :default: '25%'
        '''
        result = self._values.get("max_surge")
        return typing.cast(typing.Optional["PercentOrAbsolute"], result)

    @builtins.property
    def max_unavailable(self) -> typing.Optional["PercentOrAbsolute"]:
        '''The maximum number of pods that can be unavailable during the update.

        Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%).
        Absolute number is calculated from percentage by rounding down.
        This can not be 0 if ``maxSurge`` is 0.

        Example: when this is set to 30%, the old ReplicaSet can be scaled down to 70% of desired
        pods immediately when the rolling update starts. Once new pods are ready, old ReplicaSet can
        be scaled down further, followed by scaling up the new ReplicaSet, ensuring that the total
        number of pods available at all times during the update is at least 70% of desired pods.

        :default: '25%'
        '''
        result = self._values.get("max_unavailable")
        return typing.cast(typing.Optional["PercentOrAbsolute"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeploymentStrategyRollingUpdateOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk8s-plus-21.EmptyDirMedium")
class EmptyDirMedium(enum.Enum):
    '''The medium on which to store the volume.'''

    DEFAULT = "DEFAULT"
    '''The default volume of the backing node.'''
    MEMORY = "MEMORY"
    '''Mount a tmpfs (RAM-backed filesystem) for you instead.

    While tmpfs is very
    fast, be aware that unlike disks, tmpfs is cleared on node reboot and any
    files you write will count against your Container's memory limit.
    '''


@jsii.data_type(
    jsii_type="cdk8s-plus-21.EmptyDirVolumeOptions",
    jsii_struct_bases=[],
    name_mapping={"medium": "medium", "size_limit": "sizeLimit"},
)
class EmptyDirVolumeOptions:
    def __init__(
        self,
        *,
        medium: typing.Optional[EmptyDirMedium] = None,
        size_limit: typing.Optional[cdk8s.Size] = None,
    ) -> None:
        '''Options for volumes populated with an empty directory.

        :param medium: By default, emptyDir volumes are stored on whatever medium is backing the node - that might be disk or SSD or network storage, depending on your environment. However, you can set the emptyDir.medium field to ``EmptyDirMedium.MEMORY`` to tell Kubernetes to mount a tmpfs (RAM-backed filesystem) for you instead. While tmpfs is very fast, be aware that unlike disks, tmpfs is cleared on node reboot and any files you write will count against your Container's memory limit. Default: EmptyDirMedium.DEFAULT
        :param size_limit: Total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. Default: - limit is undefined
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if medium is not None:
            self._values["medium"] = medium
        if size_limit is not None:
            self._values["size_limit"] = size_limit

    @builtins.property
    def medium(self) -> typing.Optional[EmptyDirMedium]:
        '''By default, emptyDir volumes are stored on whatever medium is backing the node - that might be disk or SSD or network storage, depending on your environment.

        However, you can set the emptyDir.medium field to
        ``EmptyDirMedium.MEMORY`` to tell Kubernetes to mount a tmpfs (RAM-backed
        filesystem) for you instead. While tmpfs is very fast, be aware that unlike
        disks, tmpfs is cleared on node reboot and any files you write will count
        against your Container's memory limit.

        :default: EmptyDirMedium.DEFAULT
        '''
        result = self._values.get("medium")
        return typing.cast(typing.Optional[EmptyDirMedium], result)

    @builtins.property
    def size_limit(self) -> typing.Optional[cdk8s.Size]:
        '''Total amount of local storage required for this EmptyDir volume.

        The size
        limit is also applicable for memory medium. The maximum usage on memory
        medium EmptyDir would be the minimum value between the SizeLimit specified
        here and the sum of memory limits of all containers in a pod.

        :default: - limit is undefined
        '''
        result = self._values.get("size_limit")
        return typing.cast(typing.Optional[cdk8s.Size], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmptyDirVolumeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk8s-plus-21.EnvFieldPaths")
class EnvFieldPaths(enum.Enum):
    POD_NAME = "POD_NAME"
    '''The name of the pod.'''
    POD_NAMESPACE = "POD_NAMESPACE"
    '''The namespace of the pod.'''
    POD_UID = "POD_UID"
    '''The uid of the pod.'''
    POD_LABEL = "POD_LABEL"
    '''The labels of the pod.'''
    POD_ANNOTATION = "POD_ANNOTATION"
    '''The annotations of the pod.'''
    POD_IP = "POD_IP"
    '''The ipAddress of the pod.'''
    SERVICE_ACCOUNT_NAME = "SERVICE_ACCOUNT_NAME"
    '''The service account name of the pod.'''
    NODE_NAME = "NODE_NAME"
    '''The name of the node.'''
    NODE_IP = "NODE_IP"
    '''The ipAddress of the node.'''
    POD_IPS = "POD_IPS"
    '''The ipAddresess of the pod.'''


class EnvValue(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-21.EnvValue"):
    '''Utility class for creating reading env values from various sources.'''

    @jsii.member(jsii_name="fromConfigMap") # type: ignore[misc]
    @builtins.classmethod
    def from_config_map(
        cls,
        config_map: "IConfigMap",
        key: builtins.str,
        *,
        optional: typing.Optional[builtins.bool] = None,
    ) -> "EnvValue":
        '''Create a value by reading a specific key inside a config map.

        :param config_map: - The config map.
        :param key: - The key to extract the value from.
        :param optional: Specify whether the ConfigMap or its key must be defined. Default: false
        '''
        options = EnvValueFromConfigMapOptions(optional=optional)

        return typing.cast("EnvValue", jsii.sinvoke(cls, "fromConfigMap", [config_map, key, options]))

    @jsii.member(jsii_name="fromFieldRef") # type: ignore[misc]
    @builtins.classmethod
    def from_field_ref(
        cls,
        field_path: EnvFieldPaths,
        *,
        api_version: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
    ) -> "EnvValue":
        '''Create a value from a field reference.

        :param field_path: : The field reference.
        :param api_version: Version of the schema the FieldPath is written in terms of.
        :param key: The key to select the pod label or annotation.
        '''
        options = EnvValueFromFieldRefOptions(api_version=api_version, key=key)

        return typing.cast("EnvValue", jsii.sinvoke(cls, "fromFieldRef", [field_path, options]))

    @jsii.member(jsii_name="fromProcess") # type: ignore[misc]
    @builtins.classmethod
    def from_process(
        cls,
        key: builtins.str,
        *,
        required: typing.Optional[builtins.bool] = None,
    ) -> "EnvValue":
        '''Create a value from a key in the current process environment.

        :param key: - The key to read.
        :param required: Specify whether the key must exist in the environment. If this is set to true, and the key does not exist, an error will thrown. Default: false
        '''
        options = EnvValueFromProcessOptions(required=required)

        return typing.cast("EnvValue", jsii.sinvoke(cls, "fromProcess", [key, options]))

    @jsii.member(jsii_name="fromResource") # type: ignore[misc]
    @builtins.classmethod
    def from_resource(
        cls,
        resource: "ResourceFieldPaths",
        *,
        container: typing.Optional[Container] = None,
        divisor: typing.Optional[builtins.str] = None,
    ) -> "EnvValue":
        '''Create a value from a resource.

        :param resource: : Resource to select the value from.
        :param container: The container to select the value from.
        :param divisor: The output format of the exposed resource.
        '''
        options = EnvValueFromResourceOptions(container=container, divisor=divisor)

        return typing.cast("EnvValue", jsii.sinvoke(cls, "fromResource", [resource, options]))

    @jsii.member(jsii_name="fromSecretValue") # type: ignore[misc]
    @builtins.classmethod
    def from_secret_value(
        cls,
        secret_value: "SecretValue",
        *,
        optional: typing.Optional[builtins.bool] = None,
    ) -> "EnvValue":
        '''Defines an environment value from a secret JSON value.

        :param secret_value: The secret value (secrent + key).
        :param optional: Specify whether the Secret or its key must be defined. Default: false
        '''
        options = EnvValueFromSecretOptions(optional=optional)

        return typing.cast("EnvValue", jsii.sinvoke(cls, "fromSecretValue", [secret_value, options]))

    @jsii.member(jsii_name="fromValue") # type: ignore[misc]
    @builtins.classmethod
    def from_value(cls, value: builtins.str) -> "EnvValue":
        '''Create a value from the given argument.

        :param value: - The value.
        '''
        return typing.cast("EnvValue", jsii.sinvoke(cls, "fromValue", [value]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "value"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="valueFrom")
    def value_from(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "valueFrom"))


@jsii.data_type(
    jsii_type="cdk8s-plus-21.EnvValueFromConfigMapOptions",
    jsii_struct_bases=[],
    name_mapping={"optional": "optional"},
)
class EnvValueFromConfigMapOptions:
    def __init__(self, *, optional: typing.Optional[builtins.bool] = None) -> None:
        '''Options to specify an envionment variable value from a ConfigMap key.

        :param optional: Specify whether the ConfigMap or its key must be defined. Default: false
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if optional is not None:
            self._values["optional"] = optional

    @builtins.property
    def optional(self) -> typing.Optional[builtins.bool]:
        '''Specify whether the ConfigMap or its key must be defined.

        :default: false
        '''
        result = self._values.get("optional")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvValueFromConfigMapOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.EnvValueFromFieldRefOptions",
    jsii_struct_bases=[],
    name_mapping={"api_version": "apiVersion", "key": "key"},
)
class EnvValueFromFieldRefOptions:
    def __init__(
        self,
        *,
        api_version: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options to specify an environment variable value from a field reference.

        :param api_version: Version of the schema the FieldPath is written in terms of.
        :param key: The key to select the pod label or annotation.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if api_version is not None:
            self._values["api_version"] = api_version
        if key is not None:
            self._values["key"] = key

    @builtins.property
    def api_version(self) -> typing.Optional[builtins.str]:
        '''Version of the schema the FieldPath is written in terms of.'''
        result = self._values.get("api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The key to select the pod label or annotation.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvValueFromFieldRefOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.EnvValueFromProcessOptions",
    jsii_struct_bases=[],
    name_mapping={"required": "required"},
)
class EnvValueFromProcessOptions:
    def __init__(self, *, required: typing.Optional[builtins.bool] = None) -> None:
        '''Options to specify an environment variable value from the process environment.

        :param required: Specify whether the key must exist in the environment. If this is set to true, and the key does not exist, an error will thrown. Default: false
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if required is not None:
            self._values["required"] = required

    @builtins.property
    def required(self) -> typing.Optional[builtins.bool]:
        '''Specify whether the key must exist in the environment.

        If this is set to true, and the key does not exist, an error will thrown.

        :default: false
        '''
        result = self._values.get("required")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvValueFromProcessOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.EnvValueFromResourceOptions",
    jsii_struct_bases=[],
    name_mapping={"container": "container", "divisor": "divisor"},
)
class EnvValueFromResourceOptions:
    def __init__(
        self,
        *,
        container: typing.Optional[Container] = None,
        divisor: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options to specify an environment variable value from a resource.

        :param container: The container to select the value from.
        :param divisor: The output format of the exposed resource.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if container is not None:
            self._values["container"] = container
        if divisor is not None:
            self._values["divisor"] = divisor

    @builtins.property
    def container(self) -> typing.Optional[Container]:
        '''The container to select the value from.'''
        result = self._values.get("container")
        return typing.cast(typing.Optional[Container], result)

    @builtins.property
    def divisor(self) -> typing.Optional[builtins.str]:
        '''The output format of the exposed resource.'''
        result = self._values.get("divisor")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvValueFromResourceOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.EnvValueFromSecretOptions",
    jsii_struct_bases=[],
    name_mapping={"optional": "optional"},
)
class EnvValueFromSecretOptions:
    def __init__(self, *, optional: typing.Optional[builtins.bool] = None) -> None:
        '''Options to specify an environment variable value from a Secret.

        :param optional: Specify whether the Secret or its key must be defined. Default: false
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if optional is not None:
            self._values["optional"] = optional

    @builtins.property
    def optional(self) -> typing.Optional[builtins.bool]:
        '''Specify whether the Secret or its key must be defined.

        :default: false
        '''
        result = self._values.get("optional")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvValueFromSecretOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.ExposeDeploymentViaServiceOptions",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "port": "port",
        "protocol": "protocol",
        "service_type": "serviceType",
        "target_port": "targetPort",
    },
)
class ExposeDeploymentViaServiceOptions:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional["Protocol"] = None,
        service_type: typing.Optional["ServiceType"] = None,
        target_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Options for exposing a deployment via a service.

        :param name: The name of the service to expose. This will be set on the Service.metadata and must be a DNS_LABEL Default: undefined Uses the system generated name.
        :param port: The port that the service should serve on. Default: - Copied from the container of the deployment. If a port could not be determined, throws an error.
        :param protocol: The IP protocol for this port. Supports "TCP", "UDP", and "SCTP". Default is TCP. Default: Protocol.TCP
        :param service_type: The type of the exposed service. Default: - ClusterIP.
        :param target_port: The port number the service will redirect to. Default: - The port of the first container in the deployment (ie. containers[0].port)
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if port is not None:
            self._values["port"] = port
        if protocol is not None:
            self._values["protocol"] = protocol
        if service_type is not None:
            self._values["service_type"] = service_type
        if target_port is not None:
            self._values["target_port"] = target_port

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the service to expose.

        This will be set on the Service.metadata and must be a DNS_LABEL

        :default: undefined Uses the system generated name.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port that the service should serve on.

        :default: - Copied from the container of the deployment. If a port could not be determined, throws an error.
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def protocol(self) -> typing.Optional["Protocol"]:
        '''The IP protocol for this port.

        Supports "TCP", "UDP", and "SCTP". Default is TCP.

        :default: Protocol.TCP
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional["Protocol"], result)

    @builtins.property
    def service_type(self) -> typing.Optional["ServiceType"]:
        '''The type of the exposed service.

        :default: - ClusterIP.
        '''
        result = self._values.get("service_type")
        return typing.cast(typing.Optional["ServiceType"], result)

    @builtins.property
    def target_port(self) -> typing.Optional[jsii.Number]:
        '''The port number the service will redirect to.

        :default: - The port of the first container in the deployment (ie. containers[0].port)
        '''
        result = self._values.get("target_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExposeDeploymentViaServiceOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.ExposeServiceViaIngressOptions",
    jsii_struct_bases=[],
    name_mapping={"ingress": "ingress"},
)
class ExposeServiceViaIngressOptions:
    def __init__(self, *, ingress: typing.Optional["IngressV1Beta1"] = None) -> None:
        '''Options for exposing a service using an ingress.

        :param ingress: The ingress to add rules to. Default: - An ingress will be automatically created.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if ingress is not None:
            self._values["ingress"] = ingress

    @builtins.property
    def ingress(self) -> typing.Optional["IngressV1Beta1"]:
        '''The ingress to add rules to.

        :default: - An ingress will be automatically created.
        '''
        result = self._values.get("ingress")
        return typing.cast(typing.Optional["IngressV1Beta1"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExposeServiceViaIngressOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk8s-plus-21.FsGroupChangePolicy")
class FsGroupChangePolicy(enum.Enum):
    ON_ROOT_MISMATCH = "ON_ROOT_MISMATCH"
    '''Only change permissions and ownership if permission and ownership of root directory does not match with expected permissions of the volume.

    This could help shorten the time it takes to change ownership and permission of a volume
    '''
    ALWAYS = "ALWAYS"
    '''Always change permission and ownership of the volume when volume is mounted.'''


@jsii.data_type(
    jsii_type="cdk8s-plus-21.GCEPersistentDiskVolumeOptions",
    jsii_struct_bases=[],
    name_mapping={
        "fs_type": "fsType",
        "name": "name",
        "partition": "partition",
        "read_only": "readOnly",
    },
)
class GCEPersistentDiskVolumeOptions:
    def __init__(
        self,
        *,
        fs_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options of ``Volume.fromGcePersistentDisk``.

        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Default: 'ext4'
        :param name: The volume name. Default: - auto-generated
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). Default: - No partition.
        :param read_only: Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". Default: false
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if name is not None:
            self._values["name"] = name
        if partition is not None:
            self._values["partition"] = partition
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type of the volume that you want to mount.

        Tip: Ensure that the filesystem type is supported by the host operating system.

        :default: 'ext4'

        :see: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The volume name.

        :default: - auto-generated
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition(self) -> typing.Optional[jsii.Number]:
        '''The partition in the volume that you want to mount.

        If omitted, the default is to mount by volume name.
        Examples: For volume /dev/sda1, you specify the partition as "1".
        Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).

        :default: - No partition.
        '''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_only(self) -> typing.Optional[builtins.bool]:
        '''Specify "true" to force and set the ReadOnly property in VolumeMounts to "true".

        :default: false

        :see: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GCEPersistentDiskVolumeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Handler(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-21.Handler"):
    '''Defines a specific action that should be taken.'''

    @jsii.member(jsii_name="fromCommand") # type: ignore[misc]
    @builtins.classmethod
    def from_command(cls, command: typing.Sequence[builtins.str]) -> "Handler":
        '''Defines a handler based on a command which is executed within the container.

        :param command: The command to execute.
        '''
        return typing.cast("Handler", jsii.sinvoke(cls, "fromCommand", [command]))

    @jsii.member(jsii_name="fromHttpGet") # type: ignore[misc]
    @builtins.classmethod
    def from_http_get(
        cls,
        path: builtins.str,
        *,
        port: typing.Optional[jsii.Number] = None,
    ) -> "Handler":
        '''Defines a handler based on an HTTP GET request to the IP address of the container.

        :param path: The URL path to hit.
        :param port: The TCP port to use when sending the GET request. Default: - defaults to ``container.port``.
        '''
        options = HandlerFromHttpGetOptions(port=port)

        return typing.cast("Handler", jsii.sinvoke(cls, "fromHttpGet", [path, options]))

    @jsii.member(jsii_name="fromTcpSocket") # type: ignore[misc]
    @builtins.classmethod
    def from_tcp_socket(
        cls,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> "Handler":
        '''Defines a handler based opening a connection to a TCP socket on the container.

        :param host: The host name to connect to on the container. Default: - defaults to the pod IP
        :param port: The TCP port to connect to on the container. Default: - defaults to ``container.port``.
        '''
        options = HandlerFromTcpSocketOptions(host=host, port=port)

        return typing.cast("Handler", jsii.sinvoke(cls, "fromTcpSocket", [options]))


@jsii.data_type(
    jsii_type="cdk8s-plus-21.HandlerFromHttpGetOptions",
    jsii_struct_bases=[],
    name_mapping={"port": "port"},
)
class HandlerFromHttpGetOptions:
    def __init__(self, *, port: typing.Optional[jsii.Number] = None) -> None:
        '''Options for ``Handler.fromHttpGet``.

        :param port: The TCP port to use when sending the GET request. Default: - defaults to ``container.port``.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The TCP port to use when sending the GET request.

        :default: - defaults to ``container.port``.
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HandlerFromHttpGetOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.HandlerFromTcpSocketOptions",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "port": "port"},
)
class HandlerFromTcpSocketOptions:
    def __init__(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Options for ``Handler.fromTcpSocket``.

        :param host: The host name to connect to on the container. Default: - defaults to the pod IP
        :param port: The TCP port to connect to on the container. Default: - defaults to ``container.port``.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if host is not None:
            self._values["host"] = host
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''The host name to connect to on the container.

        :default: - defaults to the pod IP
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The TCP port to connect to on the container.

        :default: - defaults to ``container.port``.
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HandlerFromTcpSocketOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.HostAlias",
    jsii_struct_bases=[],
    name_mapping={"hostnames": "hostnames", "ip": "ip"},
)
class HostAlias:
    def __init__(
        self,
        *,
        hostnames: typing.Sequence[builtins.str],
        ip: builtins.str,
    ) -> None:
        '''HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's /etc/hosts file.

        :param hostnames: Hostnames for the chosen IP address.
        :param ip: IP address of the host file entry.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "hostnames": hostnames,
            "ip": ip,
        }

    @builtins.property
    def hostnames(self) -> typing.List[builtins.str]:
        '''Hostnames for the chosen IP address.'''
        result = self._values.get("hostnames")
        assert result is not None, "Required property 'hostnames' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def ip(self) -> builtins.str:
        '''IP address of the host file entry.'''
        result = self._values.get("ip")
        assert result is not None, "Required property 'ip' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HostAlias(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="cdk8s-plus-21.IPodSpec")
class IPodSpec(typing_extensions.Protocol):
    '''Represents a resource that can be configured with a kuberenets pod spec. (e.g ``Deployment``, ``Job``, ``Pod``, ...).

    Use the ``PodSpec`` class as an implementation helper.
    '''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="containers")
    def containers(self) -> typing.List[Container]:
        '''The containers belonging to the pod.

        Use ``addContainer`` to add containers.
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hostAliases")
    def host_aliases(self) -> typing.List[HostAlias]:
        '''An optional list of hosts and IPs that will be injected into the pod's hosts file if specified.

        This is only valid for non-hostNetwork pods.
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="initContainers")
    def init_containers(self) -> typing.List[Container]:
        '''The init containers belonging to the pod.

        Use ``addInitContainer`` to add init containers.
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="volumes")
    def volumes(self) -> typing.List["Volume"]:
        '''The volumes associated with this pod.

        Use ``addVolume`` to add volumes.
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="restartPolicy")
    def restart_policy(self) -> typing.Optional["RestartPolicy"]:
        '''Restart policy for all containers within the pod.'''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> typing.Optional["IServiceAccount"]:
        '''The service account used to run this pod.'''
        ...

    @jsii.member(jsii_name="addContainer")
    def add_container(
        self,
        *,
        image: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, EnvValue]] = None,
        image_pull_policy: typing.Optional["ImagePullPolicy"] = None,
        lifecycle: typing.Optional[ContainerLifecycle] = None,
        liveness: typing.Optional["Probe"] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        readiness: typing.Optional["Probe"] = None,
        resources: typing.Optional["Resources"] = None,
        security_context: typing.Optional[ContainerSecurityContextProps] = None,
        startup: typing.Optional["Probe"] = None,
        volume_mounts: typing.Optional[typing.Sequence["VolumeMount"]] = None,
        working_dir: typing.Optional[builtins.str] = None,
    ) -> Container:
        '''Add a container to the pod.

        :param image: Docker image name.
        :param args: Arguments to the entrypoint. The docker image's CMD is used if ``command`` is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. Default: []
        :param command: Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell Default: - The docker image's ENTRYPOINT.
        :param env: List of environment variables to set in the container. Cannot be updated. Default: - No environment variables.
        :param image_pull_policy: Image pull policy for this container. Default: ImagePullPolicy.ALWAYS
        :param lifecycle: Describes actions that the management system should take in response to container lifecycle events.
        :param liveness: Periodic probe of container liveness. Container will be restarted if the probe fails. Default: - no liveness probe is defined
        :param name: Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. Default: 'main'
        :param port: Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. Default: - No port is exposed.
        :param readiness: Determines when the container is ready to serve traffic. Default: - no readiness probe is defined
        :param resources: Compute resources (CPU and memory requests and limits) required by the container.
        :param security_context: SecurityContext defines the security options the container should be run with. If set, the fields override equivalent fields of the pod's security context. Default: ensureNonRoot: false privileged: false readOnlyRootFilesystem: false
        :param startup: StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully Default: - no startup probe is defined.
        :param volume_mounts: Pod volumes to mount into the container's filesystem. Cannot be updated.
        :param working_dir: Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. Default: - The container runtime's default.
        '''
        ...

    @jsii.member(jsii_name="addInitContainer")
    def add_init_container(
        self,
        *,
        image: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, EnvValue]] = None,
        image_pull_policy: typing.Optional["ImagePullPolicy"] = None,
        lifecycle: typing.Optional[ContainerLifecycle] = None,
        liveness: typing.Optional["Probe"] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        readiness: typing.Optional["Probe"] = None,
        resources: typing.Optional["Resources"] = None,
        security_context: typing.Optional[ContainerSecurityContextProps] = None,
        startup: typing.Optional["Probe"] = None,
        volume_mounts: typing.Optional[typing.Sequence["VolumeMount"]] = None,
        working_dir: typing.Optional[builtins.str] = None,
    ) -> Container:
        '''Add an init container to the pod.

        :param image: Docker image name.
        :param args: Arguments to the entrypoint. The docker image's CMD is used if ``command`` is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. Default: []
        :param command: Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell Default: - The docker image's ENTRYPOINT.
        :param env: List of environment variables to set in the container. Cannot be updated. Default: - No environment variables.
        :param image_pull_policy: Image pull policy for this container. Default: ImagePullPolicy.ALWAYS
        :param lifecycle: Describes actions that the management system should take in response to container lifecycle events.
        :param liveness: Periodic probe of container liveness. Container will be restarted if the probe fails. Default: - no liveness probe is defined
        :param name: Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. Default: 'main'
        :param port: Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. Default: - No port is exposed.
        :param readiness: Determines when the container is ready to serve traffic. Default: - no readiness probe is defined
        :param resources: Compute resources (CPU and memory requests and limits) required by the container.
        :param security_context: SecurityContext defines the security options the container should be run with. If set, the fields override equivalent fields of the pod's security context. Default: ensureNonRoot: false privileged: false readOnlyRootFilesystem: false
        :param startup: StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully Default: - no startup probe is defined.
        :param volume_mounts: Pod volumes to mount into the container's filesystem. Cannot be updated.
        :param working_dir: Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. Default: - The container runtime's default.
        '''
        ...

    @jsii.member(jsii_name="addVolume")
    def add_volume(self, volume: "Volume") -> None:
        '''Add a volume to the pod.

        :param volume: The volume.
        '''
        ...


class _IPodSpecProxy:
    '''Represents a resource that can be configured with a kuberenets pod spec. (e.g ``Deployment``, ``Job``, ``Pod``, ...).

    Use the ``PodSpec`` class as an implementation helper.
    '''

    __jsii_type__: typing.ClassVar[str] = "cdk8s-plus-21.IPodSpec"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="containers")
    def containers(self) -> typing.List[Container]:
        '''The containers belonging to the pod.

        Use ``addContainer`` to add containers.
        '''
        return typing.cast(typing.List[Container], jsii.get(self, "containers"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hostAliases")
    def host_aliases(self) -> typing.List[HostAlias]:
        '''An optional list of hosts and IPs that will be injected into the pod's hosts file if specified.

        This is only valid for non-hostNetwork pods.
        '''
        return typing.cast(typing.List[HostAlias], jsii.get(self, "hostAliases"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="initContainers")
    def init_containers(self) -> typing.List[Container]:
        '''The init containers belonging to the pod.

        Use ``addInitContainer`` to add init containers.
        '''
        return typing.cast(typing.List[Container], jsii.get(self, "initContainers"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="volumes")
    def volumes(self) -> typing.List["Volume"]:
        '''The volumes associated with this pod.

        Use ``addVolume`` to add volumes.
        '''
        return typing.cast(typing.List["Volume"], jsii.get(self, "volumes"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="restartPolicy")
    def restart_policy(self) -> typing.Optional["RestartPolicy"]:
        '''Restart policy for all containers within the pod.'''
        return typing.cast(typing.Optional["RestartPolicy"], jsii.get(self, "restartPolicy"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> typing.Optional["IServiceAccount"]:
        '''The service account used to run this pod.'''
        return typing.cast(typing.Optional["IServiceAccount"], jsii.get(self, "serviceAccount"))

    @jsii.member(jsii_name="addContainer")
    def add_container(
        self,
        *,
        image: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, EnvValue]] = None,
        image_pull_policy: typing.Optional["ImagePullPolicy"] = None,
        lifecycle: typing.Optional[ContainerLifecycle] = None,
        liveness: typing.Optional["Probe"] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        readiness: typing.Optional["Probe"] = None,
        resources: typing.Optional["Resources"] = None,
        security_context: typing.Optional[ContainerSecurityContextProps] = None,
        startup: typing.Optional["Probe"] = None,
        volume_mounts: typing.Optional[typing.Sequence["VolumeMount"]] = None,
        working_dir: typing.Optional[builtins.str] = None,
    ) -> Container:
        '''Add a container to the pod.

        :param image: Docker image name.
        :param args: Arguments to the entrypoint. The docker image's CMD is used if ``command`` is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. Default: []
        :param command: Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell Default: - The docker image's ENTRYPOINT.
        :param env: List of environment variables to set in the container. Cannot be updated. Default: - No environment variables.
        :param image_pull_policy: Image pull policy for this container. Default: ImagePullPolicy.ALWAYS
        :param lifecycle: Describes actions that the management system should take in response to container lifecycle events.
        :param liveness: Periodic probe of container liveness. Container will be restarted if the probe fails. Default: - no liveness probe is defined
        :param name: Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. Default: 'main'
        :param port: Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. Default: - No port is exposed.
        :param readiness: Determines when the container is ready to serve traffic. Default: - no readiness probe is defined
        :param resources: Compute resources (CPU and memory requests and limits) required by the container.
        :param security_context: SecurityContext defines the security options the container should be run with. If set, the fields override equivalent fields of the pod's security context. Default: ensureNonRoot: false privileged: false readOnlyRootFilesystem: false
        :param startup: StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully Default: - no startup probe is defined.
        :param volume_mounts: Pod volumes to mount into the container's filesystem. Cannot be updated.
        :param working_dir: Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. Default: - The container runtime's default.
        '''
        container = ContainerProps(
            image=image,
            args=args,
            command=command,
            env=env,
            image_pull_policy=image_pull_policy,
            lifecycle=lifecycle,
            liveness=liveness,
            name=name,
            port=port,
            readiness=readiness,
            resources=resources,
            security_context=security_context,
            startup=startup,
            volume_mounts=volume_mounts,
            working_dir=working_dir,
        )

        return typing.cast(Container, jsii.invoke(self, "addContainer", [container]))

    @jsii.member(jsii_name="addInitContainer")
    def add_init_container(
        self,
        *,
        image: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, EnvValue]] = None,
        image_pull_policy: typing.Optional["ImagePullPolicy"] = None,
        lifecycle: typing.Optional[ContainerLifecycle] = None,
        liveness: typing.Optional["Probe"] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        readiness: typing.Optional["Probe"] = None,
        resources: typing.Optional["Resources"] = None,
        security_context: typing.Optional[ContainerSecurityContextProps] = None,
        startup: typing.Optional["Probe"] = None,
        volume_mounts: typing.Optional[typing.Sequence["VolumeMount"]] = None,
        working_dir: typing.Optional[builtins.str] = None,
    ) -> Container:
        '''Add an init container to the pod.

        :param image: Docker image name.
        :param args: Arguments to the entrypoint. The docker image's CMD is used if ``command`` is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. Default: []
        :param command: Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell Default: - The docker image's ENTRYPOINT.
        :param env: List of environment variables to set in the container. Cannot be updated. Default: - No environment variables.
        :param image_pull_policy: Image pull policy for this container. Default: ImagePullPolicy.ALWAYS
        :param lifecycle: Describes actions that the management system should take in response to container lifecycle events.
        :param liveness: Periodic probe of container liveness. Container will be restarted if the probe fails. Default: - no liveness probe is defined
        :param name: Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. Default: 'main'
        :param port: Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. Default: - No port is exposed.
        :param readiness: Determines when the container is ready to serve traffic. Default: - no readiness probe is defined
        :param resources: Compute resources (CPU and memory requests and limits) required by the container.
        :param security_context: SecurityContext defines the security options the container should be run with. If set, the fields override equivalent fields of the pod's security context. Default: ensureNonRoot: false privileged: false readOnlyRootFilesystem: false
        :param startup: StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully Default: - no startup probe is defined.
        :param volume_mounts: Pod volumes to mount into the container's filesystem. Cannot be updated.
        :param working_dir: Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. Default: - The container runtime's default.
        '''
        container = ContainerProps(
            image=image,
            args=args,
            command=command,
            env=env,
            image_pull_policy=image_pull_policy,
            lifecycle=lifecycle,
            liveness=liveness,
            name=name,
            port=port,
            readiness=readiness,
            resources=resources,
            security_context=security_context,
            startup=startup,
            volume_mounts=volume_mounts,
            working_dir=working_dir,
        )

        return typing.cast(Container, jsii.invoke(self, "addInitContainer", [container]))

    @jsii.member(jsii_name="addVolume")
    def add_volume(self, volume: "Volume") -> None:
        '''Add a volume to the pod.

        :param volume: The volume.
        '''
        return typing.cast(None, jsii.invoke(self, "addVolume", [volume]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPodSpec).__jsii_proxy_class__ = lambda : _IPodSpecProxy


@jsii.interface(jsii_type="cdk8s-plus-21.IPodTemplate")
class IPodTemplate(IPodSpec, typing_extensions.Protocol):
    '''Represents a resource that can be configured with a kuberenets pod template. (e.g ``Deployment``, ``Job``, ...).

    Use the ``PodTemplate`` class as an implementation helper.
    '''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="podMetadata")
    def pod_metadata(self) -> cdk8s.ApiObjectMetadataDefinition:
        '''Provides read/write access to the underlying pod metadata of the resource.'''
        ...


class _IPodTemplateProxy(
    jsii.proxy_for(IPodSpec) # type: ignore[misc]
):
    '''Represents a resource that can be configured with a kuberenets pod template. (e.g ``Deployment``, ``Job``, ...).

    Use the ``PodTemplate`` class as an implementation helper.
    '''

    __jsii_type__: typing.ClassVar[str] = "cdk8s-plus-21.IPodTemplate"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="podMetadata")
    def pod_metadata(self) -> cdk8s.ApiObjectMetadataDefinition:
        '''Provides read/write access to the underlying pod metadata of the resource.'''
        return typing.cast(cdk8s.ApiObjectMetadataDefinition, jsii.get(self, "podMetadata"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPodTemplate).__jsii_proxy_class__ = lambda : _IPodTemplateProxy


@jsii.interface(jsii_type="cdk8s-plus-21.IResource")
class IResource(typing_extensions.Protocol):
    '''Represents a resource.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The Kubernetes name of this resource.'''
        ...


class _IResourceProxy:
    '''Represents a resource.'''

    __jsii_type__: typing.ClassVar[str] = "cdk8s-plus-21.IResource"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The Kubernetes name of this resource.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResource).__jsii_proxy_class__ = lambda : _IResourceProxy


@jsii.interface(jsii_type="cdk8s-plus-21.ISecret")
class ISecret(IResource, typing_extensions.Protocol):
    pass


class _ISecretProxy(
    jsii.proxy_for(IResource) # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "cdk8s-plus-21.ISecret"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISecret).__jsii_proxy_class__ = lambda : _ISecretProxy


@jsii.interface(jsii_type="cdk8s-plus-21.IServiceAccount")
class IServiceAccount(IResource, typing_extensions.Protocol):
    pass


class _IServiceAccountProxy(
    jsii.proxy_for(IResource) # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "cdk8s-plus-21.IServiceAccount"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServiceAccount).__jsii_proxy_class__ = lambda : _IServiceAccountProxy


@jsii.interface(jsii_type="cdk8s-plus-21.IStorage")
class IStorage(typing_extensions.Protocol):
    '''Represents a piece of storage in the cluster.'''

    @jsii.member(jsii_name="asVolume")
    def as_volume(self) -> "Volume":
        '''Convert the piece of storage into a concrete volume.'''
        ...


class _IStorageProxy:
    '''Represents a piece of storage in the cluster.'''

    __jsii_type__: typing.ClassVar[str] = "cdk8s-plus-21.IStorage"

    @jsii.member(jsii_name="asVolume")
    def as_volume(self) -> "Volume":
        '''Convert the piece of storage into a concrete volume.'''
        return typing.cast("Volume", jsii.invoke(self, "asVolume", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStorage).__jsii_proxy_class__ = lambda : _IStorageProxy


@jsii.enum(jsii_type="cdk8s-plus-21.ImagePullPolicy")
class ImagePullPolicy(enum.Enum):
    ALWAYS = "ALWAYS"
    '''Every time the kubelet launches a container, the kubelet queries the container image registry to resolve the name to an image digest.

    If the kubelet has a container image with that exact
    digest cached locally, the kubelet uses its cached image; otherwise, the kubelet downloads
    (pulls) the image with the resolved digest, and uses that image to launch the container.

    Default is Always if ImagePullPolicy is omitted and either the image tag is :latest or
    the image tag is omitted.
    '''
    IF_NOT_PRESENT = "IF_NOT_PRESENT"
    '''The image is pulled only if it is not already present locally.

    Default is IfNotPresent if ImagePullPolicy is omitted and the image tag is present but
    not :latest
    '''
    NEVER = "NEVER"
    '''The image is assumed to exist locally.

    No attempt is made to pull the image.
    '''


class IngressV1Beta1Backend(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-21.IngressV1Beta1Backend",
):
    '''The backend for an ingress path.'''

    @jsii.member(jsii_name="fromService") # type: ignore[misc]
    @builtins.classmethod
    def from_service(
        cls,
        service: "Service",
        *,
        port: typing.Optional[jsii.Number] = None,
    ) -> "IngressV1Beta1Backend":
        '''A Kubernetes ``Service`` to use as the backend for this path.

        :param service: The service object.
        :param port: The port to use to access the service. - This option will fail if the service does not expose any ports. - If the service exposes multiple ports, this option must be specified. - If the service exposes a single port, this option is optional and if specified, it must be the same port exposed by the service. Default: - if the service exposes a single port, this port will be used.
        '''
        options = ServiceIngressV1BetaBackendOptions(port=port)

        return typing.cast("IngressV1Beta1Backend", jsii.sinvoke(cls, "fromService", [service, options]))


@jsii.data_type(
    jsii_type="cdk8s-plus-21.IngressV1Beta1Rule",
    jsii_struct_bases=[],
    name_mapping={"backend": "backend", "host": "host", "path": "path"},
)
class IngressV1Beta1Rule:
    def __init__(
        self,
        *,
        backend: IngressV1Beta1Backend,
        host: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Represents the rules mapping the paths under a specified host to the related backend services.

        Incoming requests are first evaluated for a host match,
        then routed to the backend associated with the matching path.

        :param backend: Backend defines the referenced service endpoint to which the traffic will be forwarded to.
        :param host: Host is the fully qualified domain name of a network host, as defined by RFC 3986. Note the following deviations from the "host" part of the URI as defined in the RFC: 1. IPs are not allowed. Currently an IngressRuleValue can only apply to the IP in the Spec of the parent Ingress. 2. The ``:`` delimiter is not respected because ports are not allowed. Currently the port of an Ingress is implicitly :80 for http and :443 for https. Both these may change in the future. Incoming requests are matched against the host before the IngressRuleValue. Default: - If the host is unspecified, the Ingress routes all traffic based on the specified IngressRuleValue.
        :param path: Path is an extended POSIX regex as defined by IEEE Std 1003.1, (i.e this follows the egrep/unix syntax, not the perl syntax) matched against the path of an incoming request. Currently it can contain characters disallowed from the conventional "path" part of a URL as defined by RFC 3986. Paths must begin with a '/'. Default: - If unspecified, the path defaults to a catch all sending traffic to the backend.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "backend": backend,
        }
        if host is not None:
            self._values["host"] = host
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def backend(self) -> IngressV1Beta1Backend:
        '''Backend defines the referenced service endpoint to which the traffic will be forwarded to.'''
        result = self._values.get("backend")
        assert result is not None, "Required property 'backend' is missing"
        return typing.cast(IngressV1Beta1Backend, result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Host is the fully qualified domain name of a network host, as defined by RFC 3986.

        Note the following deviations from the "host" part of the URI as
        defined in the RFC: 1. IPs are not allowed. Currently an IngressRuleValue
        can only apply to the IP in the Spec of the parent Ingress. 2. The ``:``
        delimiter is not respected because ports are not allowed. Currently the
        port of an Ingress is implicitly :80 for http and :443 for https. Both
        these may change in the future. Incoming requests are matched against the
        host before the IngressRuleValue.

        :default:

        - If the host is unspecified, the Ingress routes all traffic based
        on the specified IngressRuleValue.
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path is an extended POSIX regex as defined by IEEE Std 1003.1, (i.e this follows the egrep/unix syntax, not the perl syntax) matched against the path of an incoming request. Currently it can contain characters disallowed from the conventional "path" part of a URL as defined by RFC 3986. Paths must begin with a '/'.

        :default:

        - If unspecified, the path defaults to a catch all sending traffic
        to the backend.
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1Beta1Rule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.IngressV1Beta1Tls",
    jsii_struct_bases=[],
    name_mapping={"hosts": "hosts", "secret": "secret"},
)
class IngressV1Beta1Tls:
    def __init__(
        self,
        *,
        hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
        secret: typing.Optional[ISecret] = None,
    ) -> None:
        '''Represents the TLS configuration mapping that is passed to the ingress controller for SSL termination.

        :param hosts: Hosts are a list of hosts included in the TLS certificate. The values in this list must match the name/s used in the TLS Secret. Default: - If unspecified, it defaults to the wildcard host setting for the loadbalancer controller fulfilling this Ingress.
        :param secret: Secret is the secret that contains the certificate and key used to terminate SSL traffic on 443. If the SNI host in a listener conflicts with the "Host" header field used by an IngressRule, the SNI host is used for termination and value of the Host header is used for routing. Default: - If unspecified, it allows SSL routing based on SNI hostname.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if hosts is not None:
            self._values["hosts"] = hosts
        if secret is not None:
            self._values["secret"] = secret

    @builtins.property
    def hosts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Hosts are a list of hosts included in the TLS certificate.

        The values in
        this list must match the name/s used in the TLS Secret.

        :default:

        - If unspecified, it defaults to the wildcard host setting for
        the loadbalancer controller fulfilling this Ingress.
        '''
        result = self._values.get("hosts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def secret(self) -> typing.Optional[ISecret]:
        '''Secret is the secret that contains the certificate and key used to terminate SSL traffic on 443.

        If the SNI host in a listener conflicts with
        the "Host" header field used by an IngressRule, the SNI host is used for
        termination and value of the Host header is used for routing.

        :default: - If unspecified, it allows SSL routing based on SNI hostname.
        '''
        result = self._values.get("secret")
        return typing.cast(typing.Optional[ISecret], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1Beta1Tls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.MemoryResources",
    jsii_struct_bases=[],
    name_mapping={"limit": "limit", "request": "request"},
)
class MemoryResources:
    def __init__(self, *, limit: cdk8s.Size, request: cdk8s.Size) -> None:
        '''Memory request and limit.

        :param limit: 
        :param request: 
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "limit": limit,
            "request": request,
        }

    @builtins.property
    def limit(self) -> cdk8s.Size:
        result = self._values.get("limit")
        assert result is not None, "Required property 'limit' is missing"
        return typing.cast(cdk8s.Size, result)

    @builtins.property
    def request(self) -> cdk8s.Size:
        result = self._values.get("request")
        assert result is not None, "Required property 'request' is missing"
        return typing.cast(cdk8s.Size, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MemoryResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.MountOptions",
    jsii_struct_bases=[],
    name_mapping={
        "propagation": "propagation",
        "read_only": "readOnly",
        "sub_path": "subPath",
        "sub_path_expr": "subPathExpr",
    },
)
class MountOptions:
    def __init__(
        self,
        *,
        propagation: typing.Optional["MountPropagation"] = None,
        read_only: typing.Optional[builtins.bool] = None,
        sub_path: typing.Optional[builtins.str] = None,
        sub_path_expr: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options for mounts.

        :param propagation: Determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. Mount propagation allows for sharing volumes mounted by a Container to other Containers in the same Pod, or even to other Pods on the same node. Default: MountPropagation.NONE
        :param read_only: Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false. Default: false
        :param sub_path: Path within the volume from which the container's volume should be mounted.). Default: "" the volume's root
        :param sub_path_expr: Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to "" (volume's root). ``subPathExpr`` and ``subPath`` are mutually exclusive. Default: "" volume's root.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if propagation is not None:
            self._values["propagation"] = propagation
        if read_only is not None:
            self._values["read_only"] = read_only
        if sub_path is not None:
            self._values["sub_path"] = sub_path
        if sub_path_expr is not None:
            self._values["sub_path_expr"] = sub_path_expr

    @builtins.property
    def propagation(self) -> typing.Optional["MountPropagation"]:
        '''Determines how mounts are propagated from the host to container and the other way around.

        When not set, MountPropagationNone is used.

        Mount propagation allows for sharing volumes mounted by a Container to
        other Containers in the same Pod, or even to other Pods on the same node.

        :default: MountPropagation.NONE
        '''
        result = self._values.get("propagation")
        return typing.cast(typing.Optional["MountPropagation"], result)

    @builtins.property
    def read_only(self) -> typing.Optional[builtins.bool]:
        '''Mounted read-only if true, read-write otherwise (false or unspecified).

        Defaults to false.

        :default: false
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def sub_path(self) -> typing.Optional[builtins.str]:
        '''Path within the volume from which the container's volume should be mounted.).

        :default: "" the volume's root
        '''
        result = self._values.get("sub_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sub_path_expr(self) -> typing.Optional[builtins.str]:
        '''Expanded path within the volume from which the container's volume should be mounted.

        Behaves similarly to SubPath but environment variable references
        $(VAR_NAME) are expanded using the container's environment. Defaults to ""
        (volume's root).

        ``subPathExpr`` and ``subPath`` are mutually exclusive.

        :default: "" volume's root.
        '''
        result = self._values.get("sub_path_expr")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MountOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk8s-plus-21.MountPropagation")
class MountPropagation(enum.Enum):
    NONE = "NONE"
    '''This volume mount will not receive any subsequent mounts that are mounted to this volume or any of its subdirectories by the host.

    In similar
    fashion, no mounts created by the Container will be visible on the host.

    This is the default mode.

    This mode is equal to ``private`` mount propagation as described in the Linux
    kernel documentation
    '''
    HOST_TO_CONTAINER = "HOST_TO_CONTAINER"
    '''This volume mount will receive all subsequent mounts that are mounted to this volume or any of its subdirectories.

    In other words, if the host mounts anything inside the volume mount, the
    Container will see it mounted there.

    Similarly, if any Pod with Bidirectional mount propagation to the same
    volume mounts anything there, the Container with HostToContainer mount
    propagation will see it.

    This mode is equal to ``rslave`` mount propagation as described in the Linux
    kernel documentation
    '''
    BIDIRECTIONAL = "BIDIRECTIONAL"
    '''This volume mount behaves the same the HostToContainer mount.

    In addition,
    all volume mounts created by the Container will be propagated back to the
    host and to all Containers of all Pods that use the same volume

    A typical use case for this mode is a Pod with a FlexVolume or CSI driver
    or a Pod that needs to mount something on the host using a hostPath volume.

    This mode is equal to ``rshared`` mount propagation as described in the Linux
    kernel documentation

    Caution: Bidirectional mount propagation can be dangerous. It can damage
    the host operating system and therefore it is allowed only in privileged
    Containers. Familiarity with Linux kernel behavior is strongly recommended.
    In addition, any volume mounts created by Containers in Pods must be
    destroyed (unmounted) by the Containers on termination.
    '''


@jsii.data_type(
    jsii_type="cdk8s-plus-21.PathMapping",
    jsii_struct_bases=[],
    name_mapping={"path": "path", "mode": "mode"},
)
class PathMapping:
    def __init__(
        self,
        *,
        path: builtins.str,
        mode: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Maps a string key to a path within a volume.

        :param path: The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.
        :param mode: Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
        }
        if mode is not None:
            self._values["mode"] = mode

    @builtins.property
    def path(self) -> builtins.str:
        '''The relative path of the file to map the key to.

        May not be an absolute
        path. May not contain the path element '..'. May not start with the string
        '..'.
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mode(self) -> typing.Optional[jsii.Number]:
        '''Optional: mode bits to use on this file, must be a value between 0 and 0777.

        If not specified, the volume defaultMode will be used. This might be
        in conflict with other options that affect the file mode, like fsGroup, and
        the result can be other mode bits set.
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PathMapping(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PercentOrAbsolute(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-21.PercentOrAbsolute",
):
    '''Union like class repsenting either a ration in percents or an absolute number.'''

    @jsii.member(jsii_name="absolute") # type: ignore[misc]
    @builtins.classmethod
    def absolute(cls, num: jsii.Number) -> "PercentOrAbsolute":
        '''Absolute number.

        :param num: -
        '''
        return typing.cast("PercentOrAbsolute", jsii.sinvoke(cls, "absolute", [num]))

    @jsii.member(jsii_name="percent") # type: ignore[misc]
    @builtins.classmethod
    def percent(cls, percent: jsii.Number) -> "PercentOrAbsolute":
        '''Percent ratio.

        :param percent: -
        '''
        return typing.cast("PercentOrAbsolute", jsii.sinvoke(cls, "percent", [percent]))

    @jsii.member(jsii_name="isZero")
    def is_zero(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.invoke(self, "isZero", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "value"))


@jsii.enum(jsii_type="cdk8s-plus-21.PersistentVolumeAccessMode")
class PersistentVolumeAccessMode(enum.Enum):
    '''Access Modes.'''

    READ_WRITE_ONCE = "READ_WRITE_ONCE"
    '''The volume can be mounted as read-write by a single node.

    ReadWriteOnce access mode still can allow multiple pods to access
    the volume when the pods are running on the same node.
    '''
    READ_ONLY_MANY = "READ_ONLY_MANY"
    '''The volume can be mounted as read-only by many nodes.'''
    READ_WRITE_MANY = "READ_WRITE_MANY"
    '''The volume can be mounted as read-write by many nodes.'''
    READ_WRITE_ONCE_POD = "READ_WRITE_ONCE_POD"
    '''The volume can be mounted as read-write by a single Pod.

    Use ReadWriteOncePod access mode if you want to ensure that
    only one pod across whole cluster can read that PVC or write to it.
    This is only supported for CSI volumes and Kubernetes version 1.22+.
    '''


@jsii.data_type(
    jsii_type="cdk8s-plus-21.PersistentVolumeClaimVolumeOptions",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "read_only": "readOnly"},
)
class PersistentVolumeClaimVolumeOptions:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options for a PersistentVolumeClaim-based volume.

        :param name: The volume name. Default: - Derived from the PVC name.
        :param read_only: Will force the ReadOnly setting in VolumeMounts. Default: false
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The volume name.

        :default: - Derived from the PVC name.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(self) -> typing.Optional[builtins.bool]:
        '''Will force the ReadOnly setting in VolumeMounts.

        :default: false
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeClaimVolumeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk8s-plus-21.PersistentVolumeMode")
class PersistentVolumeMode(enum.Enum):
    '''Volume Modes.'''

    FILE_SYSTEM = "FILE_SYSTEM"
    '''Volume is ounted into Pods into a directory.

    If the volume is backed by a block device and the device is empty,
    Kubernetes creates a filesystem on the device before mounting it
    for the first time.
    '''
    BLOCK = "BLOCK"
    '''Use a volume as a raw block device.

    Such volume is presented into a Pod as a block device,
    without any filesystem on it. This mode is useful to provide a Pod the fastest possible way
    to access a volume, without any filesystem layer between the Pod
    and the volume. On the other hand, the application running in
    the Pod must know how to handle a raw block device
    '''


@jsii.enum(jsii_type="cdk8s-plus-21.PersistentVolumeReclaimPolicy")
class PersistentVolumeReclaimPolicy(enum.Enum):
    '''Reclaim Policies.'''

    RETAIN = "RETAIN"
    '''The Retain reclaim policy allows for manual reclamation of the resource.

    When the PersistentVolumeClaim is deleted, the PersistentVolume still exists and the
    volume is considered "released". But it is not yet available for another claim
    because the previous claimant's data remains on the volume.
    An administrator can manually reclaim the volume with the following steps:

    1. Delete the PersistentVolume. The associated storage asset in external
       infrastructure (such as an AWS EBS, GCE PD, Azure Disk, or Cinder volume) still exists after the PV is deleted.
    2. Manually clean up the data on the associated storage asset accordingly.
    3. Manually delete the associated storage asset.

    If you want to reuse the same storage asset, create a new PersistentVolume
    with the same storage asset definition.
    '''
    DELETE = "DELETE"
    '''For volume plugins that support the Delete reclaim policy, deletion removes both the PersistentVolume object from Kubernetes, as well as the associated storage asset in the external infrastructure, such as an AWS EBS, GCE PD, Azure Disk, or Cinder volume.

    Volumes that were dynamically provisioned inherit the reclaim policy of their StorageClass, which defaults to Delete.
    The administrator should configure the StorageClass according to users' expectations; otherwise,
    the PV must be edited or patched after it is created
    '''


@jsii.enum(jsii_type="cdk8s-plus-21.PodManagementPolicy")
class PodManagementPolicy(enum.Enum):
    '''Controls how pods are created during initial scale up, when replacing pods on nodes, or when scaling down.

    The default policy is ``OrderedReady``, where pods are created in increasing order
    (pod-0, then pod-1, etc) and the controller will wait until each pod is ready before
    continuing. When scaling down, the pods are removed in the opposite order.

    The alternative policy is ``Parallel`` which will create pods in parallel to match the
    desired scale without waiting, and on scale down will delete all pods at once.
    '''

    ORDERED_READY = "ORDERED_READY"
    PARALLEL = "PARALLEL"


class PodSecurityContext(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-21.PodSecurityContext",
):
    '''Holds pod-level security attributes and common container settings.'''

    def __init__(
        self,
        *,
        ensure_non_root: typing.Optional[builtins.bool] = None,
        fs_group: typing.Optional[jsii.Number] = None,
        fs_group_change_policy: typing.Optional[FsGroupChangePolicy] = None,
        group: typing.Optional[jsii.Number] = None,
        sysctls: typing.Optional[typing.Sequence["Sysctl"]] = None,
        user: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param ensure_non_root: Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. Default: false
        :param fs_group: Modify the ownership and permissions of pod volumes to this GID. Default: - Volume ownership is not changed.
        :param fs_group_change_policy: Defines behavior of changing ownership and permission of the volume before being exposed inside Pod. This field will only apply to volume types which support fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir. Default: FsGroupChangePolicy.ALWAYS
        :param group: The GID to run the entrypoint of the container process. Default: - Group configured by container runtime
        :param sysctls: Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch. Default: - No sysctls
        :param user: The UID to run the entrypoint of the container process. Default: - User specified in image metadata
        '''
        props = PodSecurityContextProps(
            ensure_non_root=ensure_non_root,
            fs_group=fs_group,
            fs_group_change_policy=fs_group_change_policy,
            group=group,
            sysctls=sysctls,
            user=user,
        )

        jsii.create(self.__class__, self, [props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ensureNonRoot")
    def ensure_non_root(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "ensureNonRoot"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fsGroupChangePolicy")
    def fs_group_change_policy(self) -> FsGroupChangePolicy:
        return typing.cast(FsGroupChangePolicy, jsii.get(self, "fsGroupChangePolicy"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sysctls")
    def sysctls(self) -> typing.List["Sysctl"]:
        return typing.cast(typing.List["Sysctl"], jsii.get(self, "sysctls"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fsGroup")
    def fs_group(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fsGroup"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="group")
    def group(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "group"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="user")
    def user(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "user"))


@jsii.data_type(
    jsii_type="cdk8s-plus-21.PodSecurityContextProps",
    jsii_struct_bases=[],
    name_mapping={
        "ensure_non_root": "ensureNonRoot",
        "fs_group": "fsGroup",
        "fs_group_change_policy": "fsGroupChangePolicy",
        "group": "group",
        "sysctls": "sysctls",
        "user": "user",
    },
)
class PodSecurityContextProps:
    def __init__(
        self,
        *,
        ensure_non_root: typing.Optional[builtins.bool] = None,
        fs_group: typing.Optional[jsii.Number] = None,
        fs_group_change_policy: typing.Optional[FsGroupChangePolicy] = None,
        group: typing.Optional[jsii.Number] = None,
        sysctls: typing.Optional[typing.Sequence["Sysctl"]] = None,
        user: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for ``PodSecurityContext``.

        :param ensure_non_root: Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. Default: false
        :param fs_group: Modify the ownership and permissions of pod volumes to this GID. Default: - Volume ownership is not changed.
        :param fs_group_change_policy: Defines behavior of changing ownership and permission of the volume before being exposed inside Pod. This field will only apply to volume types which support fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir. Default: FsGroupChangePolicy.ALWAYS
        :param group: The GID to run the entrypoint of the container process. Default: - Group configured by container runtime
        :param sysctls: Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch. Default: - No sysctls
        :param user: The UID to run the entrypoint of the container process. Default: - User specified in image metadata
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if ensure_non_root is not None:
            self._values["ensure_non_root"] = ensure_non_root
        if fs_group is not None:
            self._values["fs_group"] = fs_group
        if fs_group_change_policy is not None:
            self._values["fs_group_change_policy"] = fs_group_change_policy
        if group is not None:
            self._values["group"] = group
        if sysctls is not None:
            self._values["sysctls"] = sysctls
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def ensure_non_root(self) -> typing.Optional[builtins.bool]:
        '''Indicates that the container must run as a non-root user.

        If true, the Kubelet will validate the image at runtime to ensure that it does
        not run as UID 0 (root) and fail to start the container if it does.

        :default: false
        '''
        result = self._values.get("ensure_non_root")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def fs_group(self) -> typing.Optional[jsii.Number]:
        '''Modify the ownership and permissions of pod volumes to this GID.

        :default: - Volume ownership is not changed.
        '''
        result = self._values.get("fs_group")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def fs_group_change_policy(self) -> typing.Optional[FsGroupChangePolicy]:
        '''Defines behavior of changing ownership and permission of the volume before being exposed inside Pod.

        This field will only apply to volume types which support fsGroup based ownership(and permissions).
        It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir.

        :default: FsGroupChangePolicy.ALWAYS
        '''
        result = self._values.get("fs_group_change_policy")
        return typing.cast(typing.Optional[FsGroupChangePolicy], result)

    @builtins.property
    def group(self) -> typing.Optional[jsii.Number]:
        '''The GID to run the entrypoint of the container process.

        :default: - Group configured by container runtime
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sysctls(self) -> typing.Optional[typing.List["Sysctl"]]:
        '''Sysctls hold a list of namespaced sysctls used for the pod.

        Pods with unsupported sysctls (by the container runtime) might fail to launch.

        :default: - No sysctls
        '''
        result = self._values.get("sysctls")
        return typing.cast(typing.Optional[typing.List["Sysctl"]], result)

    @builtins.property
    def user(self) -> typing.Optional[jsii.Number]:
        '''The UID to run the entrypoint of the container process.

        :default: - User specified in image metadata
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityContextProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IPodSpec)
class PodSpec(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-21.PodSpec"):
    '''Provides read/write capabilities ontop of a ``PodSpecProps``.'''

    def __init__(
        self,
        *,
        containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        docker_registry_auth: typing.Optional["DockerConfigSecret"] = None,
        host_aliases: typing.Optional[typing.Sequence[HostAlias]] = None,
        init_containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        restart_policy: typing.Optional["RestartPolicy"] = None,
        security_context: typing.Optional[PodSecurityContextProps] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence["Volume"]] = None,
    ) -> None:
        '''
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        '''
        props = PodSpecProps(
            containers=containers,
            docker_registry_auth=docker_registry_auth,
            host_aliases=host_aliases,
            init_containers=init_containers,
            restart_policy=restart_policy,
            security_context=security_context,
            service_account=service_account,
            volumes=volumes,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="addContainer")
    def add_container(
        self,
        *,
        image: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, EnvValue]] = None,
        image_pull_policy: typing.Optional[ImagePullPolicy] = None,
        lifecycle: typing.Optional[ContainerLifecycle] = None,
        liveness: typing.Optional["Probe"] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        readiness: typing.Optional["Probe"] = None,
        resources: typing.Optional["Resources"] = None,
        security_context: typing.Optional[ContainerSecurityContextProps] = None,
        startup: typing.Optional["Probe"] = None,
        volume_mounts: typing.Optional[typing.Sequence["VolumeMount"]] = None,
        working_dir: typing.Optional[builtins.str] = None,
    ) -> Container:
        '''Add a container to the pod.

        :param image: Docker image name.
        :param args: Arguments to the entrypoint. The docker image's CMD is used if ``command`` is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. Default: []
        :param command: Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell Default: - The docker image's ENTRYPOINT.
        :param env: List of environment variables to set in the container. Cannot be updated. Default: - No environment variables.
        :param image_pull_policy: Image pull policy for this container. Default: ImagePullPolicy.ALWAYS
        :param lifecycle: Describes actions that the management system should take in response to container lifecycle events.
        :param liveness: Periodic probe of container liveness. Container will be restarted if the probe fails. Default: - no liveness probe is defined
        :param name: Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. Default: 'main'
        :param port: Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. Default: - No port is exposed.
        :param readiness: Determines when the container is ready to serve traffic. Default: - no readiness probe is defined
        :param resources: Compute resources (CPU and memory requests and limits) required by the container.
        :param security_context: SecurityContext defines the security options the container should be run with. If set, the fields override equivalent fields of the pod's security context. Default: ensureNonRoot: false privileged: false readOnlyRootFilesystem: false
        :param startup: StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully Default: - no startup probe is defined.
        :param volume_mounts: Pod volumes to mount into the container's filesystem. Cannot be updated.
        :param working_dir: Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. Default: - The container runtime's default.
        '''
        container = ContainerProps(
            image=image,
            args=args,
            command=command,
            env=env,
            image_pull_policy=image_pull_policy,
            lifecycle=lifecycle,
            liveness=liveness,
            name=name,
            port=port,
            readiness=readiness,
            resources=resources,
            security_context=security_context,
            startup=startup,
            volume_mounts=volume_mounts,
            working_dir=working_dir,
        )

        return typing.cast(Container, jsii.invoke(self, "addContainer", [container]))

    @jsii.member(jsii_name="addHostAlias")
    def add_host_alias(
        self,
        *,
        hostnames: typing.Sequence[builtins.str],
        ip: builtins.str,
    ) -> None:
        '''
        :param hostnames: Hostnames for the chosen IP address.
        :param ip: IP address of the host file entry.
        '''
        host_alias = HostAlias(hostnames=hostnames, ip=ip)

        return typing.cast(None, jsii.invoke(self, "addHostAlias", [host_alias]))

    @jsii.member(jsii_name="addInitContainer")
    def add_init_container(
        self,
        *,
        image: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, EnvValue]] = None,
        image_pull_policy: typing.Optional[ImagePullPolicy] = None,
        lifecycle: typing.Optional[ContainerLifecycle] = None,
        liveness: typing.Optional["Probe"] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        readiness: typing.Optional["Probe"] = None,
        resources: typing.Optional["Resources"] = None,
        security_context: typing.Optional[ContainerSecurityContextProps] = None,
        startup: typing.Optional["Probe"] = None,
        volume_mounts: typing.Optional[typing.Sequence["VolumeMount"]] = None,
        working_dir: typing.Optional[builtins.str] = None,
    ) -> Container:
        '''Add an init container to the pod.

        :param image: Docker image name.
        :param args: Arguments to the entrypoint. The docker image's CMD is used if ``command`` is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. Default: []
        :param command: Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell Default: - The docker image's ENTRYPOINT.
        :param env: List of environment variables to set in the container. Cannot be updated. Default: - No environment variables.
        :param image_pull_policy: Image pull policy for this container. Default: ImagePullPolicy.ALWAYS
        :param lifecycle: Describes actions that the management system should take in response to container lifecycle events.
        :param liveness: Periodic probe of container liveness. Container will be restarted if the probe fails. Default: - no liveness probe is defined
        :param name: Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. Default: 'main'
        :param port: Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. Default: - No port is exposed.
        :param readiness: Determines when the container is ready to serve traffic. Default: - no readiness probe is defined
        :param resources: Compute resources (CPU and memory requests and limits) required by the container.
        :param security_context: SecurityContext defines the security options the container should be run with. If set, the fields override equivalent fields of the pod's security context. Default: ensureNonRoot: false privileged: false readOnlyRootFilesystem: false
        :param startup: StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully Default: - no startup probe is defined.
        :param volume_mounts: Pod volumes to mount into the container's filesystem. Cannot be updated.
        :param working_dir: Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. Default: - The container runtime's default.
        '''
        container = ContainerProps(
            image=image,
            args=args,
            command=command,
            env=env,
            image_pull_policy=image_pull_policy,
            lifecycle=lifecycle,
            liveness=liveness,
            name=name,
            port=port,
            readiness=readiness,
            resources=resources,
            security_context=security_context,
            startup=startup,
            volume_mounts=volume_mounts,
            working_dir=working_dir,
        )

        return typing.cast(Container, jsii.invoke(self, "addInitContainer", [container]))

    @jsii.member(jsii_name="addVolume")
    def add_volume(self, volume: "Volume") -> None:
        '''Add a volume to the pod.

        :param volume: -
        '''
        return typing.cast(None, jsii.invoke(self, "addVolume", [volume]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="containers")
    def containers(self) -> typing.List[Container]:
        '''The containers belonging to the pod.

        Use ``addContainer`` to add containers.
        '''
        return typing.cast(typing.List[Container], jsii.get(self, "containers"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hostAliases")
    def host_aliases(self) -> typing.List[HostAlias]:
        '''An optional list of hosts and IPs that will be injected into the pod's hosts file if specified.

        This is only valid for non-hostNetwork pods.
        '''
        return typing.cast(typing.List[HostAlias], jsii.get(self, "hostAliases"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="initContainers")
    def init_containers(self) -> typing.List[Container]:
        '''The init containers belonging to the pod.

        Use ``addInitContainer`` to add init containers.
        '''
        return typing.cast(typing.List[Container], jsii.get(self, "initContainers"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityContext")
    def security_context(self) -> PodSecurityContext:
        return typing.cast(PodSecurityContext, jsii.get(self, "securityContext"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="volumes")
    def volumes(self) -> typing.List["Volume"]:
        '''The volumes associated with this pod.

        Use ``addVolume`` to add volumes.
        '''
        return typing.cast(typing.List["Volume"], jsii.get(self, "volumes"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dockerRegistryAuth")
    def docker_registry_auth(self) -> typing.Optional["DockerConfigSecret"]:
        return typing.cast(typing.Optional["DockerConfigSecret"], jsii.get(self, "dockerRegistryAuth"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="restartPolicy")
    def restart_policy(self) -> typing.Optional["RestartPolicy"]:
        '''Restart policy for all containers within the pod.'''
        return typing.cast(typing.Optional["RestartPolicy"], jsii.get(self, "restartPolicy"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> typing.Optional[IServiceAccount]:
        '''The service account used to run this pod.'''
        return typing.cast(typing.Optional[IServiceAccount], jsii.get(self, "serviceAccount"))


@jsii.data_type(
    jsii_type="cdk8s-plus-21.PodSpecProps",
    jsii_struct_bases=[],
    name_mapping={
        "containers": "containers",
        "docker_registry_auth": "dockerRegistryAuth",
        "host_aliases": "hostAliases",
        "init_containers": "initContainers",
        "restart_policy": "restartPolicy",
        "security_context": "securityContext",
        "service_account": "serviceAccount",
        "volumes": "volumes",
    },
)
class PodSpecProps:
    def __init__(
        self,
        *,
        containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        docker_registry_auth: typing.Optional["DockerConfigSecret"] = None,
        host_aliases: typing.Optional[typing.Sequence[HostAlias]] = None,
        init_containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        restart_policy: typing.Optional["RestartPolicy"] = None,
        security_context: typing.Optional[PodSecurityContextProps] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence["Volume"]] = None,
    ) -> None:
        '''Properties of a ``PodSpec``.

        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        '''
        if isinstance(security_context, dict):
            security_context = PodSecurityContextProps(**security_context)
        self._values: typing.Dict[str, typing.Any] = {}
        if containers is not None:
            self._values["containers"] = containers
        if docker_registry_auth is not None:
            self._values["docker_registry_auth"] = docker_registry_auth
        if host_aliases is not None:
            self._values["host_aliases"] = host_aliases
        if init_containers is not None:
            self._values["init_containers"] = init_containers
        if restart_policy is not None:
            self._values["restart_policy"] = restart_policy
        if security_context is not None:
            self._values["security_context"] = security_context
        if service_account is not None:
            self._values["service_account"] = service_account
        if volumes is not None:
            self._values["volumes"] = volumes

    @builtins.property
    def containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of containers belonging to the pod.

        Containers cannot currently be
        added or removed. There must be at least one container in a Pod.

        You can add additionnal containers using ``podSpec.addContainer()``

        :default: - No containers. Note that a pod spec must include at least one container.
        '''
        result = self._values.get("containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def docker_registry_auth(self) -> typing.Optional["DockerConfigSecret"]:
        '''A secret containing docker credentials for authenticating to a registry.

        :default: - No auth. Images are assumed to be publicly available.
        '''
        result = self._values.get("docker_registry_auth")
        return typing.cast(typing.Optional["DockerConfigSecret"], result)

    @builtins.property
    def host_aliases(self) -> typing.Optional[typing.List[HostAlias]]:
        '''HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.

        :schema: io.k8s.api.core.v1.HostAlias
        '''
        result = self._values.get("host_aliases")
        return typing.cast(typing.Optional[typing.List[HostAlias]], result)

    @builtins.property
    def init_containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of initialization containers belonging to the pod.

        Init containers are executed in order prior to containers being started.
        If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy.
        The name for an init container or normal container must be unique among all containers.
        Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes.
        The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit
        for each resource type, and then using the max of of that value or the sum of the normal containers.
        Limits are applied to init containers in a similar fashion.

        Init containers cannot currently be added ,removed or updated.

        :default: - No init containers.

        :see: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
        '''
        result = self._values.get("init_containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def restart_policy(self) -> typing.Optional["RestartPolicy"]:
        '''Restart policy for all containers within the pod.

        :default: RestartPolicy.ALWAYS

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy
        '''
        result = self._values.get("restart_policy")
        return typing.cast(typing.Optional["RestartPolicy"], result)

    @builtins.property
    def security_context(self) -> typing.Optional[PodSecurityContextProps]:
        '''SecurityContext holds pod-level security attributes and common container settings.

        :default:

        fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS
        ensureNonRoot: false
        '''
        result = self._values.get("security_context")
        return typing.cast(typing.Optional[PodSecurityContextProps], result)

    @builtins.property
    def service_account(self) -> typing.Optional[IServiceAccount]:
        '''A service account provides an identity for processes that run in a Pod.

        When you (a human) access the cluster (for example, using kubectl), you are
        authenticated by the apiserver as a particular User Account (currently this
        is usually admin, unless your cluster administrator has customized your
        cluster). Processes in containers inside pods can also contact the
        apiserver. When they do, they are authenticated as a particular Service
        Account (for example, default).

        :default: - No service account.

        :see: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[IServiceAccount], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List["Volume"]]:
        '''List of volumes that can be mounted by containers belonging to the pod.

        You can also add volumes later using ``podSpec.addVolume()``

        :default: - No volumes.

        :see: https://kubernetes.io/docs/concepts/storage/volumes
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List["Volume"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSpecProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IPodTemplate)
class PodTemplate(
    PodSpec,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-21.PodTemplate",
):
    '''Provides read/write capabilities ontop of a ``PodTemplateProps``.'''

    def __init__(
        self,
        *,
        pod_metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        docker_registry_auth: typing.Optional["DockerConfigSecret"] = None,
        host_aliases: typing.Optional[typing.Sequence[HostAlias]] = None,
        init_containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        restart_policy: typing.Optional["RestartPolicy"] = None,
        security_context: typing.Optional[PodSecurityContextProps] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence["Volume"]] = None,
    ) -> None:
        '''
        :param pod_metadata: The pod metadata.
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        '''
        props = PodTemplateProps(
            pod_metadata=pod_metadata,
            containers=containers,
            docker_registry_auth=docker_registry_auth,
            host_aliases=host_aliases,
            init_containers=init_containers,
            restart_policy=restart_policy,
            security_context=security_context,
            service_account=service_account,
            volumes=volumes,
        )

        jsii.create(self.__class__, self, [props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="podMetadata")
    def pod_metadata(self) -> cdk8s.ApiObjectMetadataDefinition:
        '''Provides read/write access to the underlying pod metadata of the resource.'''
        return typing.cast(cdk8s.ApiObjectMetadataDefinition, jsii.get(self, "podMetadata"))


@jsii.data_type(
    jsii_type="cdk8s-plus-21.PodTemplateProps",
    jsii_struct_bases=[PodSpecProps],
    name_mapping={
        "containers": "containers",
        "docker_registry_auth": "dockerRegistryAuth",
        "host_aliases": "hostAliases",
        "init_containers": "initContainers",
        "restart_policy": "restartPolicy",
        "security_context": "securityContext",
        "service_account": "serviceAccount",
        "volumes": "volumes",
        "pod_metadata": "podMetadata",
    },
)
class PodTemplateProps(PodSpecProps):
    def __init__(
        self,
        *,
        containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        docker_registry_auth: typing.Optional["DockerConfigSecret"] = None,
        host_aliases: typing.Optional[typing.Sequence[HostAlias]] = None,
        init_containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        restart_policy: typing.Optional["RestartPolicy"] = None,
        security_context: typing.Optional[PodSecurityContextProps] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence["Volume"]] = None,
        pod_metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
    ) -> None:
        '''Properties of a ``PodTemplate``.

        Adds metadata information on top of the spec.

        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        :param pod_metadata: The pod metadata.
        '''
        if isinstance(security_context, dict):
            security_context = PodSecurityContextProps(**security_context)
        if isinstance(pod_metadata, dict):
            pod_metadata = cdk8s.ApiObjectMetadata(**pod_metadata)
        self._values: typing.Dict[str, typing.Any] = {}
        if containers is not None:
            self._values["containers"] = containers
        if docker_registry_auth is not None:
            self._values["docker_registry_auth"] = docker_registry_auth
        if host_aliases is not None:
            self._values["host_aliases"] = host_aliases
        if init_containers is not None:
            self._values["init_containers"] = init_containers
        if restart_policy is not None:
            self._values["restart_policy"] = restart_policy
        if security_context is not None:
            self._values["security_context"] = security_context
        if service_account is not None:
            self._values["service_account"] = service_account
        if volumes is not None:
            self._values["volumes"] = volumes
        if pod_metadata is not None:
            self._values["pod_metadata"] = pod_metadata

    @builtins.property
    def containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of containers belonging to the pod.

        Containers cannot currently be
        added or removed. There must be at least one container in a Pod.

        You can add additionnal containers using ``podSpec.addContainer()``

        :default: - No containers. Note that a pod spec must include at least one container.
        '''
        result = self._values.get("containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def docker_registry_auth(self) -> typing.Optional["DockerConfigSecret"]:
        '''A secret containing docker credentials for authenticating to a registry.

        :default: - No auth. Images are assumed to be publicly available.
        '''
        result = self._values.get("docker_registry_auth")
        return typing.cast(typing.Optional["DockerConfigSecret"], result)

    @builtins.property
    def host_aliases(self) -> typing.Optional[typing.List[HostAlias]]:
        '''HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.

        :schema: io.k8s.api.core.v1.HostAlias
        '''
        result = self._values.get("host_aliases")
        return typing.cast(typing.Optional[typing.List[HostAlias]], result)

    @builtins.property
    def init_containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of initialization containers belonging to the pod.

        Init containers are executed in order prior to containers being started.
        If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy.
        The name for an init container or normal container must be unique among all containers.
        Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes.
        The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit
        for each resource type, and then using the max of of that value or the sum of the normal containers.
        Limits are applied to init containers in a similar fashion.

        Init containers cannot currently be added ,removed or updated.

        :default: - No init containers.

        :see: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
        '''
        result = self._values.get("init_containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def restart_policy(self) -> typing.Optional["RestartPolicy"]:
        '''Restart policy for all containers within the pod.

        :default: RestartPolicy.ALWAYS

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy
        '''
        result = self._values.get("restart_policy")
        return typing.cast(typing.Optional["RestartPolicy"], result)

    @builtins.property
    def security_context(self) -> typing.Optional[PodSecurityContextProps]:
        '''SecurityContext holds pod-level security attributes and common container settings.

        :default:

        fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS
        ensureNonRoot: false
        '''
        result = self._values.get("security_context")
        return typing.cast(typing.Optional[PodSecurityContextProps], result)

    @builtins.property
    def service_account(self) -> typing.Optional[IServiceAccount]:
        '''A service account provides an identity for processes that run in a Pod.

        When you (a human) access the cluster (for example, using kubectl), you are
        authenticated by the apiserver as a particular User Account (currently this
        is usually admin, unless your cluster administrator has customized your
        cluster). Processes in containers inside pods can also contact the
        apiserver. When they do, they are authenticated as a particular Service
        Account (for example, default).

        :default: - No service account.

        :see: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[IServiceAccount], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List["Volume"]]:
        '''List of volumes that can be mounted by containers belonging to the pod.

        You can also add volumes later using ``podSpec.addVolume()``

        :default: - No volumes.

        :see: https://kubernetes.io/docs/concepts/storage/volumes
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List["Volume"]], result)

    @builtins.property
    def pod_metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''The pod metadata.'''
        result = self._values.get("pod_metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Probe(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-21.Probe"):
    '''Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.'''

    @jsii.member(jsii_name="fromCommand") # type: ignore[misc]
    @builtins.classmethod
    def from_command(
        cls,
        command: typing.Sequence[builtins.str],
        *,
        failure_threshold: typing.Optional[jsii.Number] = None,
        initial_delay_seconds: typing.Optional[cdk8s.Duration] = None,
        period_seconds: typing.Optional[cdk8s.Duration] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[cdk8s.Duration] = None,
    ) -> "Probe":
        '''Defines a probe based on a command which is executed within the container.

        :param command: The command to execute.
        :param failure_threshold: Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. Default: 3
        :param initial_delay_seconds: Number of seconds after the container has started before liveness probes are initiated. Default: - immediate
        :param period_seconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. Default: Duration.seconds(10) Minimum value is 1.
        :param success_threshold: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. Default: 1 Must be 1 for liveness and startup. Minimum value is 1.
        :param timeout_seconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. Default: Duration.seconds(1)
        '''
        options = CommandProbeOptions(
            failure_threshold=failure_threshold,
            initial_delay_seconds=initial_delay_seconds,
            period_seconds=period_seconds,
            success_threshold=success_threshold,
            timeout_seconds=timeout_seconds,
        )

        return typing.cast("Probe", jsii.sinvoke(cls, "fromCommand", [command, options]))

    @jsii.member(jsii_name="fromHttpGet") # type: ignore[misc]
    @builtins.classmethod
    def from_http_get(
        cls,
        path: builtins.str,
        *,
        port: typing.Optional[jsii.Number] = None,
        failure_threshold: typing.Optional[jsii.Number] = None,
        initial_delay_seconds: typing.Optional[cdk8s.Duration] = None,
        period_seconds: typing.Optional[cdk8s.Duration] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[cdk8s.Duration] = None,
    ) -> "Probe":
        '''Defines a probe based on an HTTP GET request to the IP address of the container.

        :param path: The URL path to hit.
        :param port: The TCP port to use when sending the GET request. Default: - defaults to ``container.port``.
        :param failure_threshold: Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. Default: 3
        :param initial_delay_seconds: Number of seconds after the container has started before liveness probes are initiated. Default: - immediate
        :param period_seconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. Default: Duration.seconds(10) Minimum value is 1.
        :param success_threshold: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. Default: 1 Must be 1 for liveness and startup. Minimum value is 1.
        :param timeout_seconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. Default: Duration.seconds(1)
        '''
        options = HttpGetProbeOptions(
            port=port,
            failure_threshold=failure_threshold,
            initial_delay_seconds=initial_delay_seconds,
            period_seconds=period_seconds,
            success_threshold=success_threshold,
            timeout_seconds=timeout_seconds,
        )

        return typing.cast("Probe", jsii.sinvoke(cls, "fromHttpGet", [path, options]))

    @jsii.member(jsii_name="fromTcpSocket") # type: ignore[misc]
    @builtins.classmethod
    def from_tcp_socket(
        cls,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        failure_threshold: typing.Optional[jsii.Number] = None,
        initial_delay_seconds: typing.Optional[cdk8s.Duration] = None,
        period_seconds: typing.Optional[cdk8s.Duration] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[cdk8s.Duration] = None,
    ) -> "Probe":
        '''Defines a probe based opening a connection to a TCP socket on the container.

        :param host: The host name to connect to on the container. Default: - defaults to the pod IP
        :param port: The TCP port to connect to on the container. Default: - defaults to ``container.port``.
        :param failure_threshold: Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. Default: 3
        :param initial_delay_seconds: Number of seconds after the container has started before liveness probes are initiated. Default: - immediate
        :param period_seconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. Default: Duration.seconds(10) Minimum value is 1.
        :param success_threshold: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. Default: 1 Must be 1 for liveness and startup. Minimum value is 1.
        :param timeout_seconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. Default: Duration.seconds(1)
        '''
        options = TcpSocketProbeOptions(
            host=host,
            port=port,
            failure_threshold=failure_threshold,
            initial_delay_seconds=initial_delay_seconds,
            period_seconds=period_seconds,
            success_threshold=success_threshold,
            timeout_seconds=timeout_seconds,
        )

        return typing.cast("Probe", jsii.sinvoke(cls, "fromTcpSocket", [options]))


@jsii.data_type(
    jsii_type="cdk8s-plus-21.ProbeOptions",
    jsii_struct_bases=[],
    name_mapping={
        "failure_threshold": "failureThreshold",
        "initial_delay_seconds": "initialDelaySeconds",
        "period_seconds": "periodSeconds",
        "success_threshold": "successThreshold",
        "timeout_seconds": "timeoutSeconds",
    },
)
class ProbeOptions:
    def __init__(
        self,
        *,
        failure_threshold: typing.Optional[jsii.Number] = None,
        initial_delay_seconds: typing.Optional[cdk8s.Duration] = None,
        period_seconds: typing.Optional[cdk8s.Duration] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[cdk8s.Duration] = None,
    ) -> None:
        '''Probe options.

        :param failure_threshold: Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. Default: 3
        :param initial_delay_seconds: Number of seconds after the container has started before liveness probes are initiated. Default: - immediate
        :param period_seconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. Default: Duration.seconds(10) Minimum value is 1.
        :param success_threshold: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. Default: 1 Must be 1 for liveness and startup. Minimum value is 1.
        :param timeout_seconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. Default: Duration.seconds(1)
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if failure_threshold is not None:
            self._values["failure_threshold"] = failure_threshold
        if initial_delay_seconds is not None:
            self._values["initial_delay_seconds"] = initial_delay_seconds
        if period_seconds is not None:
            self._values["period_seconds"] = period_seconds
        if success_threshold is not None:
            self._values["success_threshold"] = success_threshold
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def failure_threshold(self) -> typing.Optional[jsii.Number]:
        '''Minimum consecutive failures for the probe to be considered failed after having succeeded.

        Defaults to 3. Minimum value is 1.

        :default: 3
        '''
        result = self._values.get("failure_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def initial_delay_seconds(self) -> typing.Optional[cdk8s.Duration]:
        '''Number of seconds after the container has started before liveness probes are initiated.

        :default: - immediate

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
        '''
        result = self._values.get("initial_delay_seconds")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def period_seconds(self) -> typing.Optional[cdk8s.Duration]:
        '''How often (in seconds) to perform the probe.

        Default to 10 seconds. Minimum value is 1.

        :default: Duration.seconds(10) Minimum value is 1.
        '''
        result = self._values.get("period_seconds")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def success_threshold(self) -> typing.Optional[jsii.Number]:
        '''Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1.

        Must be 1 for liveness and startup. Minimum value is 1.

        :default: 1 Must be 1 for liveness and startup. Minimum value is 1.
        '''
        result = self._values.get("success_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[cdk8s.Duration]:
        '''Number of seconds after which the probe times out.

        Defaults to 1 second. Minimum value is 1.

        :default: Duration.seconds(1)

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
        '''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProbeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk8s-plus-21.Protocol")
class Protocol(enum.Enum):
    TCP = "TCP"
    UDP = "UDP"
    SCTP = "SCTP"


@jsii.implements(IResource)
class Resource(
    constructs.Construct,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="cdk8s-plus-21.Resource",
):
    '''Base class for all Kubernetes objects in stdk8s.

    Represents a single
    resource.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        node_factory: typing.Optional[constructs.INodeFactory] = None,
    ) -> None:
        '''Creates a new construct node.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings. If the ID includes a path separator (``/``), then it will be replaced by double dash ``--``.
        :param node_factory: A factory for attaching ``Node``s to the construct. Default: - the default ``Node`` is associated
        '''
        options = constructs.ConstructOptions(node_factory=node_factory)

        jsii.create(self.__class__, self, [scope, id, options])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="apiObject")
    @abc.abstractmethod
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.'''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> cdk8s.ApiObjectMetadataDefinition:
        return typing.cast(cdk8s.ApiObjectMetadataDefinition, jsii.get(self, "metadata"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of this API object.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))


class _ResourceProxy(Resource):
    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.'''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Resource).__jsii_proxy_class__ = lambda : _ResourceProxy


@jsii.enum(jsii_type="cdk8s-plus-21.ResourceFieldPaths")
class ResourceFieldPaths(enum.Enum):
    CPU_LIMIT = "CPU_LIMIT"
    '''CPU limit of the container.'''
    MEMORY_LIMIT = "MEMORY_LIMIT"
    '''Memory limit of the container.'''
    CPU_REQUEST = "CPU_REQUEST"
    '''CPU request of the container.'''
    MEMORY_REQUEST = "MEMORY_REQUEST"
    '''Memory request of the container.'''
    STORAGE_LIMIT = "STORAGE_LIMIT"
    '''Ephemeral storage limit of the container.'''
    STORAGE_REQUEST = "STORAGE_REQUEST"
    '''Ephemeral storage request of the container.'''


@jsii.data_type(
    jsii_type="cdk8s-plus-21.ResourceProps",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata"},
)
class ResourceProps:
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
    ) -> None:
        '''Initialization properties for resources.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.Resources",
    jsii_struct_bases=[],
    name_mapping={"cpu": "cpu", "memory": "memory"},
)
class Resources:
    def __init__(self, *, cpu: CpuResources, memory: MemoryResources) -> None:
        '''CPU and memory compute resources.

        :param cpu: 
        :param memory: 
        '''
        if isinstance(cpu, dict):
            cpu = CpuResources(**cpu)
        if isinstance(memory, dict):
            memory = MemoryResources(**memory)
        self._values: typing.Dict[str, typing.Any] = {
            "cpu": cpu,
            "memory": memory,
        }

    @builtins.property
    def cpu(self) -> CpuResources:
        result = self._values.get("cpu")
        assert result is not None, "Required property 'cpu' is missing"
        return typing.cast(CpuResources, result)

    @builtins.property
    def memory(self) -> MemoryResources:
        result = self._values.get("memory")
        assert result is not None, "Required property 'memory' is missing"
        return typing.cast(MemoryResources, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Resources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk8s-plus-21.RestartPolicy")
class RestartPolicy(enum.Enum):
    '''Restart policy for all containers within the pod.'''

    ALWAYS = "ALWAYS"
    '''Always restart the pod after it exits.'''
    ON_FAILURE = "ON_FAILURE"
    '''Only restart if the pod exits with a non-zero exit code.'''
    NEVER = "NEVER"
    '''Never restart the pod.'''


@jsii.implements(ISecret)
class Secret(Resource, metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-21.Secret"):
    '''Kubernetes Secrets let you store and manage sensitive information, such as passwords, OAuth tokens, and ssh keys.

    Storing confidential information in a
    Secret is safer and more flexible than putting it verbatim in a Pod
    definition or in a container image.

    :see: https://kubernetes.io/docs/concepts/configuration/secret
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        string_data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
        immutable: typing.Optional[builtins.bool] = None,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param string_data: stringData allows specifying non-binary secret data in string form. It is provided as a write-only convenience method. All keys and values are merged into the data field on write, overwriting any existing values. It is never output when reading from the API.
        :param type: Optional type associated with the secret. Used to facilitate programmatic handling of secret data by various controllers. Default: undefined - Don't set a type.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        props = SecretProps(
            string_data=string_data, type=type, immutable=immutable, metadata=metadata
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromSecretName") # type: ignore[misc]
    @builtins.classmethod
    def from_secret_name(cls, name: builtins.str) -> ISecret:
        '''Imports a secret from the cluster as a reference.

        :param name: The name of the secret to reference.
        '''
        return typing.cast(ISecret, jsii.sinvoke(cls, "fromSecretName", [name]))

    @jsii.member(jsii_name="addStringData")
    def add_string_data(self, key: builtins.str, value: builtins.str) -> None:
        '''Adds a string data field to the secert.

        :param key: Key.
        :param value: Value.
        '''
        return typing.cast(None, jsii.invoke(self, "addStringData", [key, value]))

    @jsii.member(jsii_name="getStringData")
    def get_string_data(self, key: builtins.str) -> typing.Optional[builtins.str]:
        '''Gets a string data by key or undefined.

        :param key: Key.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "getStringData", [key]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="immutable")
    def immutable(self) -> builtins.bool:
        '''Whether or not the secret is immutable.'''
        return typing.cast(builtins.bool, jsii.get(self, "immutable"))


@jsii.data_type(
    jsii_type="cdk8s-plus-21.SecretValue",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "secret": "secret"},
)
class SecretValue:
    def __init__(self, *, key: builtins.str, secret: ISecret) -> None:
        '''Represents a specific value in JSON secret.

        :param key: The JSON key.
        :param secret: The secret.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "secret": secret,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''The JSON key.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secret(self) -> ISecret:
        '''The secret.'''
        result = self._values.get("secret")
        assert result is not None, "Required property 'secret' is missing"
        return typing.cast(ISecret, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecretValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.SecretVolumeOptions",
    jsii_struct_bases=[],
    name_mapping={
        "default_mode": "defaultMode",
        "items": "items",
        "name": "name",
        "optional": "optional",
    },
)
class SecretVolumeOptions:
    def __init__(
        self,
        *,
        default_mode: typing.Optional[jsii.Number] = None,
        items: typing.Optional[typing.Mapping[builtins.str, PathMapping]] = None,
        name: typing.Optional[builtins.str] = None,
        optional: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options for the Secret-based volume.

        :param default_mode: Mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. Default: 644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
        :param items: If unspecified, each key-value pair in the Data field of the referenced secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. Default: - no mapping
        :param name: The volume name. Default: - auto-generated
        :param optional: Specify whether the secret or its keys must be defined. Default: - undocumented
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if default_mode is not None:
            self._values["default_mode"] = default_mode
        if items is not None:
            self._values["items"] = items
        if name is not None:
            self._values["name"] = name
        if optional is not None:
            self._values["optional"] = optional

    @builtins.property
    def default_mode(self) -> typing.Optional[jsii.Number]:
        '''Mode bits to use on created files by default.

        Must be a value between 0 and
        0777. Defaults to 0644. Directories within the path are not affected by
        this setting. This might be in conflict with other options that affect the
        file mode, like fsGroup, and the result can be other mode bits set.

        :default:

        644. Directories within the path are not affected by this
        setting. This might be in conflict with other options that affect the file
        mode, like fsGroup, and the result can be other mode bits set.
        '''
        result = self._values.get("default_mode")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def items(self) -> typing.Optional[typing.Mapping[builtins.str, PathMapping]]:
        '''If unspecified, each key-value pair in the Data field of the referenced secret will be projected into the volume as a file whose name is the key and content is the value.

        If specified, the listed keys will be projected
        into the specified paths, and unlisted keys will not be present. If a key
        is specified which is not present in the secret, the volume setup will
        error unless it is marked optional. Paths must be relative and may not
        contain the '..' path or start with '..'.

        :default: - no mapping
        '''
        result = self._values.get("items")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, PathMapping]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The volume name.

        :default: - auto-generated
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optional(self) -> typing.Optional[builtins.bool]:
        '''Specify whether the secret or its keys must be defined.

        :default: - undocumented
        '''
        result = self._values.get("optional")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecretVolumeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Service(Resource, metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-21.Service"):
    '''An abstract way to expose an application running on a set of Pods as a network service.

    With Kubernetes you don't need to modify your application to use an unfamiliar service discovery mechanism.
    Kubernetes gives Pods their own IP addresses and a single DNS name for a set of Pods, and can load-balance across them.

    For example, consider a stateless image-processing backend which is running with 3 replicas. Those replicas are fungible—frontends do not care which backend they use.
    While the actual Pods that compose the backend set may change, the frontend clients should not need to be aware of that,
    nor should they need to keep track of the set of backends themselves.
    The Service abstraction enables this decoupling.

    If you're able to use Kubernetes APIs for service discovery in your application, you can query the API server for Endpoints,
    that get updated whenever the set of Pods in a Service changes. For non-native applications, Kubernetes offers ways to place a network port
    or load balancer in between your application and the backend Pods.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        cluster_ip: typing.Optional[builtins.str] = None,
        external_i_ps: typing.Optional[typing.Sequence[builtins.str]] = None,
        external_name: typing.Optional[builtins.str] = None,
        load_balancer_source_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        ports: typing.Optional[typing.Sequence["ServicePort"]] = None,
        type: typing.Optional["ServiceType"] = None,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param cluster_ip: The IP address of the service and is usually assigned randomly by the master. If an address is specified manually and is not in use by others, it will be allocated to the service; otherwise, creation of the service will fail. This field can not be changed through updates. Valid values are "None", empty string (""), or a valid IP address. "None" can be specified for headless services when proxying is not required. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName. Default: - Automatically assigned.
        :param external_i_ps: A list of IP addresses for which nodes in the cluster will also accept traffic for this service. These IPs are not managed by Kubernetes. The user is responsible for ensuring that traffic arrives at a node with this IP. A common example is external load-balancers that are not part of the Kubernetes system. Default: - No external IPs.
        :param external_name: The externalName to be used when ServiceType.EXTERNAL_NAME is set. Default: - No external name.
        :param load_balancer_source_ranges: A list of CIDR IP addresses, if specified and supported by the platform, will restrict traffic through the cloud-provider load-balancer to the specified client IPs. More info: https://kubernetes.io/docs/tasks/access-application-cluster/configure-cloud-provider-firewall/
        :param ports: The port exposed by this service. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies
        :param type: Determines how the Service is exposed. More info: https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types Default: ServiceType.ClusterIP
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        props = ServiceProps(
            cluster_ip=cluster_ip,
            external_i_ps=external_i_ps,
            external_name=external_name,
            load_balancer_source_ranges=load_balancer_source_ranges,
            ports=ports,
            type=type,
            metadata=metadata,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addDeployment")
    def add_deployment(
        self,
        deployment: "Deployment",
        *,
        port: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        node_port: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[Protocol] = None,
        target_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Associate a deployment to this service.

        If not targetPort is specific in the portOptions, then requests will be routed
        to the port exposed by the first container in the deployment's pods.
        The deployment's ``labelSelector`` will be used to select pods.

        :param deployment: The deployment to expose.
        :param port: The port number the service will bind to. Default: - Copied from the first container of the deployment.
        :param name: The name of this port within the service. This must be a DNS_LABEL. All ports within a ServiceSpec must have unique names. This maps to the 'Name' field in EndpointPort objects. Optional if only one ServicePort is defined on this service.
        :param node_port: The port on each node on which this service is exposed when type=NodePort or LoadBalancer. Usually assigned by the system. If specified, it will be allocated to the service if unused or else creation of the service will fail. Default is to auto-allocate a port if the ServiceType of this Service requires one. Default: - auto-allocate a port if the ServiceType of this Service requires one.
        :param protocol: The IP protocol for this port. Supports "TCP", "UDP", and "SCTP". Default is TCP. Default: Protocol.TCP
        :param target_port: The port number the service will redirect to. Default: - The value of ``port`` will be used.
        '''
        options = AddDeploymentOptions(
            port=port,
            name=name,
            node_port=node_port,
            protocol=protocol,
            target_port=target_port,
        )

        return typing.cast(None, jsii.invoke(self, "addDeployment", [deployment, options]))

    @jsii.member(jsii_name="addSelector")
    def add_selector(self, label: builtins.str, value: builtins.str) -> None:
        '''Services defined using this spec will select pods according the provided label.

        :param label: The label key.
        :param value: The label value.
        '''
        return typing.cast(None, jsii.invoke(self, "addSelector", [label, value]))

    @jsii.member(jsii_name="exposeViaIngress")
    def expose_via_ingress(
        self,
        path: builtins.str,
        *,
        ingress: typing.Optional["IngressV1Beta1"] = None,
    ) -> "IngressV1Beta1":
        '''Expose a service via an ingress using the specified path.

        :param path: The path to expose the service under.
        :param ingress: The ingress to add rules to. Default: - An ingress will be automatically created.

        :return: The ``Ingress`` resource that was used.
        '''
        options = ExposeServiceViaIngressOptions(ingress=ingress)

        return typing.cast("IngressV1Beta1", jsii.invoke(self, "exposeViaIngress", [path, options]))

    @jsii.member(jsii_name="serve")
    def serve(
        self,
        port: jsii.Number,
        *,
        name: typing.Optional[builtins.str] = None,
        node_port: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[Protocol] = None,
        target_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Configure a port the service will bind to.

        This method can be called multiple times.

        :param port: The port definition.
        :param name: The name of this port within the service. This must be a DNS_LABEL. All ports within a ServiceSpec must have unique names. This maps to the 'Name' field in EndpointPort objects. Optional if only one ServicePort is defined on this service.
        :param node_port: The port on each node on which this service is exposed when type=NodePort or LoadBalancer. Usually assigned by the system. If specified, it will be allocated to the service if unused or else creation of the service will fail. Default is to auto-allocate a port if the ServiceType of this Service requires one. Default: - auto-allocate a port if the ServiceType of this Service requires one.
        :param protocol: The IP protocol for this port. Supports "TCP", "UDP", and "SCTP". Default is TCP. Default: Protocol.TCP
        :param target_port: The port number the service will redirect to. Default: - The value of ``port`` will be used.
        '''
        options = ServicePortOptions(
            name=name, node_port=node_port, protocol=protocol, target_port=target_port
        )

        return typing.cast(None, jsii.invoke(self, "serve", [port, options]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ports")
    def ports(self) -> typing.List["ServicePort"]:
        '''Ports for this service.

        Use ``serve()`` to expose additional service ports.
        '''
        return typing.cast(typing.List["ServicePort"], jsii.get(self, "ports"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="selector")
    def selector(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Returns the labels which are used to select pods for this service.'''
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "selector"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> "ServiceType":
        '''Determines how the Service is exposed.'''
        return typing.cast("ServiceType", jsii.get(self, "type"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clusterIP")
    def cluster_ip(self) -> typing.Optional[builtins.str]:
        '''The IP address of the service and is usually assigned randomly by the master.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIP"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="externalName")
    def external_name(self) -> typing.Optional[builtins.str]:
        '''The externalName to be used for EXTERNAL_NAME types.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalName"))


@jsii.implements(IServiceAccount)
class ServiceAccount(
    Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-21.ServiceAccount",
):
    '''A service account provides an identity for processes that run in a Pod.

    When you (a human) access the cluster (for example, using kubectl), you are
    authenticated by the apiserver as a particular User Account (currently this
    is usually admin, unless your cluster administrator has customized your
    cluster). Processes in containers inside pods can also contact the apiserver.
    When they do, they are authenticated as a particular Service Account (for
    example, default).

    :see: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        secrets: typing.Optional[typing.Sequence[ISecret]] = None,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param secrets: List of secrets allowed to be used by pods running using this ServiceAccount.
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        props = ServiceAccountProps(secrets=secrets, metadata=metadata)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromServiceAccountName") # type: ignore[misc]
    @builtins.classmethod
    def from_service_account_name(cls, name: builtins.str) -> IServiceAccount:
        '''Imports a service account from the cluster as a reference.

        :param name: The name of the service account resource.
        '''
        return typing.cast(IServiceAccount, jsii.sinvoke(cls, "fromServiceAccountName", [name]))

    @jsii.member(jsii_name="addSecret")
    def add_secret(self, secret: ISecret) -> None:
        '''Allow a secret to be accessed by pods using this service account.

        :param secret: The secret.
        '''
        return typing.cast(None, jsii.invoke(self, "addSecret", [secret]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="secrets")
    def secrets(self) -> typing.List[ISecret]:
        '''List of secrets allowed to be used by pods running using this service account.

        Returns a copy. To add a secret, use ``addSecret()``.
        '''
        return typing.cast(typing.List[ISecret], jsii.get(self, "secrets"))


@jsii.data_type(
    jsii_type="cdk8s-plus-21.ServiceAccountProps",
    jsii_struct_bases=[ResourceProps],
    name_mapping={"metadata": "metadata", "secrets": "secrets"},
)
class ServiceAccountProps(ResourceProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        secrets: typing.Optional[typing.Sequence[ISecret]] = None,
    ) -> None:
        '''Properties for initialization of ``ServiceAccount``.

        Properties for initialization of ``ServiceAccount``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param secrets: List of secrets allowed to be used by pods running using this ServiceAccount.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if secrets is not None:
            self._values["secrets"] = secrets

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def secrets(self) -> typing.Optional[typing.List[ISecret]]:
        '''List of secrets allowed to be used by pods running using this ServiceAccount.

        :see: https://kubernetes.io/docs/concepts/configuration/secret
        '''
        result = self._values.get("secrets")
        return typing.cast(typing.Optional[typing.List[ISecret]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceAccountProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceAccountTokenSecret(
    Secret,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-21.ServiceAccountTokenSecret",
):
    '''Create a secret for a service account token.

    :see: https://kubernetes.io/docs/concepts/configuration/secret/#service-account-token-secrets
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        service_account: IServiceAccount,
        immutable: typing.Optional[builtins.bool] = None,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param service_account: The service account to store a secret for.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        props = ServiceAccountTokenSecretProps(
            service_account=service_account, immutable=immutable, metadata=metadata
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="cdk8s-plus-21.ServiceIngressV1BetaBackendOptions",
    jsii_struct_bases=[],
    name_mapping={"port": "port"},
)
class ServiceIngressV1BetaBackendOptions:
    def __init__(self, *, port: typing.Optional[jsii.Number] = None) -> None:
        '''Options for setting up backends for ingress rules.

        :param port: The port to use to access the service. - This option will fail if the service does not expose any ports. - If the service exposes multiple ports, this option must be specified. - If the service exposes a single port, this option is optional and if specified, it must be the same port exposed by the service. Default: - if the service exposes a single port, this port will be used.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port to use to access the service.

        - This option will fail if the service does not expose any ports.
        - If the service exposes multiple ports, this option must be specified.
        - If the service exposes a single port, this option is optional and if
          specified, it must be the same port exposed by the service.

        :default: - if the service exposes a single port, this port will be used.
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceIngressV1BetaBackendOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.ServicePortOptions",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "node_port": "nodePort",
        "protocol": "protocol",
        "target_port": "targetPort",
    },
)
class ServicePortOptions:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        node_port: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[Protocol] = None,
        target_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: The name of this port within the service. This must be a DNS_LABEL. All ports within a ServiceSpec must have unique names. This maps to the 'Name' field in EndpointPort objects. Optional if only one ServicePort is defined on this service.
        :param node_port: The port on each node on which this service is exposed when type=NodePort or LoadBalancer. Usually assigned by the system. If specified, it will be allocated to the service if unused or else creation of the service will fail. Default is to auto-allocate a port if the ServiceType of this Service requires one. Default: - auto-allocate a port if the ServiceType of this Service requires one.
        :param protocol: The IP protocol for this port. Supports "TCP", "UDP", and "SCTP". Default is TCP. Default: Protocol.TCP
        :param target_port: The port number the service will redirect to. Default: - The value of ``port`` will be used.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if node_port is not None:
            self._values["node_port"] = node_port
        if protocol is not None:
            self._values["protocol"] = protocol
        if target_port is not None:
            self._values["target_port"] = target_port

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of this port within the service.

        This must be a DNS_LABEL. All
        ports within a ServiceSpec must have unique names. This maps to the 'Name'
        field in EndpointPort objects. Optional if only one ServicePort is defined
        on this service.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_port(self) -> typing.Optional[jsii.Number]:
        '''The port on each node on which this service is exposed when type=NodePort or LoadBalancer.

        Usually assigned by the system. If specified, it will be
        allocated to the service if unused or else creation of the service will
        fail. Default is to auto-allocate a port if the ServiceType of this Service
        requires one.

        :default: - auto-allocate a port if the ServiceType of this Service requires one.

        :see: https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport
        '''
        result = self._values.get("node_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def protocol(self) -> typing.Optional[Protocol]:
        '''The IP protocol for this port.

        Supports "TCP", "UDP", and "SCTP". Default is TCP.

        :default: Protocol.TCP
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[Protocol], result)

    @builtins.property
    def target_port(self) -> typing.Optional[jsii.Number]:
        '''The port number the service will redirect to.

        :default: - The value of ``port`` will be used.
        '''
        result = self._values.get("target_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServicePortOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.ServiceProps",
    jsii_struct_bases=[ResourceProps],
    name_mapping={
        "metadata": "metadata",
        "cluster_ip": "clusterIP",
        "external_i_ps": "externalIPs",
        "external_name": "externalName",
        "load_balancer_source_ranges": "loadBalancerSourceRanges",
        "ports": "ports",
        "type": "type",
    },
)
class ServiceProps(ResourceProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        cluster_ip: typing.Optional[builtins.str] = None,
        external_i_ps: typing.Optional[typing.Sequence[builtins.str]] = None,
        external_name: typing.Optional[builtins.str] = None,
        load_balancer_source_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        ports: typing.Optional[typing.Sequence["ServicePort"]] = None,
        type: typing.Optional["ServiceType"] = None,
    ) -> None:
        '''Properties for initialization of ``Service``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param cluster_ip: The IP address of the service and is usually assigned randomly by the master. If an address is specified manually and is not in use by others, it will be allocated to the service; otherwise, creation of the service will fail. This field can not be changed through updates. Valid values are "None", empty string (""), or a valid IP address. "None" can be specified for headless services when proxying is not required. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName. Default: - Automatically assigned.
        :param external_i_ps: A list of IP addresses for which nodes in the cluster will also accept traffic for this service. These IPs are not managed by Kubernetes. The user is responsible for ensuring that traffic arrives at a node with this IP. A common example is external load-balancers that are not part of the Kubernetes system. Default: - No external IPs.
        :param external_name: The externalName to be used when ServiceType.EXTERNAL_NAME is set. Default: - No external name.
        :param load_balancer_source_ranges: A list of CIDR IP addresses, if specified and supported by the platform, will restrict traffic through the cloud-provider load-balancer to the specified client IPs. More info: https://kubernetes.io/docs/tasks/access-application-cluster/configure-cloud-provider-firewall/
        :param ports: The port exposed by this service. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies
        :param type: Determines how the Service is exposed. More info: https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types Default: ServiceType.ClusterIP
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if cluster_ip is not None:
            self._values["cluster_ip"] = cluster_ip
        if external_i_ps is not None:
            self._values["external_i_ps"] = external_i_ps
        if external_name is not None:
            self._values["external_name"] = external_name
        if load_balancer_source_ranges is not None:
            self._values["load_balancer_source_ranges"] = load_balancer_source_ranges
        if ports is not None:
            self._values["ports"] = ports
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def cluster_ip(self) -> typing.Optional[builtins.str]:
        '''The IP address of the service and is usually assigned randomly by the master.

        If an address is specified manually and is not in use by others, it
        will be allocated to the service; otherwise, creation of the service will
        fail. This field can not be changed through updates. Valid values are
        "None", empty string (""), or a valid IP address. "None" can be specified
        for headless services when proxying is not required. Only applies to types
        ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName.

        :default: - Automatically assigned.

        :see: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies
        '''
        result = self._values.get("cluster_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_i_ps(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of IP addresses for which nodes in the cluster will also accept traffic for this service.

        These IPs are not managed by Kubernetes. The user
        is responsible for ensuring that traffic arrives at a node with this IP. A
        common example is external load-balancers that are not part of the
        Kubernetes system.

        :default: - No external IPs.
        '''
        result = self._values.get("external_i_ps")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def external_name(self) -> typing.Optional[builtins.str]:
        '''The externalName to be used when ServiceType.EXTERNAL_NAME is set.

        :default: - No external name.
        '''
        result = self._values.get("external_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_balancer_source_ranges(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of CIDR IP addresses, if specified and supported by the platform, will restrict traffic through the cloud-provider load-balancer to the specified client IPs.

        More info: https://kubernetes.io/docs/tasks/access-application-cluster/configure-cloud-provider-firewall/
        '''
        result = self._values.get("load_balancer_source_ranges")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.List["ServicePort"]]:
        '''The port exposed by this service.

        More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List["ServicePort"]], result)

    @builtins.property
    def type(self) -> typing.Optional["ServiceType"]:
        '''Determines how the Service is exposed.

        More info: https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types

        :default: ServiceType.ClusterIP
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["ServiceType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk8s-plus-21.ServiceType")
class ServiceType(enum.Enum):
    '''For some parts of your application (for example, frontends) you may want to expose a Service onto an external IP address, that's outside of your cluster.

    Kubernetes ServiceTypes allow you to specify what kind of Service you want.
    The default is ClusterIP.
    '''

    CLUSTER_IP = "CLUSTER_IP"
    '''Exposes the Service on a cluster-internal IP.

    Choosing this value makes the Service only reachable from within the cluster.
    This is the default ServiceType
    '''
    NODE_PORT = "NODE_PORT"
    '''Exposes the Service on each Node's IP at a static port (the NodePort).

    A ClusterIP Service, to which the NodePort Service routes, is automatically created.
    You'll be able to contact the NodePort Service, from outside the cluster,
    by requesting :.
    '''
    LOAD_BALANCER = "LOAD_BALANCER"
    '''Exposes the Service externally using a cloud provider's load balancer.

    NodePort and ClusterIP Services, to which the external load balancer routes,
    are automatically created.
    '''
    EXTERNAL_NAME = "EXTERNAL_NAME"
    '''Maps the Service to the contents of the externalName field (e.g. foo.bar.example.com), by returning a CNAME record with its value. No proxying of any kind is set up.

    .. epigraph::

       Note: You need either kube-dns version 1.7 or CoreDNS version 0.0.8 or higher to use the ExternalName type.
    '''


class SshAuthSecret(
    Secret,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-21.SshAuthSecret",
):
    '''Create a secret for ssh authentication.

    :see: https://kubernetes.io/docs/concepts/configuration/secret/#ssh-authentication-secrets
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        ssh_private_key: builtins.str,
        immutable: typing.Optional[builtins.bool] = None,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param ssh_private_key: The SSH private key to use.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        props = SshAuthSecretProps(
            ssh_private_key=ssh_private_key, immutable=immutable, metadata=metadata
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.implements(IPodTemplate)
class StatefulSet(
    Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-21.StatefulSet",
):
    '''StatefulSet is the workload API object used to manage stateful applications.

    Manages the deployment and scaling of a set of Pods, and provides guarantees
    about the ordering and uniqueness of these Pods.

    Like a Deployment, a StatefulSet manages Pods that are based on an identical
    container spec. Unlike a Deployment, a StatefulSet maintains a sticky identity
    for each of their Pods. These pods are created from the same spec, but are not
    interchangeable: each has a persistent identifier that it maintains across any
    rescheduling.

    If you want to use storage volumes to provide persistence for your workload, you
    can use a StatefulSet as part of the solution. Although individual Pods in a StatefulSet
    are susceptible to failure, the persistent Pod identifiers make it easier to match existing
    volumes to the new Pods that replace any that have failed.


    Using StatefulSets

    StatefulSets are valuable for applications that require one or more of the following.

    - Stable, unique network identifiers.
    - Stable, persistent storage.
    - Ordered, graceful deployment and scaling.
    - Ordered, automated rolling updates.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        service: Service,
        default_selector: typing.Optional[builtins.bool] = None,
        pod_management_policy: typing.Optional[PodManagementPolicy] = None,
        replicas: typing.Optional[jsii.Number] = None,
        strategy: typing.Optional["StatefulSetUpdateStrategy"] = None,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        pod_metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        docker_registry_auth: typing.Optional["DockerConfigSecret"] = None,
        host_aliases: typing.Optional[typing.Sequence[HostAlias]] = None,
        init_containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        restart_policy: typing.Optional[RestartPolicy] = None,
        security_context: typing.Optional[PodSecurityContextProps] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence["Volume"]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param service: Service to associate with the statefulset.
        :param default_selector: Automatically allocates a pod selector for this statefulset. If this is set to ``false`` you must define your selector through ``statefulset.podMetadata.addLabel()`` and ``statefulset.selectByLabel()``. Default: true
        :param pod_management_policy: Pod management policy to use for this statefulset. Default: PodManagementPolicy.ORDERED_READY
        :param replicas: Number of desired pods. Default: 1
        :param strategy: Indicates the StatefulSetUpdateStrategy that will be employed to update Pods in the StatefulSet when a revision is made to Template. Default: - RollingUpdate with partition set to 0
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param pod_metadata: The pod metadata.
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        '''
        props = StatefulSetProps(
            service=service,
            default_selector=default_selector,
            pod_management_policy=pod_management_policy,
            replicas=replicas,
            strategy=strategy,
            metadata=metadata,
            pod_metadata=pod_metadata,
            containers=containers,
            docker_registry_auth=docker_registry_auth,
            host_aliases=host_aliases,
            init_containers=init_containers,
            restart_policy=restart_policy,
            security_context=security_context,
            service_account=service_account,
            volumes=volumes,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addContainer")
    def add_container(
        self,
        *,
        image: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, EnvValue]] = None,
        image_pull_policy: typing.Optional[ImagePullPolicy] = None,
        lifecycle: typing.Optional[ContainerLifecycle] = None,
        liveness: typing.Optional[Probe] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        readiness: typing.Optional[Probe] = None,
        resources: typing.Optional[Resources] = None,
        security_context: typing.Optional[ContainerSecurityContextProps] = None,
        startup: typing.Optional[Probe] = None,
        volume_mounts: typing.Optional[typing.Sequence["VolumeMount"]] = None,
        working_dir: typing.Optional[builtins.str] = None,
    ) -> Container:
        '''Add a container to the pod.

        :param image: Docker image name.
        :param args: Arguments to the entrypoint. The docker image's CMD is used if ``command`` is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. Default: []
        :param command: Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell Default: - The docker image's ENTRYPOINT.
        :param env: List of environment variables to set in the container. Cannot be updated. Default: - No environment variables.
        :param image_pull_policy: Image pull policy for this container. Default: ImagePullPolicy.ALWAYS
        :param lifecycle: Describes actions that the management system should take in response to container lifecycle events.
        :param liveness: Periodic probe of container liveness. Container will be restarted if the probe fails. Default: - no liveness probe is defined
        :param name: Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. Default: 'main'
        :param port: Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. Default: - No port is exposed.
        :param readiness: Determines when the container is ready to serve traffic. Default: - no readiness probe is defined
        :param resources: Compute resources (CPU and memory requests and limits) required by the container.
        :param security_context: SecurityContext defines the security options the container should be run with. If set, the fields override equivalent fields of the pod's security context. Default: ensureNonRoot: false privileged: false readOnlyRootFilesystem: false
        :param startup: StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully Default: - no startup probe is defined.
        :param volume_mounts: Pod volumes to mount into the container's filesystem. Cannot be updated.
        :param working_dir: Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. Default: - The container runtime's default.
        '''
        container = ContainerProps(
            image=image,
            args=args,
            command=command,
            env=env,
            image_pull_policy=image_pull_policy,
            lifecycle=lifecycle,
            liveness=liveness,
            name=name,
            port=port,
            readiness=readiness,
            resources=resources,
            security_context=security_context,
            startup=startup,
            volume_mounts=volume_mounts,
            working_dir=working_dir,
        )

        return typing.cast(Container, jsii.invoke(self, "addContainer", [container]))

    @jsii.member(jsii_name="addHostAlias")
    def add_host_alias(
        self,
        *,
        hostnames: typing.Sequence[builtins.str],
        ip: builtins.str,
    ) -> None:
        '''
        :param hostnames: Hostnames for the chosen IP address.
        :param ip: IP address of the host file entry.
        '''
        host_alias = HostAlias(hostnames=hostnames, ip=ip)

        return typing.cast(None, jsii.invoke(self, "addHostAlias", [host_alias]))

    @jsii.member(jsii_name="addInitContainer")
    def add_init_container(
        self,
        *,
        image: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, EnvValue]] = None,
        image_pull_policy: typing.Optional[ImagePullPolicy] = None,
        lifecycle: typing.Optional[ContainerLifecycle] = None,
        liveness: typing.Optional[Probe] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        readiness: typing.Optional[Probe] = None,
        resources: typing.Optional[Resources] = None,
        security_context: typing.Optional[ContainerSecurityContextProps] = None,
        startup: typing.Optional[Probe] = None,
        volume_mounts: typing.Optional[typing.Sequence["VolumeMount"]] = None,
        working_dir: typing.Optional[builtins.str] = None,
    ) -> Container:
        '''Add an init container to the pod.

        :param image: Docker image name.
        :param args: Arguments to the entrypoint. The docker image's CMD is used if ``command`` is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. Default: []
        :param command: Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell Default: - The docker image's ENTRYPOINT.
        :param env: List of environment variables to set in the container. Cannot be updated. Default: - No environment variables.
        :param image_pull_policy: Image pull policy for this container. Default: ImagePullPolicy.ALWAYS
        :param lifecycle: Describes actions that the management system should take in response to container lifecycle events.
        :param liveness: Periodic probe of container liveness. Container will be restarted if the probe fails. Default: - no liveness probe is defined
        :param name: Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. Default: 'main'
        :param port: Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. Default: - No port is exposed.
        :param readiness: Determines when the container is ready to serve traffic. Default: - no readiness probe is defined
        :param resources: Compute resources (CPU and memory requests and limits) required by the container.
        :param security_context: SecurityContext defines the security options the container should be run with. If set, the fields override equivalent fields of the pod's security context. Default: ensureNonRoot: false privileged: false readOnlyRootFilesystem: false
        :param startup: StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully Default: - no startup probe is defined.
        :param volume_mounts: Pod volumes to mount into the container's filesystem. Cannot be updated.
        :param working_dir: Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. Default: - The container runtime's default.
        '''
        container = ContainerProps(
            image=image,
            args=args,
            command=command,
            env=env,
            image_pull_policy=image_pull_policy,
            lifecycle=lifecycle,
            liveness=liveness,
            name=name,
            port=port,
            readiness=readiness,
            resources=resources,
            security_context=security_context,
            startup=startup,
            volume_mounts=volume_mounts,
            working_dir=working_dir,
        )

        return typing.cast(Container, jsii.invoke(self, "addInitContainer", [container]))

    @jsii.member(jsii_name="addVolume")
    def add_volume(self, volume: "Volume") -> None:
        '''Add a volume to the pod.

        :param volume: -
        '''
        return typing.cast(None, jsii.invoke(self, "addVolume", [volume]))

    @jsii.member(jsii_name="selectByLabel")
    def select_by_label(self, key: builtins.str, value: builtins.str) -> None:
        '''Configure a label selector to this deployment.

        Pods that have the label will be selected by deployments configured with this spec.

        :param key: - The label key.
        :param value: - The label value.
        '''
        return typing.cast(None, jsii.invoke(self, "selectByLabel", [key, value]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="containers")
    def containers(self) -> typing.List[Container]:
        '''The containers belonging to the pod.

        Use ``addContainer`` to add containers.
        '''
        return typing.cast(typing.List[Container], jsii.get(self, "containers"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hostAliases")
    def host_aliases(self) -> typing.List[HostAlias]:
        '''An optional list of hosts and IPs that will be injected into the pod's hosts file if specified.

        This is only valid for non-hostNetwork pods.
        '''
        return typing.cast(typing.List[HostAlias], jsii.get(self, "hostAliases"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="initContainers")
    def init_containers(self) -> typing.List[Container]:
        '''The init containers belonging to the pod.

        Use ``addInitContainer`` to add init containers.
        '''
        return typing.cast(typing.List[Container], jsii.get(self, "initContainers"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="labelSelector")
    def label_selector(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''The labels this statefulset will match against in order to select pods.

        Returns a a copy. Use ``selectByLabel()`` to add labels.
        '''
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labelSelector"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="podManagementPolicy")
    def pod_management_policy(self) -> PodManagementPolicy:
        '''Management policy to use for the set.'''
        return typing.cast(PodManagementPolicy, jsii.get(self, "podManagementPolicy"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="podMetadata")
    def pod_metadata(self) -> cdk8s.ApiObjectMetadataDefinition:
        '''Provides read/write access to the underlying pod metadata of the resource.'''
        return typing.cast(cdk8s.ApiObjectMetadataDefinition, jsii.get(self, "podMetadata"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="replicas")
    def replicas(self) -> jsii.Number:
        '''Number of desired pods.'''
        return typing.cast(jsii.Number, jsii.get(self, "replicas"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityContext")
    def security_context(self) -> PodSecurityContext:
        return typing.cast(PodSecurityContext, jsii.get(self, "securityContext"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="strategy")
    def strategy(self) -> "StatefulSetUpdateStrategy":
        '''The update startegy of this stateful set.'''
        return typing.cast("StatefulSetUpdateStrategy", jsii.get(self, "strategy"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="volumes")
    def volumes(self) -> typing.List["Volume"]:
        '''The volumes associated with this pod.

        Use ``addVolume`` to add volumes.
        '''
        return typing.cast(typing.List["Volume"], jsii.get(self, "volumes"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="restartPolicy")
    def restart_policy(self) -> typing.Optional[RestartPolicy]:
        '''Restart policy for all containers within the pod.'''
        return typing.cast(typing.Optional[RestartPolicy], jsii.get(self, "restartPolicy"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> typing.Optional[IServiceAccount]:
        '''The service account used to run this pod.'''
        return typing.cast(typing.Optional[IServiceAccount], jsii.get(self, "serviceAccount"))


@jsii.data_type(
    jsii_type="cdk8s-plus-21.StatefulSetProps",
    jsii_struct_bases=[ResourceProps, PodTemplateProps],
    name_mapping={
        "metadata": "metadata",
        "containers": "containers",
        "docker_registry_auth": "dockerRegistryAuth",
        "host_aliases": "hostAliases",
        "init_containers": "initContainers",
        "restart_policy": "restartPolicy",
        "security_context": "securityContext",
        "service_account": "serviceAccount",
        "volumes": "volumes",
        "pod_metadata": "podMetadata",
        "service": "service",
        "default_selector": "defaultSelector",
        "pod_management_policy": "podManagementPolicy",
        "replicas": "replicas",
        "strategy": "strategy",
    },
)
class StatefulSetProps(ResourceProps, PodTemplateProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        docker_registry_auth: typing.Optional["DockerConfigSecret"] = None,
        host_aliases: typing.Optional[typing.Sequence[HostAlias]] = None,
        init_containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        restart_policy: typing.Optional[RestartPolicy] = None,
        security_context: typing.Optional[PodSecurityContextProps] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence["Volume"]] = None,
        pod_metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        service: Service,
        default_selector: typing.Optional[builtins.bool] = None,
        pod_management_policy: typing.Optional[PodManagementPolicy] = None,
        replicas: typing.Optional[jsii.Number] = None,
        strategy: typing.Optional["StatefulSetUpdateStrategy"] = None,
    ) -> None:
        '''Properties for initialization of ``StatefulSet``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        :param pod_metadata: The pod metadata.
        :param service: Service to associate with the statefulset.
        :param default_selector: Automatically allocates a pod selector for this statefulset. If this is set to ``false`` you must define your selector through ``statefulset.podMetadata.addLabel()`` and ``statefulset.selectByLabel()``. Default: true
        :param pod_management_policy: Pod management policy to use for this statefulset. Default: PodManagementPolicy.ORDERED_READY
        :param replicas: Number of desired pods. Default: 1
        :param strategy: Indicates the StatefulSetUpdateStrategy that will be employed to update Pods in the StatefulSet when a revision is made to Template. Default: - RollingUpdate with partition set to 0
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(security_context, dict):
            security_context = PodSecurityContextProps(**security_context)
        if isinstance(pod_metadata, dict):
            pod_metadata = cdk8s.ApiObjectMetadata(**pod_metadata)
        self._values: typing.Dict[str, typing.Any] = {
            "service": service,
        }
        if metadata is not None:
            self._values["metadata"] = metadata
        if containers is not None:
            self._values["containers"] = containers
        if docker_registry_auth is not None:
            self._values["docker_registry_auth"] = docker_registry_auth
        if host_aliases is not None:
            self._values["host_aliases"] = host_aliases
        if init_containers is not None:
            self._values["init_containers"] = init_containers
        if restart_policy is not None:
            self._values["restart_policy"] = restart_policy
        if security_context is not None:
            self._values["security_context"] = security_context
        if service_account is not None:
            self._values["service_account"] = service_account
        if volumes is not None:
            self._values["volumes"] = volumes
        if pod_metadata is not None:
            self._values["pod_metadata"] = pod_metadata
        if default_selector is not None:
            self._values["default_selector"] = default_selector
        if pod_management_policy is not None:
            self._values["pod_management_policy"] = pod_management_policy
        if replicas is not None:
            self._values["replicas"] = replicas
        if strategy is not None:
            self._values["strategy"] = strategy

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of containers belonging to the pod.

        Containers cannot currently be
        added or removed. There must be at least one container in a Pod.

        You can add additionnal containers using ``podSpec.addContainer()``

        :default: - No containers. Note that a pod spec must include at least one container.
        '''
        result = self._values.get("containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def docker_registry_auth(self) -> typing.Optional["DockerConfigSecret"]:
        '''A secret containing docker credentials for authenticating to a registry.

        :default: - No auth. Images are assumed to be publicly available.
        '''
        result = self._values.get("docker_registry_auth")
        return typing.cast(typing.Optional["DockerConfigSecret"], result)

    @builtins.property
    def host_aliases(self) -> typing.Optional[typing.List[HostAlias]]:
        '''HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.

        :schema: io.k8s.api.core.v1.HostAlias
        '''
        result = self._values.get("host_aliases")
        return typing.cast(typing.Optional[typing.List[HostAlias]], result)

    @builtins.property
    def init_containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of initialization containers belonging to the pod.

        Init containers are executed in order prior to containers being started.
        If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy.
        The name for an init container or normal container must be unique among all containers.
        Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes.
        The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit
        for each resource type, and then using the max of of that value or the sum of the normal containers.
        Limits are applied to init containers in a similar fashion.

        Init containers cannot currently be added ,removed or updated.

        :default: - No init containers.

        :see: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
        '''
        result = self._values.get("init_containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def restart_policy(self) -> typing.Optional[RestartPolicy]:
        '''Restart policy for all containers within the pod.

        :default: RestartPolicy.ALWAYS

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy
        '''
        result = self._values.get("restart_policy")
        return typing.cast(typing.Optional[RestartPolicy], result)

    @builtins.property
    def security_context(self) -> typing.Optional[PodSecurityContextProps]:
        '''SecurityContext holds pod-level security attributes and common container settings.

        :default:

        fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS
        ensureNonRoot: false
        '''
        result = self._values.get("security_context")
        return typing.cast(typing.Optional[PodSecurityContextProps], result)

    @builtins.property
    def service_account(self) -> typing.Optional[IServiceAccount]:
        '''A service account provides an identity for processes that run in a Pod.

        When you (a human) access the cluster (for example, using kubectl), you are
        authenticated by the apiserver as a particular User Account (currently this
        is usually admin, unless your cluster administrator has customized your
        cluster). Processes in containers inside pods can also contact the
        apiserver. When they do, they are authenticated as a particular Service
        Account (for example, default).

        :default: - No service account.

        :see: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[IServiceAccount], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List["Volume"]]:
        '''List of volumes that can be mounted by containers belonging to the pod.

        You can also add volumes later using ``podSpec.addVolume()``

        :default: - No volumes.

        :see: https://kubernetes.io/docs/concepts/storage/volumes
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List["Volume"]], result)

    @builtins.property
    def pod_metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''The pod metadata.'''
        result = self._values.get("pod_metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def service(self) -> Service:
        '''Service to associate with the statefulset.'''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(Service, result)

    @builtins.property
    def default_selector(self) -> typing.Optional[builtins.bool]:
        '''Automatically allocates a pod selector for this statefulset.

        If this is set to ``false`` you must define your selector through
        ``statefulset.podMetadata.addLabel()`` and ``statefulset.selectByLabel()``.

        :default: true
        '''
        result = self._values.get("default_selector")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def pod_management_policy(self) -> typing.Optional[PodManagementPolicy]:
        '''Pod management policy to use for this statefulset.

        :default: PodManagementPolicy.ORDERED_READY
        '''
        result = self._values.get("pod_management_policy")
        return typing.cast(typing.Optional[PodManagementPolicy], result)

    @builtins.property
    def replicas(self) -> typing.Optional[jsii.Number]:
        '''Number of desired pods.

        :default: 1
        '''
        result = self._values.get("replicas")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def strategy(self) -> typing.Optional["StatefulSetUpdateStrategy"]:
        '''Indicates the StatefulSetUpdateStrategy that will be employed to update Pods in the StatefulSet when a revision is made to Template.

        :default: - RollingUpdate with partition set to 0
        '''
        result = self._values.get("strategy")
        return typing.cast(typing.Optional["StatefulSetUpdateStrategy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StatefulSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StatefulSetUpdateStrategy(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-21.StatefulSetUpdateStrategy",
):
    '''StatefulSet update strategies.'''

    @jsii.member(jsii_name="onDelete") # type: ignore[misc]
    @builtins.classmethod
    def on_delete(cls) -> "StatefulSetUpdateStrategy":
        '''The controller will not automatically update the Pods in a StatefulSet.

        Users must manually delete Pods to cause the controller to create new Pods
        that reflect modifications.
        '''
        return typing.cast("StatefulSetUpdateStrategy", jsii.sinvoke(cls, "onDelete", []))

    @jsii.member(jsii_name="rollingUpdate") # type: ignore[misc]
    @builtins.classmethod
    def rolling_update(
        cls,
        *,
        partition: typing.Optional[jsii.Number] = None,
    ) -> "StatefulSetUpdateStrategy":
        '''The controller will delete and recreate each Pod in the StatefulSet.

        It will proceed in the same order as Pod termination (from the largest ordinal to the smallest),
        updating each Pod one at a time. The Kubernetes control plane waits until an updated
        Pod is Running and Ready prior to updating its predecessor.

        :param partition: If specified, all Pods with an ordinal that is greater than or equal to the partition will be updated when the StatefulSet's .spec.template is updated. All Pods with an ordinal that is less than the partition will not be updated, and, even if they are deleted, they will be recreated at the previous version. If the partition is greater than replicas, updates to the pod template will not be propagated to Pods. In most cases you will not need to use a partition, but they are useful if you want to stage an update, roll out a canary, or perform a phased roll out. Default: 0
        '''
        options = StatefulSetUpdateStrategyRollingUpdateOptions(partition=partition)

        return typing.cast("StatefulSetUpdateStrategy", jsii.sinvoke(cls, "rollingUpdate", [options]))


@jsii.data_type(
    jsii_type="cdk8s-plus-21.StatefulSetUpdateStrategyRollingUpdateOptions",
    jsii_struct_bases=[],
    name_mapping={"partition": "partition"},
)
class StatefulSetUpdateStrategyRollingUpdateOptions:
    def __init__(self, *, partition: typing.Optional[jsii.Number] = None) -> None:
        '''Options for ``StatefulSetUpdateStrategy.rollingUpdate``.

        :param partition: If specified, all Pods with an ordinal that is greater than or equal to the partition will be updated when the StatefulSet's .spec.template is updated. All Pods with an ordinal that is less than the partition will not be updated, and, even if they are deleted, they will be recreated at the previous version. If the partition is greater than replicas, updates to the pod template will not be propagated to Pods. In most cases you will not need to use a partition, but they are useful if you want to stage an update, roll out a canary, or perform a phased roll out. Default: 0
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if partition is not None:
            self._values["partition"] = partition

    @builtins.property
    def partition(self) -> typing.Optional[jsii.Number]:
        '''If specified, all Pods with an ordinal that is greater than or equal to the partition will be updated when the StatefulSet's .spec.template is updated. All Pods with an ordinal that is less than the partition will not be updated, and, even if they are deleted, they will be recreated at the previous version.

        If the partition is greater than replicas, updates to the pod template will not be propagated to Pods.
        In most cases you will not need to use a partition, but they are useful if you want to stage an
        update, roll out a canary, or perform a phased roll out.

        :default: 0

        :see: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#partitions
        '''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StatefulSetUpdateStrategyRollingUpdateOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.Sysctl",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class Sysctl:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''Sysctl defines a kernel parameter to be set.

        :param name: Name of a property to set.
        :param value: Value of a property to set.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of a property to set.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Value of a property to set.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Sysctl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.TcpSocketProbeOptions",
    jsii_struct_bases=[ProbeOptions],
    name_mapping={
        "failure_threshold": "failureThreshold",
        "initial_delay_seconds": "initialDelaySeconds",
        "period_seconds": "periodSeconds",
        "success_threshold": "successThreshold",
        "timeout_seconds": "timeoutSeconds",
        "host": "host",
        "port": "port",
    },
)
class TcpSocketProbeOptions(ProbeOptions):
    def __init__(
        self,
        *,
        failure_threshold: typing.Optional[jsii.Number] = None,
        initial_delay_seconds: typing.Optional[cdk8s.Duration] = None,
        period_seconds: typing.Optional[cdk8s.Duration] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[cdk8s.Duration] = None,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Options for ``Probe.fromTcpSocket()``.

        :param failure_threshold: Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. Default: 3
        :param initial_delay_seconds: Number of seconds after the container has started before liveness probes are initiated. Default: - immediate
        :param period_seconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. Default: Duration.seconds(10) Minimum value is 1.
        :param success_threshold: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. Default: 1 Must be 1 for liveness and startup. Minimum value is 1.
        :param timeout_seconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. Default: Duration.seconds(1)
        :param host: The host name to connect to on the container. Default: - defaults to the pod IP
        :param port: The TCP port to connect to on the container. Default: - defaults to ``container.port``.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if failure_threshold is not None:
            self._values["failure_threshold"] = failure_threshold
        if initial_delay_seconds is not None:
            self._values["initial_delay_seconds"] = initial_delay_seconds
        if period_seconds is not None:
            self._values["period_seconds"] = period_seconds
        if success_threshold is not None:
            self._values["success_threshold"] = success_threshold
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds
        if host is not None:
            self._values["host"] = host
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def failure_threshold(self) -> typing.Optional[jsii.Number]:
        '''Minimum consecutive failures for the probe to be considered failed after having succeeded.

        Defaults to 3. Minimum value is 1.

        :default: 3
        '''
        result = self._values.get("failure_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def initial_delay_seconds(self) -> typing.Optional[cdk8s.Duration]:
        '''Number of seconds after the container has started before liveness probes are initiated.

        :default: - immediate

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
        '''
        result = self._values.get("initial_delay_seconds")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def period_seconds(self) -> typing.Optional[cdk8s.Duration]:
        '''How often (in seconds) to perform the probe.

        Default to 10 seconds. Minimum value is 1.

        :default: Duration.seconds(10) Minimum value is 1.
        '''
        result = self._values.get("period_seconds")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def success_threshold(self) -> typing.Optional[jsii.Number]:
        '''Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1.

        Must be 1 for liveness and startup. Minimum value is 1.

        :default: 1 Must be 1 for liveness and startup. Minimum value is 1.
        '''
        result = self._values.get("success_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[cdk8s.Duration]:
        '''Number of seconds after which the probe times out.

        Defaults to 1 second. Minimum value is 1.

        :default: Duration.seconds(1)

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
        '''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''The host name to connect to on the container.

        :default: - defaults to the pod IP
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The TCP port to connect to on the container.

        :default: - defaults to ``container.port``.
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TcpSocketProbeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TlsSecret(Secret, metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-21.TlsSecret"):
    '''Create a secret for storing a TLS certificate and its associated key.

    :see: https://kubernetes.io/docs/concepts/configuration/secret/#tls-secrets
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        tls_cert: builtins.str,
        tls_key: builtins.str,
        immutable: typing.Optional[builtins.bool] = None,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param tls_cert: The TLS cert.
        :param tls_key: The TLS key.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        props = TlsSecretProps(
            tls_cert=tls_cert, tls_key=tls_key, immutable=immutable, metadata=metadata
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.implements(IStorage)
class Volume(metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-21.Volume"):
    '''Volume represents a named volume in a pod that may be accessed by any container in the pod.

    Docker also has a concept of volumes, though it is somewhat looser and less
    managed. In Docker, a volume is simply a directory on disk or in another
    Container. Lifetimes are not managed and until very recently there were only
    local-disk-backed volumes. Docker now provides volume drivers, but the
    functionality is very limited for now (e.g. as of Docker 1.7 only one volume
    driver is allowed per Container and there is no way to pass parameters to
    volumes).

    A Kubernetes volume, on the other hand, has an explicit lifetime - the same
    as the Pod that encloses it. Consequently, a volume outlives any Containers
    that run within the Pod, and data is preserved across Container restarts. Of
    course, when a Pod ceases to exist, the volume will cease to exist, too.
    Perhaps more importantly than this, Kubernetes supports many types of
    volumes, and a Pod can use any number of them simultaneously.

    At its core, a volume is just a directory, possibly with some data in it,
    which is accessible to the Containers in a Pod. How that directory comes to
    be, the medium that backs it, and the contents of it are determined by the
    particular volume type used.

    To use a volume, a Pod specifies what volumes to provide for the Pod (the
    .spec.volumes field) and where to mount those into Containers (the
    .spec.containers[*].volumeMounts field).

    A process in a container sees a filesystem view composed from their Docker
    image and volumes. The Docker image is at the root of the filesystem
    hierarchy, and any volumes are mounted at the specified paths within the
    image. Volumes can not mount onto other volumes
    '''

    @jsii.member(jsii_name="fromAwsElasticBlockStore") # type: ignore[misc]
    @builtins.classmethod
    def from_aws_elastic_block_store(
        cls,
        volume_id: builtins.str,
        *,
        fs_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[builtins.bool] = None,
    ) -> "Volume":
        '''Mounts an Amazon Web Services (AWS) EBS volume into your pod.

        Unlike emptyDir, which is erased when a pod is removed, the contents of an EBS volume are
        persisted and the volume is unmounted. This means that an EBS volume can be pre-populated with data,
        and that data can be shared between pods.

        There are some restrictions when using an awsElasticBlockStore volume:

        - the nodes on which pods are running must be AWS EC2 instances.
        - those instances need to be in the same region and availability zone as the EBS volume.
        - EBS only supports a single EC2 instance mounting a volume.

        :param volume_id: -
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Default: 'ext4'
        :param name: The volume name. Default: - auto-generated
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). Default: - No partition.
        :param read_only: Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". Default: false
        '''
        options = AwsElasticBlockStoreVolumeOptions(
            fs_type=fs_type, name=name, partition=partition, read_only=read_only
        )

        return typing.cast("Volume", jsii.sinvoke(cls, "fromAwsElasticBlockStore", [volume_id, options]))

    @jsii.member(jsii_name="fromAzureDisk") # type: ignore[misc]
    @builtins.classmethod
    def from_azure_disk(
        cls,
        disk_name: builtins.str,
        disk_uri: builtins.str,
        *,
        caching_mode: typing.Optional[AzureDiskPersistentVolumeCachingMode] = None,
        fs_type: typing.Optional[builtins.str] = None,
        kind: typing.Optional[AzureDiskPersistentVolumeKind] = None,
        name: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[builtins.bool] = None,
    ) -> "Volume":
        '''Mounts a Microsoft Azure Data Disk into a pod.

        :param disk_name: -
        :param disk_uri: -
        :param caching_mode: Host Caching mode. Default: - AzureDiskPersistentVolumeCachingMode.NONE.
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Default: 'ext4'
        :param kind: Kind of disk. Default: AzureDiskPersistentVolumeKind.SHARED
        :param name: The volume name. Default: - auto-generated
        :param read_only: Force the ReadOnly setting in VolumeMounts. Default: false
        '''
        options = AzureDiskVolumeOptions(
            caching_mode=caching_mode,
            fs_type=fs_type,
            kind=kind,
            name=name,
            read_only=read_only,
        )

        return typing.cast("Volume", jsii.sinvoke(cls, "fromAzureDisk", [disk_name, disk_uri, options]))

    @jsii.member(jsii_name="fromConfigMap") # type: ignore[misc]
    @builtins.classmethod
    def from_config_map(
        cls,
        config_map: "IConfigMap",
        *,
        default_mode: typing.Optional[jsii.Number] = None,
        items: typing.Optional[typing.Mapping[builtins.str, PathMapping]] = None,
        name: typing.Optional[builtins.str] = None,
        optional: typing.Optional[builtins.bool] = None,
    ) -> "Volume":
        '''Populate the volume from a ConfigMap.

        The configMap resource provides a way to inject configuration data into
        Pods. The data stored in a ConfigMap object can be referenced in a volume
        of type configMap and then consumed by containerized applications running
        in a Pod.

        When referencing a configMap object, you can simply provide its name in the
        volume to reference it. You can also customize the path to use for a
        specific entry in the ConfigMap.

        :param config_map: The config map to use to populate the volume.
        :param default_mode: Mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. Default: 644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
        :param items: If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. Default: - no mapping
        :param name: The volume name. Default: - auto-generated
        :param optional: Specify whether the ConfigMap or its keys must be defined. Default: - undocumented
        '''
        options = ConfigMapVolumeOptions(
            default_mode=default_mode, items=items, name=name, optional=optional
        )

        return typing.cast("Volume", jsii.sinvoke(cls, "fromConfigMap", [config_map, options]))

    @jsii.member(jsii_name="fromEmptyDir") # type: ignore[misc]
    @builtins.classmethod
    def from_empty_dir(
        cls,
        name: builtins.str,
        *,
        medium: typing.Optional[EmptyDirMedium] = None,
        size_limit: typing.Optional[cdk8s.Size] = None,
    ) -> "Volume":
        '''An emptyDir volume is first created when a Pod is assigned to a Node, and exists as long as that Pod is running on that node.

        As the name says, it is
        initially empty. Containers in the Pod can all read and write the same
        files in the emptyDir volume, though that volume can be mounted at the same
        or different paths in each Container. When a Pod is removed from a node for
        any reason, the data in the emptyDir is deleted forever.

        :param name: -
        :param medium: By default, emptyDir volumes are stored on whatever medium is backing the node - that might be disk or SSD or network storage, depending on your environment. However, you can set the emptyDir.medium field to ``EmptyDirMedium.MEMORY`` to tell Kubernetes to mount a tmpfs (RAM-backed filesystem) for you instead. While tmpfs is very fast, be aware that unlike disks, tmpfs is cleared on node reboot and any files you write will count against your Container's memory limit. Default: EmptyDirMedium.DEFAULT
        :param size_limit: Total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. Default: - limit is undefined

        :see: http://kubernetes.io/docs/user-guide/volumes#emptydir
        '''
        options = EmptyDirVolumeOptions(medium=medium, size_limit=size_limit)

        return typing.cast("Volume", jsii.sinvoke(cls, "fromEmptyDir", [name, options]))

    @jsii.member(jsii_name="fromGcePersistentDisk") # type: ignore[misc]
    @builtins.classmethod
    def from_gce_persistent_disk(
        cls,
        pd_name: builtins.str,
        *,
        fs_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[builtins.bool] = None,
    ) -> "Volume":
        '''Mounts a Google Compute Engine (GCE) persistent disk (PD) into your Pod.

        Unlike emptyDir, which is erased when a pod is removed, the contents of a PD are
        preserved and the volume is merely unmounted. This means that a PD can be pre-populated
        with data, and that data can be shared between pods.

        There are some restrictions when using a gcePersistentDisk:

        - the nodes on which Pods are running must be GCE VMs
        - those VMs need to be in the same GCE project and zone as the persistent disk

        :param pd_name: -
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Default: 'ext4'
        :param name: The volume name. Default: - auto-generated
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). Default: - No partition.
        :param read_only: Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". Default: false
        '''
        options = GCEPersistentDiskVolumeOptions(
            fs_type=fs_type, name=name, partition=partition, read_only=read_only
        )

        return typing.cast("Volume", jsii.sinvoke(cls, "fromGcePersistentDisk", [pd_name, options]))

    @jsii.member(jsii_name="fromPersistentVolumeClaim") # type: ignore[misc]
    @builtins.classmethod
    def from_persistent_volume_claim(
        cls,
        pvc: "IPersistentVolumeClaim",
        *,
        name: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[builtins.bool] = None,
    ) -> "Volume":
        '''Used to mount a PersistentVolume into a Pod.

        PersistentVolumeClaims are a way for users to "claim" durable storage (such as a GCE PersistentDisk or an iSCSI volume)
        without knowing the details of the particular cloud environment.

        :param pvc: -
        :param name: The volume name. Default: - Derived from the PVC name.
        :param read_only: Will force the ReadOnly setting in VolumeMounts. Default: false

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
        '''
        options = PersistentVolumeClaimVolumeOptions(name=name, read_only=read_only)

        return typing.cast("Volume", jsii.sinvoke(cls, "fromPersistentVolumeClaim", [pvc, options]))

    @jsii.member(jsii_name="fromSecret") # type: ignore[misc]
    @builtins.classmethod
    def from_secret(
        cls,
        secret: ISecret,
        *,
        default_mode: typing.Optional[jsii.Number] = None,
        items: typing.Optional[typing.Mapping[builtins.str, PathMapping]] = None,
        name: typing.Optional[builtins.str] = None,
        optional: typing.Optional[builtins.bool] = None,
    ) -> "Volume":
        '''Populate the volume from a Secret.

        A secret volume is used to pass sensitive information, such as passwords, to Pods.
        You can store secrets in the Kubernetes API and mount them as files for use by pods
        without coupling to Kubernetes directly.

        secret volumes are backed by tmpfs (a RAM-backed filesystem)
        so they are never written to non-volatile storage.

        :param secret: The secret to use to populate the volume.
        :param default_mode: Mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. Default: 644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
        :param items: If unspecified, each key-value pair in the Data field of the referenced secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. Default: - no mapping
        :param name: The volume name. Default: - auto-generated
        :param optional: Specify whether the secret or its keys must be defined. Default: - undocumented

        :see: https://kubernetes.io/docs/concepts/storage/volumes/#secret
        '''
        options = SecretVolumeOptions(
            default_mode=default_mode, items=items, name=name, optional=optional
        )

        return typing.cast("Volume", jsii.sinvoke(cls, "fromSecret", [secret, options]))

    @jsii.member(jsii_name="asVolume")
    def as_volume(self) -> "Volume":
        '''Convert the piece of storage into a concrete volume.'''
        return typing.cast("Volume", jsii.invoke(self, "asVolume", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))


@jsii.data_type(
    jsii_type="cdk8s-plus-21.VolumeMount",
    jsii_struct_bases=[MountOptions],
    name_mapping={
        "propagation": "propagation",
        "read_only": "readOnly",
        "sub_path": "subPath",
        "sub_path_expr": "subPathExpr",
        "path": "path",
        "volume": "volume",
    },
)
class VolumeMount(MountOptions):
    def __init__(
        self,
        *,
        propagation: typing.Optional[MountPropagation] = None,
        read_only: typing.Optional[builtins.bool] = None,
        sub_path: typing.Optional[builtins.str] = None,
        sub_path_expr: typing.Optional[builtins.str] = None,
        path: builtins.str,
        volume: Volume,
    ) -> None:
        '''Mount a volume from the pod to the container.

        :param propagation: Determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. Mount propagation allows for sharing volumes mounted by a Container to other Containers in the same Pod, or even to other Pods on the same node. Default: MountPropagation.NONE
        :param read_only: Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false. Default: false
        :param sub_path: Path within the volume from which the container's volume should be mounted.). Default: "" the volume's root
        :param sub_path_expr: Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to "" (volume's root). ``subPathExpr`` and ``subPath`` are mutually exclusive. Default: "" volume's root.
        :param path: Path within the container at which the volume should be mounted. Must not contain ':'.
        :param volume: The volume to mount.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
            "volume": volume,
        }
        if propagation is not None:
            self._values["propagation"] = propagation
        if read_only is not None:
            self._values["read_only"] = read_only
        if sub_path is not None:
            self._values["sub_path"] = sub_path
        if sub_path_expr is not None:
            self._values["sub_path_expr"] = sub_path_expr

    @builtins.property
    def propagation(self) -> typing.Optional[MountPropagation]:
        '''Determines how mounts are propagated from the host to container and the other way around.

        When not set, MountPropagationNone is used.

        Mount propagation allows for sharing volumes mounted by a Container to
        other Containers in the same Pod, or even to other Pods on the same node.

        :default: MountPropagation.NONE
        '''
        result = self._values.get("propagation")
        return typing.cast(typing.Optional[MountPropagation], result)

    @builtins.property
    def read_only(self) -> typing.Optional[builtins.bool]:
        '''Mounted read-only if true, read-write otherwise (false or unspecified).

        Defaults to false.

        :default: false
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def sub_path(self) -> typing.Optional[builtins.str]:
        '''Path within the volume from which the container's volume should be mounted.).

        :default: "" the volume's root
        '''
        result = self._values.get("sub_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sub_path_expr(self) -> typing.Optional[builtins.str]:
        '''Expanded path within the volume from which the container's volume should be mounted.

        Behaves similarly to SubPath but environment variable references
        $(VAR_NAME) are expanded using the container's environment. Defaults to ""
        (volume's root).

        ``subPathExpr`` and ``subPath`` are mutually exclusive.

        :default: "" volume's root.
        '''
        result = self._values.get("sub_path_expr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Path within the container at which the volume should be mounted.

        Must not
        contain ':'.
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def volume(self) -> Volume:
        '''The volume to mount.'''
        result = self._values.get("volume")
        assert result is not None, "Required property 'volume' is missing"
        return typing.cast(Volume, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeMount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.AddDeploymentOptions",
    jsii_struct_bases=[ServicePortOptions],
    name_mapping={
        "name": "name",
        "node_port": "nodePort",
        "protocol": "protocol",
        "target_port": "targetPort",
        "port": "port",
    },
)
class AddDeploymentOptions(ServicePortOptions):
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        node_port: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[Protocol] = None,
        target_port: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Options to add a deployment to a service.

        :param name: The name of this port within the service. This must be a DNS_LABEL. All ports within a ServiceSpec must have unique names. This maps to the 'Name' field in EndpointPort objects. Optional if only one ServicePort is defined on this service.
        :param node_port: The port on each node on which this service is exposed when type=NodePort or LoadBalancer. Usually assigned by the system. If specified, it will be allocated to the service if unused or else creation of the service will fail. Default is to auto-allocate a port if the ServiceType of this Service requires one. Default: - auto-allocate a port if the ServiceType of this Service requires one.
        :param protocol: The IP protocol for this port. Supports "TCP", "UDP", and "SCTP". Default is TCP. Default: Protocol.TCP
        :param target_port: The port number the service will redirect to. Default: - The value of ``port`` will be used.
        :param port: The port number the service will bind to. Default: - Copied from the first container of the deployment.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if node_port is not None:
            self._values["node_port"] = node_port
        if protocol is not None:
            self._values["protocol"] = protocol
        if target_port is not None:
            self._values["target_port"] = target_port
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of this port within the service.

        This must be a DNS_LABEL. All
        ports within a ServiceSpec must have unique names. This maps to the 'Name'
        field in EndpointPort objects. Optional if only one ServicePort is defined
        on this service.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_port(self) -> typing.Optional[jsii.Number]:
        '''The port on each node on which this service is exposed when type=NodePort or LoadBalancer.

        Usually assigned by the system. If specified, it will be
        allocated to the service if unused or else creation of the service will
        fail. Default is to auto-allocate a port if the ServiceType of this Service
        requires one.

        :default: - auto-allocate a port if the ServiceType of this Service requires one.

        :see: https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport
        '''
        result = self._values.get("node_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def protocol(self) -> typing.Optional[Protocol]:
        '''The IP protocol for this port.

        Supports "TCP", "UDP", and "SCTP". Default is TCP.

        :default: Protocol.TCP
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[Protocol], result)

    @builtins.property
    def target_port(self) -> typing.Optional[jsii.Number]:
        '''The port number the service will redirect to.

        :default: - The value of ``port`` will be used.
        '''
        result = self._values.get("target_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port number the service will bind to.

        :default: - Copied from the first container of the deployment.
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AddDeploymentOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BasicAuthSecret(
    Secret,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-21.BasicAuthSecret",
):
    '''Create a secret for basic authentication.

    :see: https://kubernetes.io/docs/concepts/configuration/secret/#basic-authentication-secret
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        password: builtins.str,
        username: builtins.str,
        immutable: typing.Optional[builtins.bool] = None,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param password: The password or token for authentication.
        :param username: The user name for authentication.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        props = BasicAuthSecretProps(
            password=password,
            username=username,
            immutable=immutable,
            metadata=metadata,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="cdk8s-plus-21.CommandProbeOptions",
    jsii_struct_bases=[ProbeOptions],
    name_mapping={
        "failure_threshold": "failureThreshold",
        "initial_delay_seconds": "initialDelaySeconds",
        "period_seconds": "periodSeconds",
        "success_threshold": "successThreshold",
        "timeout_seconds": "timeoutSeconds",
    },
)
class CommandProbeOptions(ProbeOptions):
    def __init__(
        self,
        *,
        failure_threshold: typing.Optional[jsii.Number] = None,
        initial_delay_seconds: typing.Optional[cdk8s.Duration] = None,
        period_seconds: typing.Optional[cdk8s.Duration] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[cdk8s.Duration] = None,
    ) -> None:
        '''Options for ``Probe.fromCommand()``.

        :param failure_threshold: Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. Default: 3
        :param initial_delay_seconds: Number of seconds after the container has started before liveness probes are initiated. Default: - immediate
        :param period_seconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. Default: Duration.seconds(10) Minimum value is 1.
        :param success_threshold: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. Default: 1 Must be 1 for liveness and startup. Minimum value is 1.
        :param timeout_seconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. Default: Duration.seconds(1)
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if failure_threshold is not None:
            self._values["failure_threshold"] = failure_threshold
        if initial_delay_seconds is not None:
            self._values["initial_delay_seconds"] = initial_delay_seconds
        if period_seconds is not None:
            self._values["period_seconds"] = period_seconds
        if success_threshold is not None:
            self._values["success_threshold"] = success_threshold
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def failure_threshold(self) -> typing.Optional[jsii.Number]:
        '''Minimum consecutive failures for the probe to be considered failed after having succeeded.

        Defaults to 3. Minimum value is 1.

        :default: 3
        '''
        result = self._values.get("failure_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def initial_delay_seconds(self) -> typing.Optional[cdk8s.Duration]:
        '''Number of seconds after the container has started before liveness probes are initiated.

        :default: - immediate

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
        '''
        result = self._values.get("initial_delay_seconds")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def period_seconds(self) -> typing.Optional[cdk8s.Duration]:
        '''How often (in seconds) to perform the probe.

        Default to 10 seconds. Minimum value is 1.

        :default: Duration.seconds(10) Minimum value is 1.
        '''
        result = self._values.get("period_seconds")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def success_threshold(self) -> typing.Optional[jsii.Number]:
        '''Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1.

        Must be 1 for liveness and startup. Minimum value is 1.

        :default: 1 Must be 1 for liveness and startup. Minimum value is 1.
        '''
        result = self._values.get("success_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[cdk8s.Duration]:
        '''Number of seconds after which the probe times out.

        Defaults to 1 second. Minimum value is 1.

        :default: Duration.seconds(1)

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
        '''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CommandProbeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.CommonSecretProps",
    jsii_struct_bases=[ResourceProps],
    name_mapping={"metadata": "metadata", "immutable": "immutable"},
)
class CommonSecretProps(ResourceProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        immutable: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Common properties for ``Secret``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if immutable is not None:
            self._values["immutable"] = immutable

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def immutable(self) -> typing.Optional[builtins.bool]:
        '''If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified).

        If not set to true, the field can be modified at any time.

        :default: false
        '''
        result = self._values.get("immutable")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CommonSecretProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.ConfigMapProps",
    jsii_struct_bases=[ResourceProps],
    name_mapping={
        "metadata": "metadata",
        "binary_data": "binaryData",
        "data": "data",
        "immutable": "immutable",
    },
)
class ConfigMapProps(ResourceProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        binary_data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        immutable: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties for initialization of ``ConfigMap``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param binary_data: BinaryData contains the binary data. Each key must consist of alphanumeric characters, '-', '_' or '.'. BinaryData can contain byte sequences that are not in the UTF-8 range. The keys stored in BinaryData must not overlap with the ones in the Data field, this is enforced during validation process. You can also add binary data using ``configMap.addBinaryData()``.
        :param data: Data contains the configuration data. Each key must consist of alphanumeric characters, '-', '_' or '.'. Values with non-UTF-8 byte sequences must use the BinaryData field. The keys stored in Data must not overlap with the keys in the BinaryData field, this is enforced during validation process. You can also add data using ``configMap.addData()``.
        :param immutable: If set to true, ensures that data stored in the ConfigMap cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if binary_data is not None:
            self._values["binary_data"] = binary_data
        if data is not None:
            self._values["data"] = data
        if immutable is not None:
            self._values["immutable"] = immutable

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def binary_data(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''BinaryData contains the binary data.

        Each key must consist of alphanumeric characters, '-', '_' or '.'.
        BinaryData can contain byte sequences that are not in the UTF-8 range. The
        keys stored in BinaryData must not overlap with the ones in the Data field,
        this is enforced during validation process.

        You can also add binary data using ``configMap.addBinaryData()``.
        '''
        result = self._values.get("binary_data")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def data(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Data contains the configuration data.

        Each key must consist of alphanumeric characters, '-', '_' or '.'. Values
        with non-UTF-8 byte sequences must use the BinaryData field. The keys
        stored in Data must not overlap with the keys in the BinaryData field, this
        is enforced during validation process.

        You can also add data using ``configMap.addData()``.
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def immutable(self) -> typing.Optional[builtins.bool]:
        '''If set to true, ensures that data stored in the ConfigMap cannot be updated (only object metadata can be modified).

        If not set to true, the field can be modified at any time.

        :default: false
        '''
        result = self._values.get("immutable")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigMapProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IPodTemplate)
class DaemonSet(Resource, metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-21.DaemonSet"):
    '''A DaemonSet ensures that all (or some) Nodes run a copy of a Pod.

    As nodes are added to the cluster, Pods are added to them.
    As nodes are removed from the cluster, those Pods are garbage collected.
    Deleting a DaemonSet will clean up the Pods it created.

    Some typical uses of a DaemonSet are:

    - running a cluster storage daemon on every node
    - running a logs collection daemon on every node
    - running a node monitoring daemon on every node

    In a simple case, one DaemonSet, covering all nodes, would be used for each type of daemon.
    A more complex setup might use multiple DaemonSets for a single type of daemon,
    but with different flags and/or different memory and cpu requests for different hardware types.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        default_selector: typing.Optional[builtins.bool] = None,
        min_ready_seconds: typing.Optional[jsii.Number] = None,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        pod_metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        docker_registry_auth: typing.Optional["DockerConfigSecret"] = None,
        host_aliases: typing.Optional[typing.Sequence[HostAlias]] = None,
        init_containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        restart_policy: typing.Optional[RestartPolicy] = None,
        security_context: typing.Optional[PodSecurityContextProps] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence[Volume]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param default_selector: Automatically allocates a pod selector for this daemon set. If this is set to ``false`` you must define your selector through ``dset.podMetadata.addLabel()`` and ``dset.selectByLabel()``. Default: true
        :param min_ready_seconds: Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Default: 0
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param pod_metadata: The pod metadata.
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        '''
        props = DaemonSetProps(
            default_selector=default_selector,
            min_ready_seconds=min_ready_seconds,
            metadata=metadata,
            pod_metadata=pod_metadata,
            containers=containers,
            docker_registry_auth=docker_registry_auth,
            host_aliases=host_aliases,
            init_containers=init_containers,
            restart_policy=restart_policy,
            security_context=security_context,
            service_account=service_account,
            volumes=volumes,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addContainer")
    def add_container(
        self,
        *,
        image: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, EnvValue]] = None,
        image_pull_policy: typing.Optional[ImagePullPolicy] = None,
        lifecycle: typing.Optional[ContainerLifecycle] = None,
        liveness: typing.Optional[Probe] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        readiness: typing.Optional[Probe] = None,
        resources: typing.Optional[Resources] = None,
        security_context: typing.Optional[ContainerSecurityContextProps] = None,
        startup: typing.Optional[Probe] = None,
        volume_mounts: typing.Optional[typing.Sequence[VolumeMount]] = None,
        working_dir: typing.Optional[builtins.str] = None,
    ) -> Container:
        '''Add a container to the pod.

        :param image: Docker image name.
        :param args: Arguments to the entrypoint. The docker image's CMD is used if ``command`` is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. Default: []
        :param command: Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell Default: - The docker image's ENTRYPOINT.
        :param env: List of environment variables to set in the container. Cannot be updated. Default: - No environment variables.
        :param image_pull_policy: Image pull policy for this container. Default: ImagePullPolicy.ALWAYS
        :param lifecycle: Describes actions that the management system should take in response to container lifecycle events.
        :param liveness: Periodic probe of container liveness. Container will be restarted if the probe fails. Default: - no liveness probe is defined
        :param name: Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. Default: 'main'
        :param port: Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. Default: - No port is exposed.
        :param readiness: Determines when the container is ready to serve traffic. Default: - no readiness probe is defined
        :param resources: Compute resources (CPU and memory requests and limits) required by the container.
        :param security_context: SecurityContext defines the security options the container should be run with. If set, the fields override equivalent fields of the pod's security context. Default: ensureNonRoot: false privileged: false readOnlyRootFilesystem: false
        :param startup: StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully Default: - no startup probe is defined.
        :param volume_mounts: Pod volumes to mount into the container's filesystem. Cannot be updated.
        :param working_dir: Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. Default: - The container runtime's default.
        '''
        container = ContainerProps(
            image=image,
            args=args,
            command=command,
            env=env,
            image_pull_policy=image_pull_policy,
            lifecycle=lifecycle,
            liveness=liveness,
            name=name,
            port=port,
            readiness=readiness,
            resources=resources,
            security_context=security_context,
            startup=startup,
            volume_mounts=volume_mounts,
            working_dir=working_dir,
        )

        return typing.cast(Container, jsii.invoke(self, "addContainer", [container]))

    @jsii.member(jsii_name="addHostAlias")
    def add_host_alias(
        self,
        *,
        hostnames: typing.Sequence[builtins.str],
        ip: builtins.str,
    ) -> None:
        '''
        :param hostnames: Hostnames for the chosen IP address.
        :param ip: IP address of the host file entry.
        '''
        host_alias = HostAlias(hostnames=hostnames, ip=ip)

        return typing.cast(None, jsii.invoke(self, "addHostAlias", [host_alias]))

    @jsii.member(jsii_name="addInitContainer")
    def add_init_container(
        self,
        *,
        image: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, EnvValue]] = None,
        image_pull_policy: typing.Optional[ImagePullPolicy] = None,
        lifecycle: typing.Optional[ContainerLifecycle] = None,
        liveness: typing.Optional[Probe] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        readiness: typing.Optional[Probe] = None,
        resources: typing.Optional[Resources] = None,
        security_context: typing.Optional[ContainerSecurityContextProps] = None,
        startup: typing.Optional[Probe] = None,
        volume_mounts: typing.Optional[typing.Sequence[VolumeMount]] = None,
        working_dir: typing.Optional[builtins.str] = None,
    ) -> Container:
        '''Add an init container to the pod.

        :param image: Docker image name.
        :param args: Arguments to the entrypoint. The docker image's CMD is used if ``command`` is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. Default: []
        :param command: Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell Default: - The docker image's ENTRYPOINT.
        :param env: List of environment variables to set in the container. Cannot be updated. Default: - No environment variables.
        :param image_pull_policy: Image pull policy for this container. Default: ImagePullPolicy.ALWAYS
        :param lifecycle: Describes actions that the management system should take in response to container lifecycle events.
        :param liveness: Periodic probe of container liveness. Container will be restarted if the probe fails. Default: - no liveness probe is defined
        :param name: Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. Default: 'main'
        :param port: Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. Default: - No port is exposed.
        :param readiness: Determines when the container is ready to serve traffic. Default: - no readiness probe is defined
        :param resources: Compute resources (CPU and memory requests and limits) required by the container.
        :param security_context: SecurityContext defines the security options the container should be run with. If set, the fields override equivalent fields of the pod's security context. Default: ensureNonRoot: false privileged: false readOnlyRootFilesystem: false
        :param startup: StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully Default: - no startup probe is defined.
        :param volume_mounts: Pod volumes to mount into the container's filesystem. Cannot be updated.
        :param working_dir: Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. Default: - The container runtime's default.
        '''
        container = ContainerProps(
            image=image,
            args=args,
            command=command,
            env=env,
            image_pull_policy=image_pull_policy,
            lifecycle=lifecycle,
            liveness=liveness,
            name=name,
            port=port,
            readiness=readiness,
            resources=resources,
            security_context=security_context,
            startup=startup,
            volume_mounts=volume_mounts,
            working_dir=working_dir,
        )

        return typing.cast(Container, jsii.invoke(self, "addInitContainer", [container]))

    @jsii.member(jsii_name="addVolume")
    def add_volume(self, volume: Volume) -> None:
        '''Add a volume to the pod.

        :param volume: -
        '''
        return typing.cast(None, jsii.invoke(self, "addVolume", [volume]))

    @jsii.member(jsii_name="selectByLabel")
    def select_by_label(self, key: builtins.str, value: builtins.str) -> None:
        '''Configure a label selector to this daemon set.

        :param key: -
        :param value: -
        '''
        return typing.cast(None, jsii.invoke(self, "selectByLabel", [key, value]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="containers")
    def containers(self) -> typing.List[Container]:
        '''The containers belonging to the pod.

        Use ``addContainer`` to add containers.
        '''
        return typing.cast(typing.List[Container], jsii.get(self, "containers"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hostAliases")
    def host_aliases(self) -> typing.List[HostAlias]:
        '''An optional list of hosts and IPs that will be injected into the pod's hosts file if specified.

        This is only valid for non-hostNetwork pods.
        '''
        return typing.cast(typing.List[HostAlias], jsii.get(self, "hostAliases"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="initContainers")
    def init_containers(self) -> typing.List[Container]:
        '''The init containers belonging to the pod.

        Use ``addInitContainer`` to add init containers.
        '''
        return typing.cast(typing.List[Container], jsii.get(self, "initContainers"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="labelSelector")
    def label_selector(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''The labels this daemon set will match against in order to select pods.

        Returns a a copy. Use ``selectByLabel()`` to add labels.
        '''
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labelSelector"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="minReadySeconds")
    def min_ready_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minReadySeconds"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="podMetadata")
    def pod_metadata(self) -> cdk8s.ApiObjectMetadataDefinition:
        '''Provides read/write access to the underlying pod metadata of the resource.'''
        return typing.cast(cdk8s.ApiObjectMetadataDefinition, jsii.get(self, "podMetadata"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityContext")
    def security_context(self) -> PodSecurityContext:
        return typing.cast(PodSecurityContext, jsii.get(self, "securityContext"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="volumes")
    def volumes(self) -> typing.List[Volume]:
        '''The volumes associated with this pod.

        Use ``addVolume`` to add volumes.
        '''
        return typing.cast(typing.List[Volume], jsii.get(self, "volumes"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="restartPolicy")
    def restart_policy(self) -> typing.Optional[RestartPolicy]:
        '''Restart policy for all containers within the pod.'''
        return typing.cast(typing.Optional[RestartPolicy], jsii.get(self, "restartPolicy"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> typing.Optional[IServiceAccount]:
        '''The service account used to run this pod.'''
        return typing.cast(typing.Optional[IServiceAccount], jsii.get(self, "serviceAccount"))


@jsii.data_type(
    jsii_type="cdk8s-plus-21.DaemonSetProps",
    jsii_struct_bases=[ResourceProps, PodTemplateProps],
    name_mapping={
        "metadata": "metadata",
        "containers": "containers",
        "docker_registry_auth": "dockerRegistryAuth",
        "host_aliases": "hostAliases",
        "init_containers": "initContainers",
        "restart_policy": "restartPolicy",
        "security_context": "securityContext",
        "service_account": "serviceAccount",
        "volumes": "volumes",
        "pod_metadata": "podMetadata",
        "default_selector": "defaultSelector",
        "min_ready_seconds": "minReadySeconds",
    },
)
class DaemonSetProps(ResourceProps, PodTemplateProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        docker_registry_auth: typing.Optional["DockerConfigSecret"] = None,
        host_aliases: typing.Optional[typing.Sequence[HostAlias]] = None,
        init_containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        restart_policy: typing.Optional[RestartPolicy] = None,
        security_context: typing.Optional[PodSecurityContextProps] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence[Volume]] = None,
        pod_metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        default_selector: typing.Optional[builtins.bool] = None,
        min_ready_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for ``DaemonSet``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        :param pod_metadata: The pod metadata.
        :param default_selector: Automatically allocates a pod selector for this daemon set. If this is set to ``false`` you must define your selector through ``dset.podMetadata.addLabel()`` and ``dset.selectByLabel()``. Default: true
        :param min_ready_seconds: Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Default: 0
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(security_context, dict):
            security_context = PodSecurityContextProps(**security_context)
        if isinstance(pod_metadata, dict):
            pod_metadata = cdk8s.ApiObjectMetadata(**pod_metadata)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if containers is not None:
            self._values["containers"] = containers
        if docker_registry_auth is not None:
            self._values["docker_registry_auth"] = docker_registry_auth
        if host_aliases is not None:
            self._values["host_aliases"] = host_aliases
        if init_containers is not None:
            self._values["init_containers"] = init_containers
        if restart_policy is not None:
            self._values["restart_policy"] = restart_policy
        if security_context is not None:
            self._values["security_context"] = security_context
        if service_account is not None:
            self._values["service_account"] = service_account
        if volumes is not None:
            self._values["volumes"] = volumes
        if pod_metadata is not None:
            self._values["pod_metadata"] = pod_metadata
        if default_selector is not None:
            self._values["default_selector"] = default_selector
        if min_ready_seconds is not None:
            self._values["min_ready_seconds"] = min_ready_seconds

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of containers belonging to the pod.

        Containers cannot currently be
        added or removed. There must be at least one container in a Pod.

        You can add additionnal containers using ``podSpec.addContainer()``

        :default: - No containers. Note that a pod spec must include at least one container.
        '''
        result = self._values.get("containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def docker_registry_auth(self) -> typing.Optional["DockerConfigSecret"]:
        '''A secret containing docker credentials for authenticating to a registry.

        :default: - No auth. Images are assumed to be publicly available.
        '''
        result = self._values.get("docker_registry_auth")
        return typing.cast(typing.Optional["DockerConfigSecret"], result)

    @builtins.property
    def host_aliases(self) -> typing.Optional[typing.List[HostAlias]]:
        '''HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.

        :schema: io.k8s.api.core.v1.HostAlias
        '''
        result = self._values.get("host_aliases")
        return typing.cast(typing.Optional[typing.List[HostAlias]], result)

    @builtins.property
    def init_containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of initialization containers belonging to the pod.

        Init containers are executed in order prior to containers being started.
        If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy.
        The name for an init container or normal container must be unique among all containers.
        Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes.
        The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit
        for each resource type, and then using the max of of that value or the sum of the normal containers.
        Limits are applied to init containers in a similar fashion.

        Init containers cannot currently be added ,removed or updated.

        :default: - No init containers.

        :see: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
        '''
        result = self._values.get("init_containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def restart_policy(self) -> typing.Optional[RestartPolicy]:
        '''Restart policy for all containers within the pod.

        :default: RestartPolicy.ALWAYS

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy
        '''
        result = self._values.get("restart_policy")
        return typing.cast(typing.Optional[RestartPolicy], result)

    @builtins.property
    def security_context(self) -> typing.Optional[PodSecurityContextProps]:
        '''SecurityContext holds pod-level security attributes and common container settings.

        :default:

        fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS
        ensureNonRoot: false
        '''
        result = self._values.get("security_context")
        return typing.cast(typing.Optional[PodSecurityContextProps], result)

    @builtins.property
    def service_account(self) -> typing.Optional[IServiceAccount]:
        '''A service account provides an identity for processes that run in a Pod.

        When you (a human) access the cluster (for example, using kubectl), you are
        authenticated by the apiserver as a particular User Account (currently this
        is usually admin, unless your cluster administrator has customized your
        cluster). Processes in containers inside pods can also contact the
        apiserver. When they do, they are authenticated as a particular Service
        Account (for example, default).

        :default: - No service account.

        :see: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[IServiceAccount], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List[Volume]]:
        '''List of volumes that can be mounted by containers belonging to the pod.

        You can also add volumes later using ``podSpec.addVolume()``

        :default: - No volumes.

        :see: https://kubernetes.io/docs/concepts/storage/volumes
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List[Volume]], result)

    @builtins.property
    def pod_metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''The pod metadata.'''
        result = self._values.get("pod_metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def default_selector(self) -> typing.Optional[builtins.bool]:
        '''Automatically allocates a pod selector for this daemon set.

        If this is set to ``false`` you must define your selector through
        ``dset.podMetadata.addLabel()`` and ``dset.selectByLabel()``.

        :default: true
        '''
        result = self._values.get("default_selector")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def min_ready_seconds(self) -> typing.Optional[jsii.Number]:
        '''Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available.

        :default: 0
        '''
        result = self._values.get("min_ready_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DaemonSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IPodTemplate)
class Deployment(
    Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-21.Deployment",
):
    '''A Deployment provides declarative updates for Pods and ReplicaSets.

    You describe a desired state in a Deployment, and the Deployment Controller changes the actual
    state to the desired state at a controlled rate. You can define Deployments to create new ReplicaSets, or to remove
    existing Deployments and adopt all their resources with new Deployments.
    .. epigraph::

       Note: Do not manage ReplicaSets owned by a Deployment. Consider opening an issue in the main Kubernetes repository if your use case is not covered below.


    Use Case

    The following are typical use cases for Deployments:

    - Create a Deployment to rollout a ReplicaSet. The ReplicaSet creates Pods in the background.
      Check the status of the rollout to see if it succeeds or not.
    - Declare the new state of the Pods by updating the PodTemplateSpec of the Deployment.
      A new ReplicaSet is created and the Deployment manages moving the Pods from the old ReplicaSet to the new one at a controlled rate.
      Each new ReplicaSet updates the revision of the Deployment.
    - Rollback to an earlier Deployment revision if the current state of the Deployment is not stable.
      Each rollback updates the revision of the Deployment.
    - Scale up the Deployment to facilitate more load.
    - Pause the Deployment to apply multiple fixes to its PodTemplateSpec and then resume it to start a new rollout.
    - Use the status of the Deployment as an indicator that a rollout has stuck.
    - Clean up older ReplicaSets that you don't need anymore.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        default_selector: typing.Optional[builtins.bool] = None,
        replicas: typing.Optional[jsii.Number] = None,
        strategy: typing.Optional[DeploymentStrategy] = None,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        pod_metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        docker_registry_auth: typing.Optional["DockerConfigSecret"] = None,
        host_aliases: typing.Optional[typing.Sequence[HostAlias]] = None,
        init_containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        restart_policy: typing.Optional[RestartPolicy] = None,
        security_context: typing.Optional[PodSecurityContextProps] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence[Volume]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param default_selector: Automatically allocates a pod selector for this deployment. If this is set to ``false`` you must define your selector through ``deployment.podMetadata.addLabel()`` and ``deployment.selectByLabel()``. Default: true
        :param replicas: Number of desired pods. Default: 1
        :param strategy: Specifies the strategy used to replace old Pods by new ones. Default: - RollingUpdate with maxSurge and maxUnavailable set to 25%.
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param pod_metadata: The pod metadata.
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        '''
        props = DeploymentProps(
            default_selector=default_selector,
            replicas=replicas,
            strategy=strategy,
            metadata=metadata,
            pod_metadata=pod_metadata,
            containers=containers,
            docker_registry_auth=docker_registry_auth,
            host_aliases=host_aliases,
            init_containers=init_containers,
            restart_policy=restart_policy,
            security_context=security_context,
            service_account=service_account,
            volumes=volumes,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addContainer")
    def add_container(
        self,
        *,
        image: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, EnvValue]] = None,
        image_pull_policy: typing.Optional[ImagePullPolicy] = None,
        lifecycle: typing.Optional[ContainerLifecycle] = None,
        liveness: typing.Optional[Probe] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        readiness: typing.Optional[Probe] = None,
        resources: typing.Optional[Resources] = None,
        security_context: typing.Optional[ContainerSecurityContextProps] = None,
        startup: typing.Optional[Probe] = None,
        volume_mounts: typing.Optional[typing.Sequence[VolumeMount]] = None,
        working_dir: typing.Optional[builtins.str] = None,
    ) -> Container:
        '''Add a container to the pod.

        :param image: Docker image name.
        :param args: Arguments to the entrypoint. The docker image's CMD is used if ``command`` is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. Default: []
        :param command: Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell Default: - The docker image's ENTRYPOINT.
        :param env: List of environment variables to set in the container. Cannot be updated. Default: - No environment variables.
        :param image_pull_policy: Image pull policy for this container. Default: ImagePullPolicy.ALWAYS
        :param lifecycle: Describes actions that the management system should take in response to container lifecycle events.
        :param liveness: Periodic probe of container liveness. Container will be restarted if the probe fails. Default: - no liveness probe is defined
        :param name: Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. Default: 'main'
        :param port: Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. Default: - No port is exposed.
        :param readiness: Determines when the container is ready to serve traffic. Default: - no readiness probe is defined
        :param resources: Compute resources (CPU and memory requests and limits) required by the container.
        :param security_context: SecurityContext defines the security options the container should be run with. If set, the fields override equivalent fields of the pod's security context. Default: ensureNonRoot: false privileged: false readOnlyRootFilesystem: false
        :param startup: StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully Default: - no startup probe is defined.
        :param volume_mounts: Pod volumes to mount into the container's filesystem. Cannot be updated.
        :param working_dir: Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. Default: - The container runtime's default.
        '''
        container = ContainerProps(
            image=image,
            args=args,
            command=command,
            env=env,
            image_pull_policy=image_pull_policy,
            lifecycle=lifecycle,
            liveness=liveness,
            name=name,
            port=port,
            readiness=readiness,
            resources=resources,
            security_context=security_context,
            startup=startup,
            volume_mounts=volume_mounts,
            working_dir=working_dir,
        )

        return typing.cast(Container, jsii.invoke(self, "addContainer", [container]))

    @jsii.member(jsii_name="addHostAlias")
    def add_host_alias(
        self,
        *,
        hostnames: typing.Sequence[builtins.str],
        ip: builtins.str,
    ) -> None:
        '''
        :param hostnames: Hostnames for the chosen IP address.
        :param ip: IP address of the host file entry.
        '''
        host_alias = HostAlias(hostnames=hostnames, ip=ip)

        return typing.cast(None, jsii.invoke(self, "addHostAlias", [host_alias]))

    @jsii.member(jsii_name="addInitContainer")
    def add_init_container(
        self,
        *,
        image: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, EnvValue]] = None,
        image_pull_policy: typing.Optional[ImagePullPolicy] = None,
        lifecycle: typing.Optional[ContainerLifecycle] = None,
        liveness: typing.Optional[Probe] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        readiness: typing.Optional[Probe] = None,
        resources: typing.Optional[Resources] = None,
        security_context: typing.Optional[ContainerSecurityContextProps] = None,
        startup: typing.Optional[Probe] = None,
        volume_mounts: typing.Optional[typing.Sequence[VolumeMount]] = None,
        working_dir: typing.Optional[builtins.str] = None,
    ) -> Container:
        '''Add an init container to the pod.

        :param image: Docker image name.
        :param args: Arguments to the entrypoint. The docker image's CMD is used if ``command`` is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. Default: []
        :param command: Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell Default: - The docker image's ENTRYPOINT.
        :param env: List of environment variables to set in the container. Cannot be updated. Default: - No environment variables.
        :param image_pull_policy: Image pull policy for this container. Default: ImagePullPolicy.ALWAYS
        :param lifecycle: Describes actions that the management system should take in response to container lifecycle events.
        :param liveness: Periodic probe of container liveness. Container will be restarted if the probe fails. Default: - no liveness probe is defined
        :param name: Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. Default: 'main'
        :param port: Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. Default: - No port is exposed.
        :param readiness: Determines when the container is ready to serve traffic. Default: - no readiness probe is defined
        :param resources: Compute resources (CPU and memory requests and limits) required by the container.
        :param security_context: SecurityContext defines the security options the container should be run with. If set, the fields override equivalent fields of the pod's security context. Default: ensureNonRoot: false privileged: false readOnlyRootFilesystem: false
        :param startup: StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully Default: - no startup probe is defined.
        :param volume_mounts: Pod volumes to mount into the container's filesystem. Cannot be updated.
        :param working_dir: Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. Default: - The container runtime's default.
        '''
        container = ContainerProps(
            image=image,
            args=args,
            command=command,
            env=env,
            image_pull_policy=image_pull_policy,
            lifecycle=lifecycle,
            liveness=liveness,
            name=name,
            port=port,
            readiness=readiness,
            resources=resources,
            security_context=security_context,
            startup=startup,
            volume_mounts=volume_mounts,
            working_dir=working_dir,
        )

        return typing.cast(Container, jsii.invoke(self, "addInitContainer", [container]))

    @jsii.member(jsii_name="addVolume")
    def add_volume(self, volume: Volume) -> None:
        '''Add a volume to the pod.

        :param volume: -
        '''
        return typing.cast(None, jsii.invoke(self, "addVolume", [volume]))

    @jsii.member(jsii_name="exposeViaIngress")
    def expose_via_ingress(
        self,
        path: builtins.str,
        *,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[Protocol] = None,
        service_type: typing.Optional[ServiceType] = None,
        target_port: typing.Optional[jsii.Number] = None,
        ingress: typing.Optional["IngressV1Beta1"] = None,
    ) -> "IngressV1Beta1":
        '''Expose a deployment via an ingress.

        This will first expose the deployment with a service, and then expose the service via an ingress.

        :param path: The ingress path to register under.
        :param name: The name of the service to expose. This will be set on the Service.metadata and must be a DNS_LABEL Default: undefined Uses the system generated name.
        :param port: The port that the service should serve on. Default: - Copied from the container of the deployment. If a port could not be determined, throws an error.
        :param protocol: The IP protocol for this port. Supports "TCP", "UDP", and "SCTP". Default is TCP. Default: Protocol.TCP
        :param service_type: The type of the exposed service. Default: - ClusterIP.
        :param target_port: The port number the service will redirect to. Default: - The port of the first container in the deployment (ie. containers[0].port)
        :param ingress: The ingress to add rules to. Default: - An ingress will be automatically created.
        '''
        options = ExposeDeploymentViaIngressOptions(
            name=name,
            port=port,
            protocol=protocol,
            service_type=service_type,
            target_port=target_port,
            ingress=ingress,
        )

        return typing.cast("IngressV1Beta1", jsii.invoke(self, "exposeViaIngress", [path, options]))

    @jsii.member(jsii_name="exposeViaService")
    def expose_via_service(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[Protocol] = None,
        service_type: typing.Optional[ServiceType] = None,
        target_port: typing.Optional[jsii.Number] = None,
    ) -> Service:
        '''Expose a deployment via a service.

        This is equivalent to running ``kubectl expose deployment <deployment-name>``.

        :param name: The name of the service to expose. This will be set on the Service.metadata and must be a DNS_LABEL Default: undefined Uses the system generated name.
        :param port: The port that the service should serve on. Default: - Copied from the container of the deployment. If a port could not be determined, throws an error.
        :param protocol: The IP protocol for this port. Supports "TCP", "UDP", and "SCTP". Default is TCP. Default: Protocol.TCP
        :param service_type: The type of the exposed service. Default: - ClusterIP.
        :param target_port: The port number the service will redirect to. Default: - The port of the first container in the deployment (ie. containers[0].port)
        '''
        options = ExposeDeploymentViaServiceOptions(
            name=name,
            port=port,
            protocol=protocol,
            service_type=service_type,
            target_port=target_port,
        )

        return typing.cast(Service, jsii.invoke(self, "exposeViaService", [options]))

    @jsii.member(jsii_name="selectByLabel")
    def select_by_label(self, key: builtins.str, value: builtins.str) -> None:
        '''Configure a label selector to this deployment.

        Pods that have the label will be selected by deployments configured with this spec.

        :param key: - The label key.
        :param value: - The label value.
        '''
        return typing.cast(None, jsii.invoke(self, "selectByLabel", [key, value]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="containers")
    def containers(self) -> typing.List[Container]:
        '''The containers belonging to the pod.

        Use ``addContainer`` to add containers.
        '''
        return typing.cast(typing.List[Container], jsii.get(self, "containers"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hostAliases")
    def host_aliases(self) -> typing.List[HostAlias]:
        '''An optional list of hosts and IPs that will be injected into the pod's hosts file if specified.

        This is only valid for non-hostNetwork pods.
        '''
        return typing.cast(typing.List[HostAlias], jsii.get(self, "hostAliases"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="initContainers")
    def init_containers(self) -> typing.List[Container]:
        '''The init containers belonging to the pod.

        Use ``addInitContainer`` to add init containers.
        '''
        return typing.cast(typing.List[Container], jsii.get(self, "initContainers"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="labelSelector")
    def label_selector(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''The labels this deployment will match against in order to select pods.

        Returns a a copy. Use ``selectByLabel()`` to add labels.
        '''
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labelSelector"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="podMetadata")
    def pod_metadata(self) -> cdk8s.ApiObjectMetadataDefinition:
        '''Provides read/write access to the underlying pod metadata of the resource.'''
        return typing.cast(cdk8s.ApiObjectMetadataDefinition, jsii.get(self, "podMetadata"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="replicas")
    def replicas(self) -> jsii.Number:
        '''Number of desired pods.'''
        return typing.cast(jsii.Number, jsii.get(self, "replicas"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityContext")
    def security_context(self) -> PodSecurityContext:
        return typing.cast(PodSecurityContext, jsii.get(self, "securityContext"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="strategy")
    def strategy(self) -> DeploymentStrategy:
        '''The upgrade strategy of this deployment.'''
        return typing.cast(DeploymentStrategy, jsii.get(self, "strategy"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="volumes")
    def volumes(self) -> typing.List[Volume]:
        '''The volumes associated with this pod.

        Use ``addVolume`` to add volumes.
        '''
        return typing.cast(typing.List[Volume], jsii.get(self, "volumes"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="restartPolicy")
    def restart_policy(self) -> typing.Optional[RestartPolicy]:
        '''Restart policy for all containers within the pod.'''
        return typing.cast(typing.Optional[RestartPolicy], jsii.get(self, "restartPolicy"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> typing.Optional[IServiceAccount]:
        '''The service account used to run this pod.'''
        return typing.cast(typing.Optional[IServiceAccount], jsii.get(self, "serviceAccount"))


@jsii.data_type(
    jsii_type="cdk8s-plus-21.DeploymentProps",
    jsii_struct_bases=[ResourceProps, PodTemplateProps],
    name_mapping={
        "metadata": "metadata",
        "containers": "containers",
        "docker_registry_auth": "dockerRegistryAuth",
        "host_aliases": "hostAliases",
        "init_containers": "initContainers",
        "restart_policy": "restartPolicy",
        "security_context": "securityContext",
        "service_account": "serviceAccount",
        "volumes": "volumes",
        "pod_metadata": "podMetadata",
        "default_selector": "defaultSelector",
        "replicas": "replicas",
        "strategy": "strategy",
    },
)
class DeploymentProps(ResourceProps, PodTemplateProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        docker_registry_auth: typing.Optional["DockerConfigSecret"] = None,
        host_aliases: typing.Optional[typing.Sequence[HostAlias]] = None,
        init_containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        restart_policy: typing.Optional[RestartPolicy] = None,
        security_context: typing.Optional[PodSecurityContextProps] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence[Volume]] = None,
        pod_metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        default_selector: typing.Optional[builtins.bool] = None,
        replicas: typing.Optional[jsii.Number] = None,
        strategy: typing.Optional[DeploymentStrategy] = None,
    ) -> None:
        '''Properties for initialization of ``Deployment``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        :param pod_metadata: The pod metadata.
        :param default_selector: Automatically allocates a pod selector for this deployment. If this is set to ``false`` you must define your selector through ``deployment.podMetadata.addLabel()`` and ``deployment.selectByLabel()``. Default: true
        :param replicas: Number of desired pods. Default: 1
        :param strategy: Specifies the strategy used to replace old Pods by new ones. Default: - RollingUpdate with maxSurge and maxUnavailable set to 25%.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(security_context, dict):
            security_context = PodSecurityContextProps(**security_context)
        if isinstance(pod_metadata, dict):
            pod_metadata = cdk8s.ApiObjectMetadata(**pod_metadata)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if containers is not None:
            self._values["containers"] = containers
        if docker_registry_auth is not None:
            self._values["docker_registry_auth"] = docker_registry_auth
        if host_aliases is not None:
            self._values["host_aliases"] = host_aliases
        if init_containers is not None:
            self._values["init_containers"] = init_containers
        if restart_policy is not None:
            self._values["restart_policy"] = restart_policy
        if security_context is not None:
            self._values["security_context"] = security_context
        if service_account is not None:
            self._values["service_account"] = service_account
        if volumes is not None:
            self._values["volumes"] = volumes
        if pod_metadata is not None:
            self._values["pod_metadata"] = pod_metadata
        if default_selector is not None:
            self._values["default_selector"] = default_selector
        if replicas is not None:
            self._values["replicas"] = replicas
        if strategy is not None:
            self._values["strategy"] = strategy

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of containers belonging to the pod.

        Containers cannot currently be
        added or removed. There must be at least one container in a Pod.

        You can add additionnal containers using ``podSpec.addContainer()``

        :default: - No containers. Note that a pod spec must include at least one container.
        '''
        result = self._values.get("containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def docker_registry_auth(self) -> typing.Optional["DockerConfigSecret"]:
        '''A secret containing docker credentials for authenticating to a registry.

        :default: - No auth. Images are assumed to be publicly available.
        '''
        result = self._values.get("docker_registry_auth")
        return typing.cast(typing.Optional["DockerConfigSecret"], result)

    @builtins.property
    def host_aliases(self) -> typing.Optional[typing.List[HostAlias]]:
        '''HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.

        :schema: io.k8s.api.core.v1.HostAlias
        '''
        result = self._values.get("host_aliases")
        return typing.cast(typing.Optional[typing.List[HostAlias]], result)

    @builtins.property
    def init_containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of initialization containers belonging to the pod.

        Init containers are executed in order prior to containers being started.
        If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy.
        The name for an init container or normal container must be unique among all containers.
        Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes.
        The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit
        for each resource type, and then using the max of of that value or the sum of the normal containers.
        Limits are applied to init containers in a similar fashion.

        Init containers cannot currently be added ,removed or updated.

        :default: - No init containers.

        :see: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
        '''
        result = self._values.get("init_containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def restart_policy(self) -> typing.Optional[RestartPolicy]:
        '''Restart policy for all containers within the pod.

        :default: RestartPolicy.ALWAYS

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy
        '''
        result = self._values.get("restart_policy")
        return typing.cast(typing.Optional[RestartPolicy], result)

    @builtins.property
    def security_context(self) -> typing.Optional[PodSecurityContextProps]:
        '''SecurityContext holds pod-level security attributes and common container settings.

        :default:

        fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS
        ensureNonRoot: false
        '''
        result = self._values.get("security_context")
        return typing.cast(typing.Optional[PodSecurityContextProps], result)

    @builtins.property
    def service_account(self) -> typing.Optional[IServiceAccount]:
        '''A service account provides an identity for processes that run in a Pod.

        When you (a human) access the cluster (for example, using kubectl), you are
        authenticated by the apiserver as a particular User Account (currently this
        is usually admin, unless your cluster administrator has customized your
        cluster). Processes in containers inside pods can also contact the
        apiserver. When they do, they are authenticated as a particular Service
        Account (for example, default).

        :default: - No service account.

        :see: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[IServiceAccount], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List[Volume]]:
        '''List of volumes that can be mounted by containers belonging to the pod.

        You can also add volumes later using ``podSpec.addVolume()``

        :default: - No volumes.

        :see: https://kubernetes.io/docs/concepts/storage/volumes
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List[Volume]], result)

    @builtins.property
    def pod_metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''The pod metadata.'''
        result = self._values.get("pod_metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def default_selector(self) -> typing.Optional[builtins.bool]:
        '''Automatically allocates a pod selector for this deployment.

        If this is set to ``false`` you must define your selector through
        ``deployment.podMetadata.addLabel()`` and ``deployment.selectByLabel()``.

        :default: true
        '''
        result = self._values.get("default_selector")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def replicas(self) -> typing.Optional[jsii.Number]:
        '''Number of desired pods.

        :default: 1
        '''
        result = self._values.get("replicas")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def strategy(self) -> typing.Optional[DeploymentStrategy]:
        '''Specifies the strategy used to replace old Pods by new ones.

        :default: - RollingUpdate with maxSurge and maxUnavailable set to 25%.
        '''
        result = self._values.get("strategy")
        return typing.cast(typing.Optional[DeploymentStrategy], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeploymentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DockerConfigSecret(
    Secret,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-21.DockerConfigSecret",
):
    '''Create a secret for storing credentials for accessing a container image registry.

    :see: https://kubernetes.io/docs/concepts/configuration/secret/#docker-config-secrets
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        data: typing.Mapping[builtins.str, typing.Any],
        immutable: typing.Optional[builtins.bool] = None,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param data: JSON content to provide for the ``~/.docker/config.json`` file. This will be stringified and inserted as stringData.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        props = DockerConfigSecretProps(
            data=data, immutable=immutable, metadata=metadata
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="cdk8s-plus-21.DockerConfigSecretProps",
    jsii_struct_bases=[CommonSecretProps],
    name_mapping={"metadata": "metadata", "immutable": "immutable", "data": "data"},
)
class DockerConfigSecretProps(CommonSecretProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        immutable: typing.Optional[builtins.bool] = None,
        data: typing.Mapping[builtins.str, typing.Any],
    ) -> None:
        '''Options for ``DockerConfigSecret``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param data: JSON content to provide for the ``~/.docker/config.json`` file. This will be stringified and inserted as stringData.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        self._values: typing.Dict[str, typing.Any] = {
            "data": data,
        }
        if metadata is not None:
            self._values["metadata"] = metadata
        if immutable is not None:
            self._values["immutable"] = immutable

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def immutable(self) -> typing.Optional[builtins.bool]:
        '''If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified).

        If not set to true, the field can be modified at any time.

        :default: false
        '''
        result = self._values.get("immutable")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def data(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''JSON content to provide for the ``~/.docker/config.json`` file. This will be stringified and inserted as stringData.

        :see: https://docs.docker.com/engine/reference/commandline/cli/#sample-configuration-file
        '''
        result = self._values.get("data")
        assert result is not None, "Required property 'data' is missing"
        return typing.cast(typing.Mapping[builtins.str, typing.Any], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DockerConfigSecretProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.ExposeDeploymentViaIngressOptions",
    jsii_struct_bases=[
        ExposeDeploymentViaServiceOptions, ExposeServiceViaIngressOptions
    ],
    name_mapping={
        "name": "name",
        "port": "port",
        "protocol": "protocol",
        "service_type": "serviceType",
        "target_port": "targetPort",
        "ingress": "ingress",
    },
)
class ExposeDeploymentViaIngressOptions(
    ExposeDeploymentViaServiceOptions,
    ExposeServiceViaIngressOptions,
):
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[Protocol] = None,
        service_type: typing.Optional[ServiceType] = None,
        target_port: typing.Optional[jsii.Number] = None,
        ingress: typing.Optional["IngressV1Beta1"] = None,
    ) -> None:
        '''Options for exposing a deployment via an ingress.

        :param name: The name of the service to expose. This will be set on the Service.metadata and must be a DNS_LABEL Default: undefined Uses the system generated name.
        :param port: The port that the service should serve on. Default: - Copied from the container of the deployment. If a port could not be determined, throws an error.
        :param protocol: The IP protocol for this port. Supports "TCP", "UDP", and "SCTP". Default is TCP. Default: Protocol.TCP
        :param service_type: The type of the exposed service. Default: - ClusterIP.
        :param target_port: The port number the service will redirect to. Default: - The port of the first container in the deployment (ie. containers[0].port)
        :param ingress: The ingress to add rules to. Default: - An ingress will be automatically created.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if port is not None:
            self._values["port"] = port
        if protocol is not None:
            self._values["protocol"] = protocol
        if service_type is not None:
            self._values["service_type"] = service_type
        if target_port is not None:
            self._values["target_port"] = target_port
        if ingress is not None:
            self._values["ingress"] = ingress

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the service to expose.

        This will be set on the Service.metadata and must be a DNS_LABEL

        :default: undefined Uses the system generated name.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port that the service should serve on.

        :default: - Copied from the container of the deployment. If a port could not be determined, throws an error.
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def protocol(self) -> typing.Optional[Protocol]:
        '''The IP protocol for this port.

        Supports "TCP", "UDP", and "SCTP". Default is TCP.

        :default: Protocol.TCP
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[Protocol], result)

    @builtins.property
    def service_type(self) -> typing.Optional[ServiceType]:
        '''The type of the exposed service.

        :default: - ClusterIP.
        '''
        result = self._values.get("service_type")
        return typing.cast(typing.Optional[ServiceType], result)

    @builtins.property
    def target_port(self) -> typing.Optional[jsii.Number]:
        '''The port number the service will redirect to.

        :default: - The port of the first container in the deployment (ie. containers[0].port)
        '''
        result = self._values.get("target_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ingress(self) -> typing.Optional["IngressV1Beta1"]:
        '''The ingress to add rules to.

        :default: - An ingress will be automatically created.
        '''
        result = self._values.get("ingress")
        return typing.cast(typing.Optional["IngressV1Beta1"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExposeDeploymentViaIngressOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.HttpGetProbeOptions",
    jsii_struct_bases=[ProbeOptions],
    name_mapping={
        "failure_threshold": "failureThreshold",
        "initial_delay_seconds": "initialDelaySeconds",
        "period_seconds": "periodSeconds",
        "success_threshold": "successThreshold",
        "timeout_seconds": "timeoutSeconds",
        "port": "port",
    },
)
class HttpGetProbeOptions(ProbeOptions):
    def __init__(
        self,
        *,
        failure_threshold: typing.Optional[jsii.Number] = None,
        initial_delay_seconds: typing.Optional[cdk8s.Duration] = None,
        period_seconds: typing.Optional[cdk8s.Duration] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[cdk8s.Duration] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Options for ``Probe.fromHttpGet()``.

        :param failure_threshold: Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. Default: 3
        :param initial_delay_seconds: Number of seconds after the container has started before liveness probes are initiated. Default: - immediate
        :param period_seconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. Default: Duration.seconds(10) Minimum value is 1.
        :param success_threshold: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. Default: 1 Must be 1 for liveness and startup. Minimum value is 1.
        :param timeout_seconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. Default: Duration.seconds(1)
        :param port: The TCP port to use when sending the GET request. Default: - defaults to ``container.port``.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if failure_threshold is not None:
            self._values["failure_threshold"] = failure_threshold
        if initial_delay_seconds is not None:
            self._values["initial_delay_seconds"] = initial_delay_seconds
        if period_seconds is not None:
            self._values["period_seconds"] = period_seconds
        if success_threshold is not None:
            self._values["success_threshold"] = success_threshold
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def failure_threshold(self) -> typing.Optional[jsii.Number]:
        '''Minimum consecutive failures for the probe to be considered failed after having succeeded.

        Defaults to 3. Minimum value is 1.

        :default: 3
        '''
        result = self._values.get("failure_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def initial_delay_seconds(self) -> typing.Optional[cdk8s.Duration]:
        '''Number of seconds after the container has started before liveness probes are initiated.

        :default: - immediate

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
        '''
        result = self._values.get("initial_delay_seconds")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def period_seconds(self) -> typing.Optional[cdk8s.Duration]:
        '''How often (in seconds) to perform the probe.

        Default to 10 seconds. Minimum value is 1.

        :default: Duration.seconds(10) Minimum value is 1.
        '''
        result = self._values.get("period_seconds")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def success_threshold(self) -> typing.Optional[jsii.Number]:
        '''Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1.

        Must be 1 for liveness and startup. Minimum value is 1.

        :default: 1 Must be 1 for liveness and startup. Minimum value is 1.
        '''
        result = self._values.get("success_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[cdk8s.Duration]:
        '''Number of seconds after which the probe times out.

        Defaults to 1 second. Minimum value is 1.

        :default: Duration.seconds(1)

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
        '''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The TCP port to use when sending the GET request.

        :default: - defaults to ``container.port``.
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpGetProbeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="cdk8s-plus-21.IConfigMap")
class IConfigMap(IResource, typing_extensions.Protocol):
    '''Represents a config map.'''

    pass


class _IConfigMapProxy(
    jsii.proxy_for(IResource) # type: ignore[misc]
):
    '''Represents a config map.'''

    __jsii_type__: typing.ClassVar[str] = "cdk8s-plus-21.IConfigMap"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConfigMap).__jsii_proxy_class__ = lambda : _IConfigMapProxy


@jsii.interface(jsii_type="cdk8s-plus-21.IPersistentVolume")
class IPersistentVolume(IResource, typing_extensions.Protocol):
    '''Contract of a ``PersistentVolumeClaim``.'''

    pass


class _IPersistentVolumeProxy(
    jsii.proxy_for(IResource) # type: ignore[misc]
):
    '''Contract of a ``PersistentVolumeClaim``.'''

    __jsii_type__: typing.ClassVar[str] = "cdk8s-plus-21.IPersistentVolume"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPersistentVolume).__jsii_proxy_class__ = lambda : _IPersistentVolumeProxy


@jsii.interface(jsii_type="cdk8s-plus-21.IPersistentVolumeClaim")
class IPersistentVolumeClaim(IResource, typing_extensions.Protocol):
    '''Contract of a ``PersistentVolumeClaim``.'''

    pass


class _IPersistentVolumeClaimProxy(
    jsii.proxy_for(IResource) # type: ignore[misc]
):
    '''Contract of a ``PersistentVolumeClaim``.'''

    __jsii_type__: typing.ClassVar[str] = "cdk8s-plus-21.IPersistentVolumeClaim"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPersistentVolumeClaim).__jsii_proxy_class__ = lambda : _IPersistentVolumeClaimProxy


class IngressV1Beta1(
    Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-21.IngressV1Beta1",
):
    '''Ingress is a collection of rules that allow inbound connections to reach the endpoints defined by a backend.

    An Ingress can be configured to give services
    externally-reachable urls, load balance traffic, terminate SSL, offer name
    based virtual hosting etc.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        default_backend: typing.Optional[IngressV1Beta1Backend] = None,
        rules: typing.Optional[typing.Sequence[IngressV1Beta1Rule]] = None,
        tls: typing.Optional[typing.Sequence[IngressV1Beta1Tls]] = None,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param default_backend: The default backend services requests that do not match any rule. Using this option or the ``addDefaultBackend()`` method is equivalent to adding a rule with both ``path`` and ``host`` undefined.
        :param rules: Routing rules for this ingress. Each rule must define an ``IngressBackend`` that will receive the requests that match this rule. If both ``host`` and ``path`` are not specifiec, this backend will be used as the default backend of the ingress. You can also add rules later using ``addRule()``, ``addHostRule()``, ``addDefaultBackend()`` and ``addHostDefaultBackend()``.
        :param tls: TLS settings for this ingress. Using this option tells the ingress controller to expose a TLS endpoint. Currently the Ingress only supports a single TLS port, 443. If multiple members of this list specify different hosts, they will be multiplexed on the same port according to the hostname specified through the SNI TLS extension, if the ingress controller fulfilling the ingress supports SNI.
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        props = IngressV1Beta1Props(
            default_backend=default_backend, rules=rules, tls=tls, metadata=metadata
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addDefaultBackend")
    def add_default_backend(self, backend: IngressV1Beta1Backend) -> None:
        '''Defines the default backend for this ingress.

        A default backend capable of
        servicing requests that don't match any rule.

        :param backend: The backend to use for requests that do not match any rule.
        '''
        return typing.cast(None, jsii.invoke(self, "addDefaultBackend", [backend]))

    @jsii.member(jsii_name="addHostDefaultBackend")
    def add_host_default_backend(
        self,
        host: builtins.str,
        backend: IngressV1Beta1Backend,
    ) -> None:
        '''Specify a default backend for a specific host name.

        This backend will be used as a catch-all for requests
        targeted to this host name (the ``Host`` header matches this value).

        :param host: The host name to match.
        :param backend: The backend to route to.
        '''
        return typing.cast(None, jsii.invoke(self, "addHostDefaultBackend", [host, backend]))

    @jsii.member(jsii_name="addHostRule")
    def add_host_rule(
        self,
        host: builtins.str,
        path: builtins.str,
        backend: IngressV1Beta1Backend,
    ) -> None:
        '''Adds an ingress rule applied to requests to a specific host and a specific HTTP path (the ``Host`` header matches this value).

        :param host: The host name.
        :param path: The HTTP path.
        :param backend: The backend to route requests to.
        '''
        return typing.cast(None, jsii.invoke(self, "addHostRule", [host, path, backend]))

    @jsii.member(jsii_name="addRule")
    def add_rule(self, path: builtins.str, backend: IngressV1Beta1Backend) -> None:
        '''Adds an ingress rule applied to requests sent to a specific HTTP path.

        :param path: The HTTP path.
        :param backend: The backend to route requests to.
        '''
        return typing.cast(None, jsii.invoke(self, "addRule", [path, backend]))

    @jsii.member(jsii_name="addRules")
    def add_rules(self, *rules: IngressV1Beta1Rule) -> None:
        '''Adds rules to this ingress.

        :param rules: The rules to add.
        '''
        return typing.cast(None, jsii.invoke(self, "addRules", [*rules]))

    @jsii.member(jsii_name="addTls")
    def add_tls(self, tls: typing.Sequence[IngressV1Beta1Tls]) -> None:
        '''
        :param tls: -
        '''
        return typing.cast(None, jsii.invoke(self, "addTls", [tls]))

    @jsii.member(jsii_name="onValidate")
    def _on_validate(self) -> typing.List[builtins.str]:
        '''Validate the current construct.

        This method can be implemented by derived constructs in order to perform
        validation logic. It is called on all constructs before synthesis.
        '''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "onValidate", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))


@jsii.data_type(
    jsii_type="cdk8s-plus-21.IngressV1Beta1Props",
    jsii_struct_bases=[ResourceProps],
    name_mapping={
        "metadata": "metadata",
        "default_backend": "defaultBackend",
        "rules": "rules",
        "tls": "tls",
    },
)
class IngressV1Beta1Props(ResourceProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        default_backend: typing.Optional[IngressV1Beta1Backend] = None,
        rules: typing.Optional[typing.Sequence[IngressV1Beta1Rule]] = None,
        tls: typing.Optional[typing.Sequence[IngressV1Beta1Tls]] = None,
    ) -> None:
        '''Properties for ``Ingress``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param default_backend: The default backend services requests that do not match any rule. Using this option or the ``addDefaultBackend()`` method is equivalent to adding a rule with both ``path`` and ``host`` undefined.
        :param rules: Routing rules for this ingress. Each rule must define an ``IngressBackend`` that will receive the requests that match this rule. If both ``host`` and ``path`` are not specifiec, this backend will be used as the default backend of the ingress. You can also add rules later using ``addRule()``, ``addHostRule()``, ``addDefaultBackend()`` and ``addHostDefaultBackend()``.
        :param tls: TLS settings for this ingress. Using this option tells the ingress controller to expose a TLS endpoint. Currently the Ingress only supports a single TLS port, 443. If multiple members of this list specify different hosts, they will be multiplexed on the same port according to the hostname specified through the SNI TLS extension, if the ingress controller fulfilling the ingress supports SNI.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if default_backend is not None:
            self._values["default_backend"] = default_backend
        if rules is not None:
            self._values["rules"] = rules
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def default_backend(self) -> typing.Optional[IngressV1Beta1Backend]:
        '''The default backend services requests that do not match any rule.

        Using this option or the ``addDefaultBackend()`` method is equivalent to
        adding a rule with both ``path`` and ``host`` undefined.
        '''
        result = self._values.get("default_backend")
        return typing.cast(typing.Optional[IngressV1Beta1Backend], result)

    @builtins.property
    def rules(self) -> typing.Optional[typing.List[IngressV1Beta1Rule]]:
        '''Routing rules for this ingress.

        Each rule must define an ``IngressBackend`` that will receive the requests
        that match this rule. If both ``host`` and ``path`` are not specifiec, this
        backend will be used as the default backend of the ingress.

        You can also add rules later using ``addRule()``, ``addHostRule()``,
        ``addDefaultBackend()`` and ``addHostDefaultBackend()``.
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.List[IngressV1Beta1Rule]], result)

    @builtins.property
    def tls(self) -> typing.Optional[typing.List[IngressV1Beta1Tls]]:
        '''TLS settings for this ingress.

        Using this option tells the ingress controller to expose a TLS endpoint.
        Currently the Ingress only supports a single TLS port, 443. If multiple
        members of this list specify different hosts, they will be multiplexed on
        the same port according to the hostname specified through the SNI TLS
        extension, if the ingress controller fulfilling the ingress supports SNI.
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional[typing.List[IngressV1Beta1Tls]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1Beta1Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IPodTemplate)
class Job(Resource, metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-21.Job"):
    '''A Job creates one or more Pods and ensures that a specified number of them successfully terminate.

    As pods successfully complete,
    the Job tracks the successful completions. When a specified number of successful completions is reached, the task (ie, Job) is complete.
    Deleting a Job will clean up the Pods it created. A simple case is to create one Job object in order to reliably run one Pod to completion.
    The Job object will start a new Pod if the first Pod fails or is deleted (for example due to a node hardware failure or a node reboot).
    You can also use a Job to run multiple Pods in parallel.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        active_deadline: typing.Optional[cdk8s.Duration] = None,
        backoff_limit: typing.Optional[jsii.Number] = None,
        ttl_after_finished: typing.Optional[cdk8s.Duration] = None,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        pod_metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        docker_registry_auth: typing.Optional[DockerConfigSecret] = None,
        host_aliases: typing.Optional[typing.Sequence[HostAlias]] = None,
        init_containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        restart_policy: typing.Optional[RestartPolicy] = None,
        security_context: typing.Optional[PodSecurityContextProps] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence[Volume]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param active_deadline: Specifies the duration the job may be active before the system tries to terminate it. Default: - If unset, then there is no deadline.
        :param backoff_limit: Specifies the number of retries before marking this job failed. Default: - If not set, system defaults to 6.
        :param ttl_after_finished: Limits the lifetime of a Job that has finished execution (either Complete or Failed). If this field is set, after the Job finishes, it is eligible to be automatically deleted. When the Job is being deleted, its lifecycle guarantees (e.g. finalizers) will be honored. If this field is set to zero, the Job becomes eligible to be deleted immediately after it finishes. This field is alpha-level and is only honored by servers that enable the ``TTLAfterFinished`` feature. Default: - If this field is unset, the Job won't be automatically deleted.
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param pod_metadata: The pod metadata.
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        '''
        props = JobProps(
            active_deadline=active_deadline,
            backoff_limit=backoff_limit,
            ttl_after_finished=ttl_after_finished,
            metadata=metadata,
            pod_metadata=pod_metadata,
            containers=containers,
            docker_registry_auth=docker_registry_auth,
            host_aliases=host_aliases,
            init_containers=init_containers,
            restart_policy=restart_policy,
            security_context=security_context,
            service_account=service_account,
            volumes=volumes,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addContainer")
    def add_container(
        self,
        *,
        image: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, EnvValue]] = None,
        image_pull_policy: typing.Optional[ImagePullPolicy] = None,
        lifecycle: typing.Optional[ContainerLifecycle] = None,
        liveness: typing.Optional[Probe] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        readiness: typing.Optional[Probe] = None,
        resources: typing.Optional[Resources] = None,
        security_context: typing.Optional[ContainerSecurityContextProps] = None,
        startup: typing.Optional[Probe] = None,
        volume_mounts: typing.Optional[typing.Sequence[VolumeMount]] = None,
        working_dir: typing.Optional[builtins.str] = None,
    ) -> Container:
        '''Add a container to the pod.

        :param image: Docker image name.
        :param args: Arguments to the entrypoint. The docker image's CMD is used if ``command`` is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. Default: []
        :param command: Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell Default: - The docker image's ENTRYPOINT.
        :param env: List of environment variables to set in the container. Cannot be updated. Default: - No environment variables.
        :param image_pull_policy: Image pull policy for this container. Default: ImagePullPolicy.ALWAYS
        :param lifecycle: Describes actions that the management system should take in response to container lifecycle events.
        :param liveness: Periodic probe of container liveness. Container will be restarted if the probe fails. Default: - no liveness probe is defined
        :param name: Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. Default: 'main'
        :param port: Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. Default: - No port is exposed.
        :param readiness: Determines when the container is ready to serve traffic. Default: - no readiness probe is defined
        :param resources: Compute resources (CPU and memory requests and limits) required by the container.
        :param security_context: SecurityContext defines the security options the container should be run with. If set, the fields override equivalent fields of the pod's security context. Default: ensureNonRoot: false privileged: false readOnlyRootFilesystem: false
        :param startup: StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully Default: - no startup probe is defined.
        :param volume_mounts: Pod volumes to mount into the container's filesystem. Cannot be updated.
        :param working_dir: Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. Default: - The container runtime's default.
        '''
        container = ContainerProps(
            image=image,
            args=args,
            command=command,
            env=env,
            image_pull_policy=image_pull_policy,
            lifecycle=lifecycle,
            liveness=liveness,
            name=name,
            port=port,
            readiness=readiness,
            resources=resources,
            security_context=security_context,
            startup=startup,
            volume_mounts=volume_mounts,
            working_dir=working_dir,
        )

        return typing.cast(Container, jsii.invoke(self, "addContainer", [container]))

    @jsii.member(jsii_name="addHostAlias")
    def add_host_alias(
        self,
        *,
        hostnames: typing.Sequence[builtins.str],
        ip: builtins.str,
    ) -> None:
        '''
        :param hostnames: Hostnames for the chosen IP address.
        :param ip: IP address of the host file entry.
        '''
        host_alias = HostAlias(hostnames=hostnames, ip=ip)

        return typing.cast(None, jsii.invoke(self, "addHostAlias", [host_alias]))

    @jsii.member(jsii_name="addInitContainer")
    def add_init_container(
        self,
        *,
        image: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, EnvValue]] = None,
        image_pull_policy: typing.Optional[ImagePullPolicy] = None,
        lifecycle: typing.Optional[ContainerLifecycle] = None,
        liveness: typing.Optional[Probe] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        readiness: typing.Optional[Probe] = None,
        resources: typing.Optional[Resources] = None,
        security_context: typing.Optional[ContainerSecurityContextProps] = None,
        startup: typing.Optional[Probe] = None,
        volume_mounts: typing.Optional[typing.Sequence[VolumeMount]] = None,
        working_dir: typing.Optional[builtins.str] = None,
    ) -> Container:
        '''Add an init container to the pod.

        :param image: Docker image name.
        :param args: Arguments to the entrypoint. The docker image's CMD is used if ``command`` is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. Default: []
        :param command: Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell Default: - The docker image's ENTRYPOINT.
        :param env: List of environment variables to set in the container. Cannot be updated. Default: - No environment variables.
        :param image_pull_policy: Image pull policy for this container. Default: ImagePullPolicy.ALWAYS
        :param lifecycle: Describes actions that the management system should take in response to container lifecycle events.
        :param liveness: Periodic probe of container liveness. Container will be restarted if the probe fails. Default: - no liveness probe is defined
        :param name: Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. Default: 'main'
        :param port: Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. Default: - No port is exposed.
        :param readiness: Determines when the container is ready to serve traffic. Default: - no readiness probe is defined
        :param resources: Compute resources (CPU and memory requests and limits) required by the container.
        :param security_context: SecurityContext defines the security options the container should be run with. If set, the fields override equivalent fields of the pod's security context. Default: ensureNonRoot: false privileged: false readOnlyRootFilesystem: false
        :param startup: StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully Default: - no startup probe is defined.
        :param volume_mounts: Pod volumes to mount into the container's filesystem. Cannot be updated.
        :param working_dir: Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. Default: - The container runtime's default.
        '''
        container = ContainerProps(
            image=image,
            args=args,
            command=command,
            env=env,
            image_pull_policy=image_pull_policy,
            lifecycle=lifecycle,
            liveness=liveness,
            name=name,
            port=port,
            readiness=readiness,
            resources=resources,
            security_context=security_context,
            startup=startup,
            volume_mounts=volume_mounts,
            working_dir=working_dir,
        )

        return typing.cast(Container, jsii.invoke(self, "addInitContainer", [container]))

    @jsii.member(jsii_name="addVolume")
    def add_volume(self, volume: Volume) -> None:
        '''Add a volume to the pod.

        :param volume: -
        '''
        return typing.cast(None, jsii.invoke(self, "addVolume", [volume]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="containers")
    def containers(self) -> typing.List[Container]:
        '''The containers belonging to the pod.

        Use ``addContainer`` to add containers.
        '''
        return typing.cast(typing.List[Container], jsii.get(self, "containers"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hostAliases")
    def host_aliases(self) -> typing.List[HostAlias]:
        '''An optional list of hosts and IPs that will be injected into the pod's hosts file if specified.

        This is only valid for non-hostNetwork pods.
        '''
        return typing.cast(typing.List[HostAlias], jsii.get(self, "hostAliases"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="initContainers")
    def init_containers(self) -> typing.List[Container]:
        '''The init containers belonging to the pod.

        Use ``addInitContainer`` to add init containers.
        '''
        return typing.cast(typing.List[Container], jsii.get(self, "initContainers"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="podMetadata")
    def pod_metadata(self) -> cdk8s.ApiObjectMetadataDefinition:
        '''Provides read/write access to the underlying pod metadata of the resource.'''
        return typing.cast(cdk8s.ApiObjectMetadataDefinition, jsii.get(self, "podMetadata"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityContext")
    def security_context(self) -> PodSecurityContext:
        return typing.cast(PodSecurityContext, jsii.get(self, "securityContext"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="volumes")
    def volumes(self) -> typing.List[Volume]:
        '''The volumes associated with this pod.

        Use ``addVolume`` to add volumes.
        '''
        return typing.cast(typing.List[Volume], jsii.get(self, "volumes"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="activeDeadline")
    def active_deadline(self) -> typing.Optional[cdk8s.Duration]:
        '''Duration before job is terminated.

        If undefined, there is no deadline.
        '''
        return typing.cast(typing.Optional[cdk8s.Duration], jsii.get(self, "activeDeadline"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="backoffLimit")
    def backoff_limit(self) -> typing.Optional[jsii.Number]:
        '''Number of retries before marking failed.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backoffLimit"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="restartPolicy")
    def restart_policy(self) -> typing.Optional[RestartPolicy]:
        '''Restart policy for all containers within the pod.'''
        return typing.cast(typing.Optional[RestartPolicy], jsii.get(self, "restartPolicy"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> typing.Optional[IServiceAccount]:
        '''The service account used to run this pod.'''
        return typing.cast(typing.Optional[IServiceAccount], jsii.get(self, "serviceAccount"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ttlAfterFinished")
    def ttl_after_finished(self) -> typing.Optional[cdk8s.Duration]:
        '''TTL before the job is deleted after it is finished.'''
        return typing.cast(typing.Optional[cdk8s.Duration], jsii.get(self, "ttlAfterFinished"))


@jsii.data_type(
    jsii_type="cdk8s-plus-21.JobProps",
    jsii_struct_bases=[ResourceProps, PodTemplateProps],
    name_mapping={
        "metadata": "metadata",
        "containers": "containers",
        "docker_registry_auth": "dockerRegistryAuth",
        "host_aliases": "hostAliases",
        "init_containers": "initContainers",
        "restart_policy": "restartPolicy",
        "security_context": "securityContext",
        "service_account": "serviceAccount",
        "volumes": "volumes",
        "pod_metadata": "podMetadata",
        "active_deadline": "activeDeadline",
        "backoff_limit": "backoffLimit",
        "ttl_after_finished": "ttlAfterFinished",
    },
)
class JobProps(ResourceProps, PodTemplateProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        docker_registry_auth: typing.Optional[DockerConfigSecret] = None,
        host_aliases: typing.Optional[typing.Sequence[HostAlias]] = None,
        init_containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        restart_policy: typing.Optional[RestartPolicy] = None,
        security_context: typing.Optional[PodSecurityContextProps] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence[Volume]] = None,
        pod_metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        active_deadline: typing.Optional[cdk8s.Duration] = None,
        backoff_limit: typing.Optional[jsii.Number] = None,
        ttl_after_finished: typing.Optional[cdk8s.Duration] = None,
    ) -> None:
        '''Properties for initialization of ``Job``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        :param pod_metadata: The pod metadata.
        :param active_deadline: Specifies the duration the job may be active before the system tries to terminate it. Default: - If unset, then there is no deadline.
        :param backoff_limit: Specifies the number of retries before marking this job failed. Default: - If not set, system defaults to 6.
        :param ttl_after_finished: Limits the lifetime of a Job that has finished execution (either Complete or Failed). If this field is set, after the Job finishes, it is eligible to be automatically deleted. When the Job is being deleted, its lifecycle guarantees (e.g. finalizers) will be honored. If this field is set to zero, the Job becomes eligible to be deleted immediately after it finishes. This field is alpha-level and is only honored by servers that enable the ``TTLAfterFinished`` feature. Default: - If this field is unset, the Job won't be automatically deleted.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(security_context, dict):
            security_context = PodSecurityContextProps(**security_context)
        if isinstance(pod_metadata, dict):
            pod_metadata = cdk8s.ApiObjectMetadata(**pod_metadata)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if containers is not None:
            self._values["containers"] = containers
        if docker_registry_auth is not None:
            self._values["docker_registry_auth"] = docker_registry_auth
        if host_aliases is not None:
            self._values["host_aliases"] = host_aliases
        if init_containers is not None:
            self._values["init_containers"] = init_containers
        if restart_policy is not None:
            self._values["restart_policy"] = restart_policy
        if security_context is not None:
            self._values["security_context"] = security_context
        if service_account is not None:
            self._values["service_account"] = service_account
        if volumes is not None:
            self._values["volumes"] = volumes
        if pod_metadata is not None:
            self._values["pod_metadata"] = pod_metadata
        if active_deadline is not None:
            self._values["active_deadline"] = active_deadline
        if backoff_limit is not None:
            self._values["backoff_limit"] = backoff_limit
        if ttl_after_finished is not None:
            self._values["ttl_after_finished"] = ttl_after_finished

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of containers belonging to the pod.

        Containers cannot currently be
        added or removed. There must be at least one container in a Pod.

        You can add additionnal containers using ``podSpec.addContainer()``

        :default: - No containers. Note that a pod spec must include at least one container.
        '''
        result = self._values.get("containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def docker_registry_auth(self) -> typing.Optional[DockerConfigSecret]:
        '''A secret containing docker credentials for authenticating to a registry.

        :default: - No auth. Images are assumed to be publicly available.
        '''
        result = self._values.get("docker_registry_auth")
        return typing.cast(typing.Optional[DockerConfigSecret], result)

    @builtins.property
    def host_aliases(self) -> typing.Optional[typing.List[HostAlias]]:
        '''HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.

        :schema: io.k8s.api.core.v1.HostAlias
        '''
        result = self._values.get("host_aliases")
        return typing.cast(typing.Optional[typing.List[HostAlias]], result)

    @builtins.property
    def init_containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of initialization containers belonging to the pod.

        Init containers are executed in order prior to containers being started.
        If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy.
        The name for an init container or normal container must be unique among all containers.
        Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes.
        The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit
        for each resource type, and then using the max of of that value or the sum of the normal containers.
        Limits are applied to init containers in a similar fashion.

        Init containers cannot currently be added ,removed or updated.

        :default: - No init containers.

        :see: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
        '''
        result = self._values.get("init_containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def restart_policy(self) -> typing.Optional[RestartPolicy]:
        '''Restart policy for all containers within the pod.

        :default: RestartPolicy.ALWAYS

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy
        '''
        result = self._values.get("restart_policy")
        return typing.cast(typing.Optional[RestartPolicy], result)

    @builtins.property
    def security_context(self) -> typing.Optional[PodSecurityContextProps]:
        '''SecurityContext holds pod-level security attributes and common container settings.

        :default:

        fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS
        ensureNonRoot: false
        '''
        result = self._values.get("security_context")
        return typing.cast(typing.Optional[PodSecurityContextProps], result)

    @builtins.property
    def service_account(self) -> typing.Optional[IServiceAccount]:
        '''A service account provides an identity for processes that run in a Pod.

        When you (a human) access the cluster (for example, using kubectl), you are
        authenticated by the apiserver as a particular User Account (currently this
        is usually admin, unless your cluster administrator has customized your
        cluster). Processes in containers inside pods can also contact the
        apiserver. When they do, they are authenticated as a particular Service
        Account (for example, default).

        :default: - No service account.

        :see: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[IServiceAccount], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List[Volume]]:
        '''List of volumes that can be mounted by containers belonging to the pod.

        You can also add volumes later using ``podSpec.addVolume()``

        :default: - No volumes.

        :see: https://kubernetes.io/docs/concepts/storage/volumes
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List[Volume]], result)

    @builtins.property
    def pod_metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''The pod metadata.'''
        result = self._values.get("pod_metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def active_deadline(self) -> typing.Optional[cdk8s.Duration]:
        '''Specifies the duration the job may be active before the system tries to terminate it.

        :default: - If unset, then there is no deadline.
        '''
        result = self._values.get("active_deadline")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def backoff_limit(self) -> typing.Optional[jsii.Number]:
        '''Specifies the number of retries before marking this job failed.

        :default: - If not set, system defaults to 6.
        '''
        result = self._values.get("backoff_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ttl_after_finished(self) -> typing.Optional[cdk8s.Duration]:
        '''Limits the lifetime of a Job that has finished execution (either Complete or Failed).

        If this field is set, after the Job finishes, it is eligible to
        be automatically deleted. When the Job is being deleted, its lifecycle
        guarantees (e.g. finalizers) will be honored. If this field is set to zero,
        the Job becomes eligible to be deleted immediately after it finishes. This
        field is alpha-level and is only honored by servers that enable the
        ``TTLAfterFinished`` feature.

        :default: - If this field is unset, the Job won't be automatically deleted.
        '''
        result = self._values.get("ttl_after_finished")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JobProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IPersistentVolume, IStorage)
class PersistentVolume(
    Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-21.PersistentVolume",
):
    '''A PersistentVolume (PV) is a piece of storage in the cluster that has been provisioned by an administrator or dynamically provisioned using Storage Classes.

    It is a resource in the cluster just like a node is a cluster resource.
    PVs are volume plugins like Volumes, but have a lifecycle independent of any
    individual Pod that uses the PV. This API object captures the details of the
    implementation of the storage, be that NFS, iSCSI, or a
    cloud-provider-specific storage system.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        access_modes: typing.Optional[typing.Sequence[PersistentVolumeAccessMode]] = None,
        claim: typing.Optional[IPersistentVolumeClaim] = None,
        mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        reclaim_policy: typing.Optional[PersistentVolumeReclaimPolicy] = None,
        storage: typing.Optional[cdk8s.Size] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        volume_mode: typing.Optional[PersistentVolumeMode] = None,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param access_modes: Contains all ways the volume can be mounted. Default: - No access modes.
        :param claim: Part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. Default: - Not bound to a specific claim.
        :param mount_options: A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. Default: - No options.
        :param reclaim_policy: When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource. The reclaim policy tells the cluster what to do with the volume after it has been released of its claim. Default: PersistentVolumeReclaimPolicy.RETAIN
        :param storage: What is the storage capacity of this volume. Default: - No specified.
        :param storage_class_name: Name of StorageClass to which this persistent volume belongs. Default: - Volume does not belong to any storage class.
        :param volume_mode: Defines what type of volume is required by the claim. Default: VolumeMode.FILE_SYSTEM
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        props = PersistentVolumeProps(
            access_modes=access_modes,
            claim=claim,
            mount_options=mount_options,
            reclaim_policy=reclaim_policy,
            storage=storage,
            storage_class_name=storage_class_name,
            volume_mode=volume_mode,
            metadata=metadata,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromPersistentVolumeName") # type: ignore[misc]
    @builtins.classmethod
    def from_persistent_volume_name(
        cls,
        volume_name: builtins.str,
    ) -> IPersistentVolume:
        '''Imports a pv from the cluster as a reference.

        :param volume_name: The name of the pv to reference.
        '''
        return typing.cast(IPersistentVolume, jsii.sinvoke(cls, "fromPersistentVolumeName", [volume_name]))

    @jsii.member(jsii_name="asVolume")
    def as_volume(self) -> Volume:
        '''Convert the piece of storage into a concrete volume.'''
        return typing.cast(Volume, jsii.invoke(self, "asVolume", []))

    @jsii.member(jsii_name="bind")
    def bind(self, pvc: IPersistentVolumeClaim) -> None:
        '''Bind a volume to a specific claim.

        Note that you must also bind the claim to the volume.

        :param pvc: The PVC to bind to.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#binding
        '''
        return typing.cast(None, jsii.invoke(self, "bind", [pvc]))

    @jsii.member(jsii_name="reserve")
    def reserve(self) -> "PersistentVolumeClaim":
        '''Reserve a ``PersistentVolume`` by creating a ``PersistentVolumeClaim`` that is wired to claim this volume.

        Note that this method will throw in case the volume is already claimed.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#reserving-a-persistentvolume
        '''
        return typing.cast("PersistentVolumeClaim", jsii.invoke(self, "reserve", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mode")
    def mode(self) -> PersistentVolumeMode:
        '''Volume mode of this volume.'''
        return typing.cast(PersistentVolumeMode, jsii.get(self, "mode"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="reclaimPolicy")
    def reclaim_policy(self) -> PersistentVolumeReclaimPolicy:
        '''Reclaim policy of this volume.'''
        return typing.cast(PersistentVolumeReclaimPolicy, jsii.get(self, "reclaimPolicy"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="accessModes")
    def access_modes(self) -> typing.Optional[typing.List[PersistentVolumeAccessMode]]:
        '''Access modes requirement of this claim.'''
        return typing.cast(typing.Optional[typing.List[PersistentVolumeAccessMode]], jsii.get(self, "accessModes"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="claim")
    def claim(self) -> typing.Optional[IPersistentVolumeClaim]:
        '''PVC this volume is bound to.

        Undefined means this volume is not yet
        claimed by any PVC.
        '''
        return typing.cast(typing.Optional[IPersistentVolumeClaim], jsii.get(self, "claim"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mountOptions")
    def mount_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Mount options of this volume.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "mountOptions"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="storage")
    def storage(self) -> typing.Optional[cdk8s.Size]:
        '''Storage size of this volume.'''
        return typing.cast(typing.Optional[cdk8s.Size], jsii.get(self, "storage"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="storageClassName")
    def storage_class_name(self) -> typing.Optional[builtins.str]:
        '''Storage class this volume belongs to.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageClassName"))


@jsii.implements(IPersistentVolumeClaim)
class PersistentVolumeClaim(
    Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-21.PersistentVolumeClaim",
):
    '''A PersistentVolumeClaim (PVC) is a request for storage by a user.

    It is similar to a Pod. Pods consume node resources and PVCs consume PV resources.
    Pods can request specific levels of resources (CPU and Memory).
    Claims can request specific size and access modes
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        access_modes: typing.Optional[typing.Sequence[PersistentVolumeAccessMode]] = None,
        storage: typing.Optional[cdk8s.Size] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        volume: typing.Optional[IPersistentVolume] = None,
        volume_mode: typing.Optional[PersistentVolumeMode] = None,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param access_modes: Contains the access modes the volume should support. Default: - No access modes requirement.
        :param storage: Minimum storage size the volume should have. Default: - No storage requirement.
        :param storage_class_name: Name of the StorageClass required by the claim. When this property is not set, the behavior is as follows:. - If the admission plugin is turned on, the storage class marked as default will be used. - If the admission plugin is turned off, the pvc can only be bound to volumes without a storage class. Default: - Not set.
        :param volume: The PersistentVolume backing this claim. The control plane still checks that storage class, access modes, and requested storage size on the volume are valid. Note that in order to guarantee a proper binding, the volume should also define a ``claimRef`` referring to this claim. Otherwise, the volume may be claimed be other pvc's before it gets a chance to bind to this one. If the volume is managed (i.e not imported), you can use ``pv.claim()`` to easily create a bi-directional bounded claim. Default: - No specific volume binding.
        :param volume_mode: Defines what type of volume is required by the claim. Default: VolumeMode.FILE_SYSTEM
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        props = PersistentVolumeClaimProps(
            access_modes=access_modes,
            storage=storage,
            storage_class_name=storage_class_name,
            volume=volume,
            volume_mode=volume_mode,
            metadata=metadata,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromClaimName") # type: ignore[misc]
    @builtins.classmethod
    def from_claim_name(cls, claim_name: builtins.str) -> IPersistentVolumeClaim:
        '''Imports a pvc from the cluster as a reference.

        :param claim_name: The name of the pvc to reference.
        '''
        return typing.cast(IPersistentVolumeClaim, jsii.sinvoke(cls, "fromClaimName", [claim_name]))

    @jsii.member(jsii_name="bind")
    def bind(self, pv: IPersistentVolume) -> None:
        '''Bind a claim to a specific volume.

        Note that you must also bind the volume to the claim.

        :param pv: The PV to bind to.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#binding
        '''
        return typing.cast(None, jsii.invoke(self, "bind", [pv]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="volumeMode")
    def volume_mode(self) -> PersistentVolumeMode:
        '''Volume mode requirement of this claim.'''
        return typing.cast(PersistentVolumeMode, jsii.get(self, "volumeMode"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="accessModes")
    def access_modes(self) -> typing.Optional[typing.List[PersistentVolumeAccessMode]]:
        '''Access modes requirement of this claim.'''
        return typing.cast(typing.Optional[typing.List[PersistentVolumeAccessMode]], jsii.get(self, "accessModes"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="storage")
    def storage(self) -> typing.Optional[cdk8s.Size]:
        '''Storage requirement of this claim.'''
        return typing.cast(typing.Optional[cdk8s.Size], jsii.get(self, "storage"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="storageClassName")
    def storage_class_name(self) -> typing.Optional[builtins.str]:
        '''Storage class requirment of this claim.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageClassName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="volume")
    def volume(self) -> typing.Optional[IPersistentVolume]:
        '''PV this claim is bound to.

        Undefined means the claim is not bound
        to any specific volume.
        '''
        return typing.cast(typing.Optional[IPersistentVolume], jsii.get(self, "volume"))


@jsii.data_type(
    jsii_type="cdk8s-plus-21.PersistentVolumeClaimProps",
    jsii_struct_bases=[ResourceProps],
    name_mapping={
        "metadata": "metadata",
        "access_modes": "accessModes",
        "storage": "storage",
        "storage_class_name": "storageClassName",
        "volume": "volume",
        "volume_mode": "volumeMode",
    },
)
class PersistentVolumeClaimProps(ResourceProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        access_modes: typing.Optional[typing.Sequence[PersistentVolumeAccessMode]] = None,
        storage: typing.Optional[cdk8s.Size] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        volume: typing.Optional[IPersistentVolume] = None,
        volume_mode: typing.Optional[PersistentVolumeMode] = None,
    ) -> None:
        '''Properties for ``PersistentVolumeClaim``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param access_modes: Contains the access modes the volume should support. Default: - No access modes requirement.
        :param storage: Minimum storage size the volume should have. Default: - No storage requirement.
        :param storage_class_name: Name of the StorageClass required by the claim. When this property is not set, the behavior is as follows:. - If the admission plugin is turned on, the storage class marked as default will be used. - If the admission plugin is turned off, the pvc can only be bound to volumes without a storage class. Default: - Not set.
        :param volume: The PersistentVolume backing this claim. The control plane still checks that storage class, access modes, and requested storage size on the volume are valid. Note that in order to guarantee a proper binding, the volume should also define a ``claimRef`` referring to this claim. Otherwise, the volume may be claimed be other pvc's before it gets a chance to bind to this one. If the volume is managed (i.e not imported), you can use ``pv.claim()`` to easily create a bi-directional bounded claim. Default: - No specific volume binding.
        :param volume_mode: Defines what type of volume is required by the claim. Default: VolumeMode.FILE_SYSTEM
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if access_modes is not None:
            self._values["access_modes"] = access_modes
        if storage is not None:
            self._values["storage"] = storage
        if storage_class_name is not None:
            self._values["storage_class_name"] = storage_class_name
        if volume is not None:
            self._values["volume"] = volume
        if volume_mode is not None:
            self._values["volume_mode"] = volume_mode

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def access_modes(self) -> typing.Optional[typing.List[PersistentVolumeAccessMode]]:
        '''Contains the access modes the volume should support.

        :default: - No access modes requirement.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1
        '''
        result = self._values.get("access_modes")
        return typing.cast(typing.Optional[typing.List[PersistentVolumeAccessMode]], result)

    @builtins.property
    def storage(self) -> typing.Optional[cdk8s.Size]:
        '''Minimum storage size the volume should have.

        :default: - No storage requirement.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources
        '''
        result = self._values.get("storage")
        return typing.cast(typing.Optional[cdk8s.Size], result)

    @builtins.property
    def storage_class_name(self) -> typing.Optional[builtins.str]:
        '''Name of the StorageClass required by the claim. When this property is not set, the behavior is as follows:.

        - If the admission plugin is turned on, the storage class marked as default will be used.
        - If the admission plugin is turned off, the pvc can only be bound to volumes without a storage class.

        :default: - Not set.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1
        '''
        result = self._values.get("storage_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume(self) -> typing.Optional[IPersistentVolume]:
        '''The PersistentVolume backing this claim.

        The control plane still checks that storage class, access modes,
        and requested storage size on the volume are valid.

        Note that in order to guarantee a proper binding, the volume should
        also define a ``claimRef`` referring to this claim. Otherwise, the volume may be
        claimed be other pvc's before it gets a chance to bind to this one.

        If the volume is managed (i.e not imported), you can use ``pv.claim()`` to easily
        create a bi-directional bounded claim.

        :default: - No specific volume binding.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#binding.
        '''
        result = self._values.get("volume")
        return typing.cast(typing.Optional[IPersistentVolume], result)

    @builtins.property
    def volume_mode(self) -> typing.Optional[PersistentVolumeMode]:
        '''Defines what type of volume is required by the claim.

        :default: VolumeMode.FILE_SYSTEM
        '''
        result = self._values.get("volume_mode")
        return typing.cast(typing.Optional[PersistentVolumeMode], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeClaimProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.PersistentVolumeProps",
    jsii_struct_bases=[ResourceProps],
    name_mapping={
        "metadata": "metadata",
        "access_modes": "accessModes",
        "claim": "claim",
        "mount_options": "mountOptions",
        "reclaim_policy": "reclaimPolicy",
        "storage": "storage",
        "storage_class_name": "storageClassName",
        "volume_mode": "volumeMode",
    },
)
class PersistentVolumeProps(ResourceProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        access_modes: typing.Optional[typing.Sequence[PersistentVolumeAccessMode]] = None,
        claim: typing.Optional[IPersistentVolumeClaim] = None,
        mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        reclaim_policy: typing.Optional[PersistentVolumeReclaimPolicy] = None,
        storage: typing.Optional[cdk8s.Size] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        volume_mode: typing.Optional[PersistentVolumeMode] = None,
    ) -> None:
        '''Properties for ``PersistentVolume``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param access_modes: Contains all ways the volume can be mounted. Default: - No access modes.
        :param claim: Part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. Default: - Not bound to a specific claim.
        :param mount_options: A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. Default: - No options.
        :param reclaim_policy: When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource. The reclaim policy tells the cluster what to do with the volume after it has been released of its claim. Default: PersistentVolumeReclaimPolicy.RETAIN
        :param storage: What is the storage capacity of this volume. Default: - No specified.
        :param storage_class_name: Name of StorageClass to which this persistent volume belongs. Default: - Volume does not belong to any storage class.
        :param volume_mode: Defines what type of volume is required by the claim. Default: VolumeMode.FILE_SYSTEM
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if access_modes is not None:
            self._values["access_modes"] = access_modes
        if claim is not None:
            self._values["claim"] = claim
        if mount_options is not None:
            self._values["mount_options"] = mount_options
        if reclaim_policy is not None:
            self._values["reclaim_policy"] = reclaim_policy
        if storage is not None:
            self._values["storage"] = storage
        if storage_class_name is not None:
            self._values["storage_class_name"] = storage_class_name
        if volume_mode is not None:
            self._values["volume_mode"] = volume_mode

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def access_modes(self) -> typing.Optional[typing.List[PersistentVolumeAccessMode]]:
        '''Contains all ways the volume can be mounted.

        :default: - No access modes.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes
        '''
        result = self._values.get("access_modes")
        return typing.cast(typing.Optional[typing.List[PersistentVolumeAccessMode]], result)

    @builtins.property
    def claim(self) -> typing.Optional[IPersistentVolumeClaim]:
        '''Part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim.

        Expected to be non-nil when bound.

        :default: - Not bound to a specific claim.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding
        '''
        result = self._values.get("claim")
        return typing.cast(typing.Optional[IPersistentVolumeClaim], result)

    @builtins.property
    def mount_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid.

        :default: - No options.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options
        '''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def reclaim_policy(self) -> typing.Optional[PersistentVolumeReclaimPolicy]:
        '''When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource.

        The reclaim policy tells the cluster what to do with
        the volume after it has been released of its claim.

        :default: PersistentVolumeReclaimPolicy.RETAIN

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming
        '''
        result = self._values.get("reclaim_policy")
        return typing.cast(typing.Optional[PersistentVolumeReclaimPolicy], result)

    @builtins.property
    def storage(self) -> typing.Optional[cdk8s.Size]:
        '''What is the storage capacity of this volume.

        :default: - No specified.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources
        '''
        result = self._values.get("storage")
        return typing.cast(typing.Optional[cdk8s.Size], result)

    @builtins.property
    def storage_class_name(self) -> typing.Optional[builtins.str]:
        '''Name of StorageClass to which this persistent volume belongs.

        :default: - Volume does not belong to any storage class.
        '''
        result = self._values.get("storage_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_mode(self) -> typing.Optional[PersistentVolumeMode]:
        '''Defines what type of volume is required by the claim.

        :default: VolumeMode.FILE_SYSTEM
        '''
        result = self._values.get("volume_mode")
        return typing.cast(typing.Optional[PersistentVolumeMode], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IPodSpec)
class Pod(Resource, metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-21.Pod"):
    '''Pod is a collection of containers that can run on a host.

    This resource is
    created by clients and scheduled onto hosts.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        docker_registry_auth: typing.Optional[DockerConfigSecret] = None,
        host_aliases: typing.Optional[typing.Sequence[HostAlias]] = None,
        init_containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        restart_policy: typing.Optional[RestartPolicy] = None,
        security_context: typing.Optional[PodSecurityContextProps] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence[Volume]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        '''
        props = PodProps(
            metadata=metadata,
            containers=containers,
            docker_registry_auth=docker_registry_auth,
            host_aliases=host_aliases,
            init_containers=init_containers,
            restart_policy=restart_policy,
            security_context=security_context,
            service_account=service_account,
            volumes=volumes,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addContainer")
    def add_container(
        self,
        *,
        image: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, EnvValue]] = None,
        image_pull_policy: typing.Optional[ImagePullPolicy] = None,
        lifecycle: typing.Optional[ContainerLifecycle] = None,
        liveness: typing.Optional[Probe] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        readiness: typing.Optional[Probe] = None,
        resources: typing.Optional[Resources] = None,
        security_context: typing.Optional[ContainerSecurityContextProps] = None,
        startup: typing.Optional[Probe] = None,
        volume_mounts: typing.Optional[typing.Sequence[VolumeMount]] = None,
        working_dir: typing.Optional[builtins.str] = None,
    ) -> Container:
        '''Add a container to the pod.

        :param image: Docker image name.
        :param args: Arguments to the entrypoint. The docker image's CMD is used if ``command`` is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. Default: []
        :param command: Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell Default: - The docker image's ENTRYPOINT.
        :param env: List of environment variables to set in the container. Cannot be updated. Default: - No environment variables.
        :param image_pull_policy: Image pull policy for this container. Default: ImagePullPolicy.ALWAYS
        :param lifecycle: Describes actions that the management system should take in response to container lifecycle events.
        :param liveness: Periodic probe of container liveness. Container will be restarted if the probe fails. Default: - no liveness probe is defined
        :param name: Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. Default: 'main'
        :param port: Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. Default: - No port is exposed.
        :param readiness: Determines when the container is ready to serve traffic. Default: - no readiness probe is defined
        :param resources: Compute resources (CPU and memory requests and limits) required by the container.
        :param security_context: SecurityContext defines the security options the container should be run with. If set, the fields override equivalent fields of the pod's security context. Default: ensureNonRoot: false privileged: false readOnlyRootFilesystem: false
        :param startup: StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully Default: - no startup probe is defined.
        :param volume_mounts: Pod volumes to mount into the container's filesystem. Cannot be updated.
        :param working_dir: Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. Default: - The container runtime's default.
        '''
        container = ContainerProps(
            image=image,
            args=args,
            command=command,
            env=env,
            image_pull_policy=image_pull_policy,
            lifecycle=lifecycle,
            liveness=liveness,
            name=name,
            port=port,
            readiness=readiness,
            resources=resources,
            security_context=security_context,
            startup=startup,
            volume_mounts=volume_mounts,
            working_dir=working_dir,
        )

        return typing.cast(Container, jsii.invoke(self, "addContainer", [container]))

    @jsii.member(jsii_name="addHostAlias")
    def add_host_alias(
        self,
        *,
        hostnames: typing.Sequence[builtins.str],
        ip: builtins.str,
    ) -> None:
        '''
        :param hostnames: Hostnames for the chosen IP address.
        :param ip: IP address of the host file entry.
        '''
        host_alias = HostAlias(hostnames=hostnames, ip=ip)

        return typing.cast(None, jsii.invoke(self, "addHostAlias", [host_alias]))

    @jsii.member(jsii_name="addInitContainer")
    def add_init_container(
        self,
        *,
        image: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, EnvValue]] = None,
        image_pull_policy: typing.Optional[ImagePullPolicy] = None,
        lifecycle: typing.Optional[ContainerLifecycle] = None,
        liveness: typing.Optional[Probe] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        readiness: typing.Optional[Probe] = None,
        resources: typing.Optional[Resources] = None,
        security_context: typing.Optional[ContainerSecurityContextProps] = None,
        startup: typing.Optional[Probe] = None,
        volume_mounts: typing.Optional[typing.Sequence[VolumeMount]] = None,
        working_dir: typing.Optional[builtins.str] = None,
    ) -> Container:
        '''Add an init container to the pod.

        :param image: Docker image name.
        :param args: Arguments to the entrypoint. The docker image's CMD is used if ``command`` is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. Default: []
        :param command: Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell Default: - The docker image's ENTRYPOINT.
        :param env: List of environment variables to set in the container. Cannot be updated. Default: - No environment variables.
        :param image_pull_policy: Image pull policy for this container. Default: ImagePullPolicy.ALWAYS
        :param lifecycle: Describes actions that the management system should take in response to container lifecycle events.
        :param liveness: Periodic probe of container liveness. Container will be restarted if the probe fails. Default: - no liveness probe is defined
        :param name: Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. Default: 'main'
        :param port: Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. Default: - No port is exposed.
        :param readiness: Determines when the container is ready to serve traffic. Default: - no readiness probe is defined
        :param resources: Compute resources (CPU and memory requests and limits) required by the container.
        :param security_context: SecurityContext defines the security options the container should be run with. If set, the fields override equivalent fields of the pod's security context. Default: ensureNonRoot: false privileged: false readOnlyRootFilesystem: false
        :param startup: StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully Default: - no startup probe is defined.
        :param volume_mounts: Pod volumes to mount into the container's filesystem. Cannot be updated.
        :param working_dir: Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. Default: - The container runtime's default.
        '''
        container = ContainerProps(
            image=image,
            args=args,
            command=command,
            env=env,
            image_pull_policy=image_pull_policy,
            lifecycle=lifecycle,
            liveness=liveness,
            name=name,
            port=port,
            readiness=readiness,
            resources=resources,
            security_context=security_context,
            startup=startup,
            volume_mounts=volume_mounts,
            working_dir=working_dir,
        )

        return typing.cast(Container, jsii.invoke(self, "addInitContainer", [container]))

    @jsii.member(jsii_name="addVolume")
    def add_volume(self, volume: Volume) -> None:
        '''Add a volume to the pod.

        :param volume: -
        '''
        return typing.cast(None, jsii.invoke(self, "addVolume", [volume]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="containers")
    def containers(self) -> typing.List[Container]:
        '''The containers belonging to the pod.

        Use ``addContainer`` to add containers.
        '''
        return typing.cast(typing.List[Container], jsii.get(self, "containers"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hostAliases")
    def host_aliases(self) -> typing.List[HostAlias]:
        '''An optional list of hosts and IPs that will be injected into the pod's hosts file if specified.

        This is only valid for non-hostNetwork pods.
        '''
        return typing.cast(typing.List[HostAlias], jsii.get(self, "hostAliases"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="initContainers")
    def init_containers(self) -> typing.List[Container]:
        '''The init containers belonging to the pod.

        Use ``addInitContainer`` to add init containers.
        '''
        return typing.cast(typing.List[Container], jsii.get(self, "initContainers"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityContext")
    def security_context(self) -> PodSecurityContext:
        return typing.cast(PodSecurityContext, jsii.get(self, "securityContext"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="volumes")
    def volumes(self) -> typing.List[Volume]:
        '''The volumes associated with this pod.

        Use ``addVolume`` to add volumes.
        '''
        return typing.cast(typing.List[Volume], jsii.get(self, "volumes"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="restartPolicy")
    def restart_policy(self) -> typing.Optional[RestartPolicy]:
        '''Restart policy for all containers within the pod.'''
        return typing.cast(typing.Optional[RestartPolicy], jsii.get(self, "restartPolicy"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> typing.Optional[IServiceAccount]:
        '''The service account used to run this pod.'''
        return typing.cast(typing.Optional[IServiceAccount], jsii.get(self, "serviceAccount"))


@jsii.data_type(
    jsii_type="cdk8s-plus-21.PodProps",
    jsii_struct_bases=[ResourceProps, PodSpecProps],
    name_mapping={
        "metadata": "metadata",
        "containers": "containers",
        "docker_registry_auth": "dockerRegistryAuth",
        "host_aliases": "hostAliases",
        "init_containers": "initContainers",
        "restart_policy": "restartPolicy",
        "security_context": "securityContext",
        "service_account": "serviceAccount",
        "volumes": "volumes",
    },
)
class PodProps(ResourceProps, PodSpecProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        docker_registry_auth: typing.Optional[DockerConfigSecret] = None,
        host_aliases: typing.Optional[typing.Sequence[HostAlias]] = None,
        init_containers: typing.Optional[typing.Sequence[ContainerProps]] = None,
        restart_policy: typing.Optional[RestartPolicy] = None,
        security_context: typing.Optional[PodSecurityContextProps] = None,
        service_account: typing.Optional[IServiceAccount] = None,
        volumes: typing.Optional[typing.Sequence[Volume]] = None,
    ) -> None:
        '''Properties for initialization of ``Pod``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. You can add additionnal containers using ``podSpec.addContainer()`` Default: - No containers. Note that a pod spec must include at least one container.
        :param docker_registry_auth: A secret containing docker credentials for authenticating to a registry. Default: - No auth. Images are assumed to be publicly available.
        :param host_aliases: HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
        :param init_containers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added ,removed or updated. Default: - No init containers.
        :param restart_policy: Restart policy for all containers within the pod. Default: RestartPolicy.ALWAYS
        :param security_context: SecurityContext holds pod-level security attributes and common container settings. Default: fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS ensureNonRoot: false
        :param service_account: A service account provides an identity for processes that run in a Pod. When you (a human) access the cluster (for example, using kubectl), you are authenticated by the apiserver as a particular User Account (currently this is usually admin, unless your cluster administrator has customized your cluster). Processes in containers inside pods can also contact the apiserver. When they do, they are authenticated as a particular Service Account (for example, default). Default: - No service account.
        :param volumes: List of volumes that can be mounted by containers belonging to the pod. You can also add volumes later using ``podSpec.addVolume()`` Default: - No volumes.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(security_context, dict):
            security_context = PodSecurityContextProps(**security_context)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if containers is not None:
            self._values["containers"] = containers
        if docker_registry_auth is not None:
            self._values["docker_registry_auth"] = docker_registry_auth
        if host_aliases is not None:
            self._values["host_aliases"] = host_aliases
        if init_containers is not None:
            self._values["init_containers"] = init_containers
        if restart_policy is not None:
            self._values["restart_policy"] = restart_policy
        if security_context is not None:
            self._values["security_context"] = security_context
        if service_account is not None:
            self._values["service_account"] = service_account
        if volumes is not None:
            self._values["volumes"] = volumes

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of containers belonging to the pod.

        Containers cannot currently be
        added or removed. There must be at least one container in a Pod.

        You can add additionnal containers using ``podSpec.addContainer()``

        :default: - No containers. Note that a pod spec must include at least one container.
        '''
        result = self._values.get("containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def docker_registry_auth(self) -> typing.Optional[DockerConfigSecret]:
        '''A secret containing docker credentials for authenticating to a registry.

        :default: - No auth. Images are assumed to be publicly available.
        '''
        result = self._values.get("docker_registry_auth")
        return typing.cast(typing.Optional[DockerConfigSecret], result)

    @builtins.property
    def host_aliases(self) -> typing.Optional[typing.List[HostAlias]]:
        '''HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.

        :schema: io.k8s.api.core.v1.HostAlias
        '''
        result = self._values.get("host_aliases")
        return typing.cast(typing.Optional[typing.List[HostAlias]], result)

    @builtins.property
    def init_containers(self) -> typing.Optional[typing.List[ContainerProps]]:
        '''List of initialization containers belonging to the pod.

        Init containers are executed in order prior to containers being started.
        If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy.
        The name for an init container or normal container must be unique among all containers.
        Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes.
        The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit
        for each resource type, and then using the max of of that value or the sum of the normal containers.
        Limits are applied to init containers in a similar fashion.

        Init containers cannot currently be added ,removed or updated.

        :default: - No init containers.

        :see: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
        '''
        result = self._values.get("init_containers")
        return typing.cast(typing.Optional[typing.List[ContainerProps]], result)

    @builtins.property
    def restart_policy(self) -> typing.Optional[RestartPolicy]:
        '''Restart policy for all containers within the pod.

        :default: RestartPolicy.ALWAYS

        :see: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy
        '''
        result = self._values.get("restart_policy")
        return typing.cast(typing.Optional[RestartPolicy], result)

    @builtins.property
    def security_context(self) -> typing.Optional[PodSecurityContextProps]:
        '''SecurityContext holds pod-level security attributes and common container settings.

        :default:

        fsGroupChangePolicy: FsGroupChangePolicy.FsGroupChangePolicy.ALWAYS
        ensureNonRoot: false
        '''
        result = self._values.get("security_context")
        return typing.cast(typing.Optional[PodSecurityContextProps], result)

    @builtins.property
    def service_account(self) -> typing.Optional[IServiceAccount]:
        '''A service account provides an identity for processes that run in a Pod.

        When you (a human) access the cluster (for example, using kubectl), you are
        authenticated by the apiserver as a particular User Account (currently this
        is usually admin, unless your cluster administrator has customized your
        cluster). Processes in containers inside pods can also contact the
        apiserver. When they do, they are authenticated as a particular Service
        Account (for example, default).

        :default: - No service account.

        :see: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[IServiceAccount], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List[Volume]]:
        '''List of volumes that can be mounted by containers belonging to the pod.

        You can also add volumes later using ``podSpec.addVolume()``

        :default: - No volumes.

        :see: https://kubernetes.io/docs/concepts/storage/volumes
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List[Volume]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.SecretProps",
    jsii_struct_bases=[CommonSecretProps],
    name_mapping={
        "metadata": "metadata",
        "immutable": "immutable",
        "string_data": "stringData",
        "type": "type",
    },
)
class SecretProps(CommonSecretProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        immutable: typing.Optional[builtins.bool] = None,
        string_data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options for ``Secret``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param string_data: stringData allows specifying non-binary secret data in string form. It is provided as a write-only convenience method. All keys and values are merged into the data field on write, overwriting any existing values. It is never output when reading from the API.
        :param type: Optional type associated with the secret. Used to facilitate programmatic handling of secret data by various controllers. Default: undefined - Don't set a type.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if immutable is not None:
            self._values["immutable"] = immutable
        if string_data is not None:
            self._values["string_data"] = string_data
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def immutable(self) -> typing.Optional[builtins.bool]:
        '''If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified).

        If not set to true, the field can be modified at any time.

        :default: false
        '''
        result = self._values.get("immutable")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def string_data(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''stringData allows specifying non-binary secret data in string form.

        It is
        provided as a write-only convenience method. All keys and values are merged
        into the data field on write, overwriting any existing values. It is never
        output when reading from the API.
        '''
        result = self._values.get("string_data")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Optional type associated with the secret.

        Used to facilitate programmatic
        handling of secret data by various controllers.

        :default: undefined - Don't set a type.
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecretProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.ServiceAccountTokenSecretProps",
    jsii_struct_bases=[CommonSecretProps],
    name_mapping={
        "metadata": "metadata",
        "immutable": "immutable",
        "service_account": "serviceAccount",
    },
)
class ServiceAccountTokenSecretProps(CommonSecretProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        immutable: typing.Optional[builtins.bool] = None,
        service_account: IServiceAccount,
    ) -> None:
        '''Options for ``ServiceAccountTokenSecret``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param service_account: The service account to store a secret for.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        self._values: typing.Dict[str, typing.Any] = {
            "service_account": service_account,
        }
        if metadata is not None:
            self._values["metadata"] = metadata
        if immutable is not None:
            self._values["immutable"] = immutable

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def immutable(self) -> typing.Optional[builtins.bool]:
        '''If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified).

        If not set to true, the field can be modified at any time.

        :default: false
        '''
        result = self._values.get("immutable")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def service_account(self) -> IServiceAccount:
        '''The service account to store a secret for.'''
        result = self._values.get("service_account")
        assert result is not None, "Required property 'service_account' is missing"
        return typing.cast(IServiceAccount, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceAccountTokenSecretProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.ServicePort",
    jsii_struct_bases=[ServicePortOptions],
    name_mapping={
        "name": "name",
        "node_port": "nodePort",
        "protocol": "protocol",
        "target_port": "targetPort",
        "port": "port",
    },
)
class ServicePort(ServicePortOptions):
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        node_port: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[Protocol] = None,
        target_port: typing.Optional[jsii.Number] = None,
        port: jsii.Number,
    ) -> None:
        '''Definition of a service port.

        :param name: The name of this port within the service. This must be a DNS_LABEL. All ports within a ServiceSpec must have unique names. This maps to the 'Name' field in EndpointPort objects. Optional if only one ServicePort is defined on this service.
        :param node_port: The port on each node on which this service is exposed when type=NodePort or LoadBalancer. Usually assigned by the system. If specified, it will be allocated to the service if unused or else creation of the service will fail. Default is to auto-allocate a port if the ServiceType of this Service requires one. Default: - auto-allocate a port if the ServiceType of this Service requires one.
        :param protocol: The IP protocol for this port. Supports "TCP", "UDP", and "SCTP". Default is TCP. Default: Protocol.TCP
        :param target_port: The port number the service will redirect to. Default: - The value of ``port`` will be used.
        :param port: The port number the service will bind to.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "port": port,
        }
        if name is not None:
            self._values["name"] = name
        if node_port is not None:
            self._values["node_port"] = node_port
        if protocol is not None:
            self._values["protocol"] = protocol
        if target_port is not None:
            self._values["target_port"] = target_port

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of this port within the service.

        This must be a DNS_LABEL. All
        ports within a ServiceSpec must have unique names. This maps to the 'Name'
        field in EndpointPort objects. Optional if only one ServicePort is defined
        on this service.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_port(self) -> typing.Optional[jsii.Number]:
        '''The port on each node on which this service is exposed when type=NodePort or LoadBalancer.

        Usually assigned by the system. If specified, it will be
        allocated to the service if unused or else creation of the service will
        fail. Default is to auto-allocate a port if the ServiceType of this Service
        requires one.

        :default: - auto-allocate a port if the ServiceType of this Service requires one.

        :see: https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport
        '''
        result = self._values.get("node_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def protocol(self) -> typing.Optional[Protocol]:
        '''The IP protocol for this port.

        Supports "TCP", "UDP", and "SCTP". Default is TCP.

        :default: Protocol.TCP
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[Protocol], result)

    @builtins.property
    def target_port(self) -> typing.Optional[jsii.Number]:
        '''The port number the service will redirect to.

        :default: - The value of ``port`` will be used.
        '''
        result = self._values.get("target_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''The port number the service will bind to.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServicePort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.SshAuthSecretProps",
    jsii_struct_bases=[CommonSecretProps],
    name_mapping={
        "metadata": "metadata",
        "immutable": "immutable",
        "ssh_private_key": "sshPrivateKey",
    },
)
class SshAuthSecretProps(CommonSecretProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        immutable: typing.Optional[builtins.bool] = None,
        ssh_private_key: builtins.str,
    ) -> None:
        '''Options for ``SshAuthSecret``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param ssh_private_key: The SSH private key to use.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        self._values: typing.Dict[str, typing.Any] = {
            "ssh_private_key": ssh_private_key,
        }
        if metadata is not None:
            self._values["metadata"] = metadata
        if immutable is not None:
            self._values["immutable"] = immutable

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def immutable(self) -> typing.Optional[builtins.bool]:
        '''If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified).

        If not set to true, the field can be modified at any time.

        :default: false
        '''
        result = self._values.get("immutable")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ssh_private_key(self) -> builtins.str:
        '''The SSH private key to use.'''
        result = self._values.get("ssh_private_key")
        assert result is not None, "Required property 'ssh_private_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SshAuthSecretProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.TlsSecretProps",
    jsii_struct_bases=[CommonSecretProps],
    name_mapping={
        "metadata": "metadata",
        "immutable": "immutable",
        "tls_cert": "tlsCert",
        "tls_key": "tlsKey",
    },
)
class TlsSecretProps(CommonSecretProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        immutable: typing.Optional[builtins.bool] = None,
        tls_cert: builtins.str,
        tls_key: builtins.str,
    ) -> None:
        '''Options for ``TlsSecret``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param tls_cert: The TLS cert.
        :param tls_key: The TLS key.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        self._values: typing.Dict[str, typing.Any] = {
            "tls_cert": tls_cert,
            "tls_key": tls_key,
        }
        if metadata is not None:
            self._values["metadata"] = metadata
        if immutable is not None:
            self._values["immutable"] = immutable

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def immutable(self) -> typing.Optional[builtins.bool]:
        '''If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified).

        If not set to true, the field can be modified at any time.

        :default: false
        '''
        result = self._values.get("immutable")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def tls_cert(self) -> builtins.str:
        '''The TLS cert.'''
        result = self._values.get("tls_cert")
        assert result is not None, "Required property 'tls_cert' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tls_key(self) -> builtins.str:
        '''The TLS key.'''
        result = self._values.get("tls_key")
        assert result is not None, "Required property 'tls_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TlsSecretProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AwsElasticBlockStorePersistentVolume(
    PersistentVolume,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-21.AwsElasticBlockStorePersistentVolume",
):
    '''Represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod.

    :see: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        volume_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[builtins.bool] = None,
        access_modes: typing.Optional[typing.Sequence[PersistentVolumeAccessMode]] = None,
        claim: typing.Optional[IPersistentVolumeClaim] = None,
        mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        reclaim_policy: typing.Optional[PersistentVolumeReclaimPolicy] = None,
        storage: typing.Optional[cdk8s.Size] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        volume_mode: typing.Optional[PersistentVolumeMode] = None,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param volume_id: Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Default: 'ext4'
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). Default: - No partition.
        :param read_only: Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". Default: false
        :param access_modes: Contains all ways the volume can be mounted. Default: - No access modes.
        :param claim: Part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. Default: - Not bound to a specific claim.
        :param mount_options: A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. Default: - No options.
        :param reclaim_policy: When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource. The reclaim policy tells the cluster what to do with the volume after it has been released of its claim. Default: PersistentVolumeReclaimPolicy.RETAIN
        :param storage: What is the storage capacity of this volume. Default: - No specified.
        :param storage_class_name: Name of StorageClass to which this persistent volume belongs. Default: - Volume does not belong to any storage class.
        :param volume_mode: Defines what type of volume is required by the claim. Default: VolumeMode.FILE_SYSTEM
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        props = AwsElasticBlockStorePersistentVolumeProps(
            volume_id=volume_id,
            fs_type=fs_type,
            partition=partition,
            read_only=read_only,
            access_modes=access_modes,
            claim=claim,
            mount_options=mount_options,
            reclaim_policy=reclaim_policy,
            storage=storage,
            storage_class_name=storage_class_name,
            volume_mode=volume_mode,
            metadata=metadata,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        '''File system type of this volume.'''
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> builtins.bool:
        '''Whether or not it is mounted as a read-only volume.'''
        return typing.cast(builtins.bool, jsii.get(self, "readOnly"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="volumeId")
    def volume_id(self) -> builtins.str:
        '''Volume id of this volume.'''
        return typing.cast(builtins.str, jsii.get(self, "volumeId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="partition")
    def partition(self) -> typing.Optional[jsii.Number]:
        '''Partition of this volume.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "partition"))


@jsii.data_type(
    jsii_type="cdk8s-plus-21.AwsElasticBlockStorePersistentVolumeProps",
    jsii_struct_bases=[PersistentVolumeProps],
    name_mapping={
        "metadata": "metadata",
        "access_modes": "accessModes",
        "claim": "claim",
        "mount_options": "mountOptions",
        "reclaim_policy": "reclaimPolicy",
        "storage": "storage",
        "storage_class_name": "storageClassName",
        "volume_mode": "volumeMode",
        "volume_id": "volumeId",
        "fs_type": "fsType",
        "partition": "partition",
        "read_only": "readOnly",
    },
)
class AwsElasticBlockStorePersistentVolumeProps(PersistentVolumeProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        access_modes: typing.Optional[typing.Sequence[PersistentVolumeAccessMode]] = None,
        claim: typing.Optional[IPersistentVolumeClaim] = None,
        mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        reclaim_policy: typing.Optional[PersistentVolumeReclaimPolicy] = None,
        storage: typing.Optional[cdk8s.Size] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        volume_mode: typing.Optional[PersistentVolumeMode] = None,
        volume_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties for ``AwsElasticBlockStorePersistentVolume``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param access_modes: Contains all ways the volume can be mounted. Default: - No access modes.
        :param claim: Part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. Default: - Not bound to a specific claim.
        :param mount_options: A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. Default: - No options.
        :param reclaim_policy: When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource. The reclaim policy tells the cluster what to do with the volume after it has been released of its claim. Default: PersistentVolumeReclaimPolicy.RETAIN
        :param storage: What is the storage capacity of this volume. Default: - No specified.
        :param storage_class_name: Name of StorageClass to which this persistent volume belongs. Default: - Volume does not belong to any storage class.
        :param volume_mode: Defines what type of volume is required by the claim. Default: VolumeMode.FILE_SYSTEM
        :param volume_id: Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Default: 'ext4'
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). Default: - No partition.
        :param read_only: Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". Default: false
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        self._values: typing.Dict[str, typing.Any] = {
            "volume_id": volume_id,
        }
        if metadata is not None:
            self._values["metadata"] = metadata
        if access_modes is not None:
            self._values["access_modes"] = access_modes
        if claim is not None:
            self._values["claim"] = claim
        if mount_options is not None:
            self._values["mount_options"] = mount_options
        if reclaim_policy is not None:
            self._values["reclaim_policy"] = reclaim_policy
        if storage is not None:
            self._values["storage"] = storage
        if storage_class_name is not None:
            self._values["storage_class_name"] = storage_class_name
        if volume_mode is not None:
            self._values["volume_mode"] = volume_mode
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if partition is not None:
            self._values["partition"] = partition
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def access_modes(self) -> typing.Optional[typing.List[PersistentVolumeAccessMode]]:
        '''Contains all ways the volume can be mounted.

        :default: - No access modes.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes
        '''
        result = self._values.get("access_modes")
        return typing.cast(typing.Optional[typing.List[PersistentVolumeAccessMode]], result)

    @builtins.property
    def claim(self) -> typing.Optional[IPersistentVolumeClaim]:
        '''Part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim.

        Expected to be non-nil when bound.

        :default: - Not bound to a specific claim.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding
        '''
        result = self._values.get("claim")
        return typing.cast(typing.Optional[IPersistentVolumeClaim], result)

    @builtins.property
    def mount_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid.

        :default: - No options.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options
        '''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def reclaim_policy(self) -> typing.Optional[PersistentVolumeReclaimPolicy]:
        '''When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource.

        The reclaim policy tells the cluster what to do with
        the volume after it has been released of its claim.

        :default: PersistentVolumeReclaimPolicy.RETAIN

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming
        '''
        result = self._values.get("reclaim_policy")
        return typing.cast(typing.Optional[PersistentVolumeReclaimPolicy], result)

    @builtins.property
    def storage(self) -> typing.Optional[cdk8s.Size]:
        '''What is the storage capacity of this volume.

        :default: - No specified.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources
        '''
        result = self._values.get("storage")
        return typing.cast(typing.Optional[cdk8s.Size], result)

    @builtins.property
    def storage_class_name(self) -> typing.Optional[builtins.str]:
        '''Name of StorageClass to which this persistent volume belongs.

        :default: - Volume does not belong to any storage class.
        '''
        result = self._values.get("storage_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_mode(self) -> typing.Optional[PersistentVolumeMode]:
        '''Defines what type of volume is required by the claim.

        :default: VolumeMode.FILE_SYSTEM
        '''
        result = self._values.get("volume_mode")
        return typing.cast(typing.Optional[PersistentVolumeMode], result)

    @builtins.property
    def volume_id(self) -> builtins.str:
        '''Unique ID of the persistent disk resource in AWS (Amazon EBS volume).

        More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore

        :see: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
        '''
        result = self._values.get("volume_id")
        assert result is not None, "Required property 'volume_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type of the volume that you want to mount.

        Tip: Ensure that the filesystem type is supported by the host operating system.

        :default: 'ext4'

        :see: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition(self) -> typing.Optional[jsii.Number]:
        '''The partition in the volume that you want to mount.

        If omitted, the default is to mount by volume name.
        Examples: For volume /dev/sda1, you specify the partition as "1".
        Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).

        :default: - No partition.
        '''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_only(self) -> typing.Optional[builtins.bool]:
        '''Specify "true" to force and set the ReadOnly property in VolumeMounts to "true".

        :default: false

        :see: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsElasticBlockStorePersistentVolumeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AzureDiskPersistentVolume(
    PersistentVolume,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-21.AzureDiskPersistentVolume",
):
    '''AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        disk_name: builtins.str,
        disk_uri: builtins.str,
        caching_mode: typing.Optional[AzureDiskPersistentVolumeCachingMode] = None,
        fs_type: typing.Optional[builtins.str] = None,
        kind: typing.Optional[AzureDiskPersistentVolumeKind] = None,
        read_only: typing.Optional[builtins.bool] = None,
        access_modes: typing.Optional[typing.Sequence[PersistentVolumeAccessMode]] = None,
        claim: typing.Optional[IPersistentVolumeClaim] = None,
        mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        reclaim_policy: typing.Optional[PersistentVolumeReclaimPolicy] = None,
        storage: typing.Optional[cdk8s.Size] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        volume_mode: typing.Optional[PersistentVolumeMode] = None,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param disk_name: The Name of the data disk in the blob storage.
        :param disk_uri: The URI the data disk in the blob storage.
        :param caching_mode: Host Caching mode. Default: - AzureDiskPersistentVolumeCachingMode.NONE.
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Default: 'ext4'
        :param kind: Kind of disk. Default: AzureDiskPersistentVolumeKind.SHARED
        :param read_only: Force the ReadOnly setting in VolumeMounts. Default: false
        :param access_modes: Contains all ways the volume can be mounted. Default: - No access modes.
        :param claim: Part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. Default: - Not bound to a specific claim.
        :param mount_options: A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. Default: - No options.
        :param reclaim_policy: When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource. The reclaim policy tells the cluster what to do with the volume after it has been released of its claim. Default: PersistentVolumeReclaimPolicy.RETAIN
        :param storage: What is the storage capacity of this volume. Default: - No specified.
        :param storage_class_name: Name of StorageClass to which this persistent volume belongs. Default: - Volume does not belong to any storage class.
        :param volume_mode: Defines what type of volume is required by the claim. Default: VolumeMode.FILE_SYSTEM
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        props = AzureDiskPersistentVolumeProps(
            disk_name=disk_name,
            disk_uri=disk_uri,
            caching_mode=caching_mode,
            fs_type=fs_type,
            kind=kind,
            read_only=read_only,
            access_modes=access_modes,
            claim=claim,
            mount_options=mount_options,
            reclaim_policy=reclaim_policy,
            storage=storage,
            storage_class_name=storage_class_name,
            volume_mode=volume_mode,
            metadata=metadata,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cachingMode")
    def caching_mode(self) -> AzureDiskPersistentVolumeCachingMode:
        '''Caching mode of this volume.'''
        return typing.cast(AzureDiskPersistentVolumeCachingMode, jsii.get(self, "cachingMode"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="diskName")
    def disk_name(self) -> builtins.str:
        '''Disk name of this volume.'''
        return typing.cast(builtins.str, jsii.get(self, "diskName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="diskUri")
    def disk_uri(self) -> builtins.str:
        '''Disk URI of this volume.'''
        return typing.cast(builtins.str, jsii.get(self, "diskUri"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        '''File system type of this volume.'''
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kind")
    def kind(self) -> AzureDiskPersistentVolumeKind:
        '''Azure kind of this volume.'''
        return typing.cast(AzureDiskPersistentVolumeKind, jsii.get(self, "kind"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> builtins.bool:
        '''Whether or not it is mounted as a read-only volume.'''
        return typing.cast(builtins.bool, jsii.get(self, "readOnly"))


@jsii.data_type(
    jsii_type="cdk8s-plus-21.AzureDiskPersistentVolumeProps",
    jsii_struct_bases=[PersistentVolumeProps],
    name_mapping={
        "metadata": "metadata",
        "access_modes": "accessModes",
        "claim": "claim",
        "mount_options": "mountOptions",
        "reclaim_policy": "reclaimPolicy",
        "storage": "storage",
        "storage_class_name": "storageClassName",
        "volume_mode": "volumeMode",
        "disk_name": "diskName",
        "disk_uri": "diskUri",
        "caching_mode": "cachingMode",
        "fs_type": "fsType",
        "kind": "kind",
        "read_only": "readOnly",
    },
)
class AzureDiskPersistentVolumeProps(PersistentVolumeProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        access_modes: typing.Optional[typing.Sequence[PersistentVolumeAccessMode]] = None,
        claim: typing.Optional[IPersistentVolumeClaim] = None,
        mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        reclaim_policy: typing.Optional[PersistentVolumeReclaimPolicy] = None,
        storage: typing.Optional[cdk8s.Size] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        volume_mode: typing.Optional[PersistentVolumeMode] = None,
        disk_name: builtins.str,
        disk_uri: builtins.str,
        caching_mode: typing.Optional[AzureDiskPersistentVolumeCachingMode] = None,
        fs_type: typing.Optional[builtins.str] = None,
        kind: typing.Optional[AzureDiskPersistentVolumeKind] = None,
        read_only: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties for ``AzureDiskPersistentVolume``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param access_modes: Contains all ways the volume can be mounted. Default: - No access modes.
        :param claim: Part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. Default: - Not bound to a specific claim.
        :param mount_options: A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. Default: - No options.
        :param reclaim_policy: When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource. The reclaim policy tells the cluster what to do with the volume after it has been released of its claim. Default: PersistentVolumeReclaimPolicy.RETAIN
        :param storage: What is the storage capacity of this volume. Default: - No specified.
        :param storage_class_name: Name of StorageClass to which this persistent volume belongs. Default: - Volume does not belong to any storage class.
        :param volume_mode: Defines what type of volume is required by the claim. Default: VolumeMode.FILE_SYSTEM
        :param disk_name: The Name of the data disk in the blob storage.
        :param disk_uri: The URI the data disk in the blob storage.
        :param caching_mode: Host Caching mode. Default: - AzureDiskPersistentVolumeCachingMode.NONE.
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Default: 'ext4'
        :param kind: Kind of disk. Default: AzureDiskPersistentVolumeKind.SHARED
        :param read_only: Force the ReadOnly setting in VolumeMounts. Default: false
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        self._values: typing.Dict[str, typing.Any] = {
            "disk_name": disk_name,
            "disk_uri": disk_uri,
        }
        if metadata is not None:
            self._values["metadata"] = metadata
        if access_modes is not None:
            self._values["access_modes"] = access_modes
        if claim is not None:
            self._values["claim"] = claim
        if mount_options is not None:
            self._values["mount_options"] = mount_options
        if reclaim_policy is not None:
            self._values["reclaim_policy"] = reclaim_policy
        if storage is not None:
            self._values["storage"] = storage
        if storage_class_name is not None:
            self._values["storage_class_name"] = storage_class_name
        if volume_mode is not None:
            self._values["volume_mode"] = volume_mode
        if caching_mode is not None:
            self._values["caching_mode"] = caching_mode
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if kind is not None:
            self._values["kind"] = kind
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def access_modes(self) -> typing.Optional[typing.List[PersistentVolumeAccessMode]]:
        '''Contains all ways the volume can be mounted.

        :default: - No access modes.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes
        '''
        result = self._values.get("access_modes")
        return typing.cast(typing.Optional[typing.List[PersistentVolumeAccessMode]], result)

    @builtins.property
    def claim(self) -> typing.Optional[IPersistentVolumeClaim]:
        '''Part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim.

        Expected to be non-nil when bound.

        :default: - Not bound to a specific claim.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding
        '''
        result = self._values.get("claim")
        return typing.cast(typing.Optional[IPersistentVolumeClaim], result)

    @builtins.property
    def mount_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid.

        :default: - No options.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options
        '''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def reclaim_policy(self) -> typing.Optional[PersistentVolumeReclaimPolicy]:
        '''When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource.

        The reclaim policy tells the cluster what to do with
        the volume after it has been released of its claim.

        :default: PersistentVolumeReclaimPolicy.RETAIN

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming
        '''
        result = self._values.get("reclaim_policy")
        return typing.cast(typing.Optional[PersistentVolumeReclaimPolicy], result)

    @builtins.property
    def storage(self) -> typing.Optional[cdk8s.Size]:
        '''What is the storage capacity of this volume.

        :default: - No specified.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources
        '''
        result = self._values.get("storage")
        return typing.cast(typing.Optional[cdk8s.Size], result)

    @builtins.property
    def storage_class_name(self) -> typing.Optional[builtins.str]:
        '''Name of StorageClass to which this persistent volume belongs.

        :default: - Volume does not belong to any storage class.
        '''
        result = self._values.get("storage_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_mode(self) -> typing.Optional[PersistentVolumeMode]:
        '''Defines what type of volume is required by the claim.

        :default: VolumeMode.FILE_SYSTEM
        '''
        result = self._values.get("volume_mode")
        return typing.cast(typing.Optional[PersistentVolumeMode], result)

    @builtins.property
    def disk_name(self) -> builtins.str:
        '''The Name of the data disk in the blob storage.'''
        result = self._values.get("disk_name")
        assert result is not None, "Required property 'disk_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disk_uri(self) -> builtins.str:
        '''The URI the data disk in the blob storage.'''
        result = self._values.get("disk_uri")
        assert result is not None, "Required property 'disk_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def caching_mode(self) -> typing.Optional[AzureDiskPersistentVolumeCachingMode]:
        '''Host Caching mode.

        :default: - AzureDiskPersistentVolumeCachingMode.NONE.
        '''
        result = self._values.get("caching_mode")
        return typing.cast(typing.Optional[AzureDiskPersistentVolumeCachingMode], result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system.

        :default: 'ext4'
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[AzureDiskPersistentVolumeKind]:
        '''Kind of disk.

        :default: AzureDiskPersistentVolumeKind.SHARED
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[AzureDiskPersistentVolumeKind], result)

    @builtins.property
    def read_only(self) -> typing.Optional[builtins.bool]:
        '''Force the ReadOnly setting in VolumeMounts.

        :default: false
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AzureDiskPersistentVolumeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-plus-21.BasicAuthSecretProps",
    jsii_struct_bases=[CommonSecretProps],
    name_mapping={
        "metadata": "metadata",
        "immutable": "immutable",
        "password": "password",
        "username": "username",
    },
)
class BasicAuthSecretProps(CommonSecretProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        immutable: typing.Optional[builtins.bool] = None,
        password: builtins.str,
        username: builtins.str,
    ) -> None:
        '''Options for ``BasicAuthSecret``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param immutable: If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param password: The password or token for authentication.
        :param username: The user name for authentication.
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        self._values: typing.Dict[str, typing.Any] = {
            "password": password,
            "username": username,
        }
        if metadata is not None:
            self._values["metadata"] = metadata
        if immutable is not None:
            self._values["immutable"] = immutable

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def immutable(self) -> typing.Optional[builtins.bool]:
        '''If set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified).

        If not set to true, the field can be modified at any time.

        :default: false
        '''
        result = self._values.get("immutable")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def password(self) -> builtins.str:
        '''The password or token for authentication.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''The user name for authentication.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BasicAuthSecretProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IConfigMap)
class ConfigMap(Resource, metaclass=jsii.JSIIMeta, jsii_type="cdk8s-plus-21.ConfigMap"):
    '''ConfigMap holds configuration data for pods to consume.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        binary_data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        immutable: typing.Optional[builtins.bool] = None,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param binary_data: BinaryData contains the binary data. Each key must consist of alphanumeric characters, '-', '_' or '.'. BinaryData can contain byte sequences that are not in the UTF-8 range. The keys stored in BinaryData must not overlap with the ones in the Data field, this is enforced during validation process. You can also add binary data using ``configMap.addBinaryData()``.
        :param data: Data contains the configuration data. Each key must consist of alphanumeric characters, '-', '_' or '.'. Values with non-UTF-8 byte sequences must use the BinaryData field. The keys stored in Data must not overlap with the keys in the BinaryData field, this is enforced during validation process. You can also add data using ``configMap.addData()``.
        :param immutable: If set to true, ensures that data stored in the ConfigMap cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Default: false
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        props = ConfigMapProps(
            binary_data=binary_data, data=data, immutable=immutable, metadata=metadata
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromConfigMapName") # type: ignore[misc]
    @builtins.classmethod
    def from_config_map_name(cls, name: builtins.str) -> IConfigMap:
        '''Represents a ConfigMap created elsewhere.

        :param name: The name of the config map to import.
        '''
        return typing.cast(IConfigMap, jsii.sinvoke(cls, "fromConfigMapName", [name]))

    @jsii.member(jsii_name="addBinaryData")
    def add_binary_data(self, key: builtins.str, value: builtins.str) -> None:
        '''Adds a binary data entry to the config map.

        BinaryData can contain byte
        sequences that are not in the UTF-8 range.

        :param key: The key.
        :param value: The value.

        :throws: if there is either a ``data`` or ``binaryData`` entry with the same key
        '''
        return typing.cast(None, jsii.invoke(self, "addBinaryData", [key, value]))

    @jsii.member(jsii_name="addData")
    def add_data(self, key: builtins.str, value: builtins.str) -> None:
        '''Adds a data entry to the config map.

        :param key: The key.
        :param value: The value.

        :throws: if there is either a ``data`` or ``binaryData`` entry with the same key
        '''
        return typing.cast(None, jsii.invoke(self, "addData", [key, value]))

    @jsii.member(jsii_name="addDirectory")
    def add_directory(
        self,
        local_dir: builtins.str,
        *,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        key_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Adds a directory to the ConfigMap.

        :param local_dir: A path to a local directory.
        :param exclude: Glob patterns to exclude when adding files. Default: - include all files
        :param key_prefix: A prefix to add to all keys in the config map. Default: ""
        '''
        options = AddDirectoryOptions(exclude=exclude, key_prefix=key_prefix)

        return typing.cast(None, jsii.invoke(self, "addDirectory", [local_dir, options]))

    @jsii.member(jsii_name="addFile")
    def add_file(
        self,
        local_file: builtins.str,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Adds a file to the ConfigMap.

        :param local_file: The path to the local file.
        :param key: The ConfigMap key (default to the file name).
        '''
        return typing.cast(None, jsii.invoke(self, "addFile", [local_file, key]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="apiObject")
    def _api_object(self) -> cdk8s.ApiObject:
        '''The underlying cdk8s API object.

        :see: base.Resource.apiObject
        '''
        return typing.cast(cdk8s.ApiObject, jsii.get(self, "apiObject"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="binaryData")
    def binary_data(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''The binary data associated with this config map.

        Returns a copy. To add data records, use ``addBinaryData()`` or ``addData()``.
        '''
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "binaryData"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="data")
    def data(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''The data associated with this config map.

        Returns an copy. To add data records, use ``addData()`` or ``addBinaryData()``.
        '''
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "data"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="immutable")
    def immutable(self) -> builtins.bool:
        '''Whether or not this config map is immutable.'''
        return typing.cast(builtins.bool, jsii.get(self, "immutable"))


class GCEPersistentDiskPersistentVolume(
    PersistentVolume,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-plus-21.GCEPersistentDiskPersistentVolume",
):
    '''GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod.

    Provisioned by an admin.

    :see: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        pd_name: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[builtins.bool] = None,
        access_modes: typing.Optional[typing.Sequence[PersistentVolumeAccessMode]] = None,
        claim: typing.Optional[IPersistentVolumeClaim] = None,
        mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        reclaim_policy: typing.Optional[PersistentVolumeReclaimPolicy] = None,
        storage: typing.Optional[cdk8s.Size] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        volume_mode: typing.Optional[PersistentVolumeMode] = None,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param pd_name: Unique name of the PD resource in GCE. Used to identify the disk in GCE.
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Default: 'ext4'
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). Default: - No partition.
        :param read_only: Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". Default: false
        :param access_modes: Contains all ways the volume can be mounted. Default: - No access modes.
        :param claim: Part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. Default: - Not bound to a specific claim.
        :param mount_options: A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. Default: - No options.
        :param reclaim_policy: When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource. The reclaim policy tells the cluster what to do with the volume after it has been released of its claim. Default: PersistentVolumeReclaimPolicy.RETAIN
        :param storage: What is the storage capacity of this volume. Default: - No specified.
        :param storage_class_name: Name of StorageClass to which this persistent volume belongs. Default: - Volume does not belong to any storage class.
        :param volume_mode: Defines what type of volume is required by the claim. Default: VolumeMode.FILE_SYSTEM
        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        '''
        props = GCEPersistentDiskPersistentVolumeProps(
            pd_name=pd_name,
            fs_type=fs_type,
            partition=partition,
            read_only=read_only,
            access_modes=access_modes,
            claim=claim,
            mount_options=mount_options,
            reclaim_policy=reclaim_policy,
            storage=storage,
            storage_class_name=storage_class_name,
            volume_mode=volume_mode,
            metadata=metadata,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        '''File system type of this volume.'''
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pdName")
    def pd_name(self) -> builtins.str:
        '''PD resource in GCE of this volume.'''
        return typing.cast(builtins.str, jsii.get(self, "pdName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> builtins.bool:
        '''Whether or not it is mounted as a read-only volume.'''
        return typing.cast(builtins.bool, jsii.get(self, "readOnly"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="partition")
    def partition(self) -> typing.Optional[jsii.Number]:
        '''Partition of this volume.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "partition"))


@jsii.data_type(
    jsii_type="cdk8s-plus-21.GCEPersistentDiskPersistentVolumeProps",
    jsii_struct_bases=[PersistentVolumeProps],
    name_mapping={
        "metadata": "metadata",
        "access_modes": "accessModes",
        "claim": "claim",
        "mount_options": "mountOptions",
        "reclaim_policy": "reclaimPolicy",
        "storage": "storage",
        "storage_class_name": "storageClassName",
        "volume_mode": "volumeMode",
        "pd_name": "pdName",
        "fs_type": "fsType",
        "partition": "partition",
        "read_only": "readOnly",
    },
)
class GCEPersistentDiskPersistentVolumeProps(PersistentVolumeProps):
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        access_modes: typing.Optional[typing.Sequence[PersistentVolumeAccessMode]] = None,
        claim: typing.Optional[IPersistentVolumeClaim] = None,
        mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        reclaim_policy: typing.Optional[PersistentVolumeReclaimPolicy] = None,
        storage: typing.Optional[cdk8s.Size] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        volume_mode: typing.Optional[PersistentVolumeMode] = None,
        pd_name: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties for ``GCEPersistentDiskPersistentVolume``.

        :param metadata: Metadata that all persisted resources must have, which includes all objects users must create.
        :param access_modes: Contains all ways the volume can be mounted. Default: - No access modes.
        :param claim: Part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. Default: - Not bound to a specific claim.
        :param mount_options: A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. Default: - No options.
        :param reclaim_policy: When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource. The reclaim policy tells the cluster what to do with the volume after it has been released of its claim. Default: PersistentVolumeReclaimPolicy.RETAIN
        :param storage: What is the storage capacity of this volume. Default: - No specified.
        :param storage_class_name: Name of StorageClass to which this persistent volume belongs. Default: - Volume does not belong to any storage class.
        :param volume_mode: Defines what type of volume is required by the claim. Default: VolumeMode.FILE_SYSTEM
        :param pd_name: Unique name of the PD resource in GCE. Used to identify the disk in GCE.
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Default: 'ext4'
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). Default: - No partition.
        :param read_only: Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". Default: false
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        self._values: typing.Dict[str, typing.Any] = {
            "pd_name": pd_name,
        }
        if metadata is not None:
            self._values["metadata"] = metadata
        if access_modes is not None:
            self._values["access_modes"] = access_modes
        if claim is not None:
            self._values["claim"] = claim
        if mount_options is not None:
            self._values["mount_options"] = mount_options
        if reclaim_policy is not None:
            self._values["reclaim_policy"] = reclaim_policy
        if storage is not None:
            self._values["storage"] = storage
        if storage_class_name is not None:
            self._values["storage_class_name"] = storage_class_name
        if volume_mode is not None:
            self._values["volume_mode"] = volume_mode
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if partition is not None:
            self._values["partition"] = partition
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''Metadata that all persisted resources must have, which includes all objects users must create.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def access_modes(self) -> typing.Optional[typing.List[PersistentVolumeAccessMode]]:
        '''Contains all ways the volume can be mounted.

        :default: - No access modes.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes
        '''
        result = self._values.get("access_modes")
        return typing.cast(typing.Optional[typing.List[PersistentVolumeAccessMode]], result)

    @builtins.property
    def claim(self) -> typing.Optional[IPersistentVolumeClaim]:
        '''Part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim.

        Expected to be non-nil when bound.

        :default: - Not bound to a specific claim.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding
        '''
        result = self._values.get("claim")
        return typing.cast(typing.Optional[IPersistentVolumeClaim], result)

    @builtins.property
    def mount_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid.

        :default: - No options.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options
        '''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def reclaim_policy(self) -> typing.Optional[PersistentVolumeReclaimPolicy]:
        '''When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource.

        The reclaim policy tells the cluster what to do with
        the volume after it has been released of its claim.

        :default: PersistentVolumeReclaimPolicy.RETAIN

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming
        '''
        result = self._values.get("reclaim_policy")
        return typing.cast(typing.Optional[PersistentVolumeReclaimPolicy], result)

    @builtins.property
    def storage(self) -> typing.Optional[cdk8s.Size]:
        '''What is the storage capacity of this volume.

        :default: - No specified.

        :see: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources
        '''
        result = self._values.get("storage")
        return typing.cast(typing.Optional[cdk8s.Size], result)

    @builtins.property
    def storage_class_name(self) -> typing.Optional[builtins.str]:
        '''Name of StorageClass to which this persistent volume belongs.

        :default: - Volume does not belong to any storage class.
        '''
        result = self._values.get("storage_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_mode(self) -> typing.Optional[PersistentVolumeMode]:
        '''Defines what type of volume is required by the claim.

        :default: VolumeMode.FILE_SYSTEM
        '''
        result = self._values.get("volume_mode")
        return typing.cast(typing.Optional[PersistentVolumeMode], result)

    @builtins.property
    def pd_name(self) -> builtins.str:
        '''Unique name of the PD resource in GCE.

        Used to identify the disk in GCE.

        :see: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
        '''
        result = self._values.get("pd_name")
        assert result is not None, "Required property 'pd_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type of the volume that you want to mount.

        Tip: Ensure that the filesystem type is supported by the host operating system.

        :default: 'ext4'

        :see: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition(self) -> typing.Optional[jsii.Number]:
        '''The partition in the volume that you want to mount.

        If omitted, the default is to mount by volume name.
        Examples: For volume /dev/sda1, you specify the partition as "1".
        Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).

        :default: - No partition.
        '''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_only(self) -> typing.Optional[builtins.bool]:
        '''Specify "true" to force and set the ReadOnly property in VolumeMounts to "true".

        :default: false

        :see: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GCEPersistentDiskPersistentVolumeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AddDeploymentOptions",
    "AddDirectoryOptions",
    "AwsElasticBlockStorePersistentVolume",
    "AwsElasticBlockStorePersistentVolumeProps",
    "AwsElasticBlockStoreVolumeOptions",
    "AzureDiskPersistentVolume",
    "AzureDiskPersistentVolumeCachingMode",
    "AzureDiskPersistentVolumeKind",
    "AzureDiskPersistentVolumeProps",
    "AzureDiskVolumeOptions",
    "BasicAuthSecret",
    "BasicAuthSecretProps",
    "CommandProbeOptions",
    "CommonSecretProps",
    "ConfigMap",
    "ConfigMapProps",
    "ConfigMapVolumeOptions",
    "Container",
    "ContainerLifecycle",
    "ContainerProps",
    "ContainerSecurityContext",
    "ContainerSecurityContextProps",
    "Cpu",
    "CpuResources",
    "DaemonSet",
    "DaemonSetProps",
    "Deployment",
    "DeploymentProps",
    "DeploymentStrategy",
    "DeploymentStrategyRollingUpdateOptions",
    "DockerConfigSecret",
    "DockerConfigSecretProps",
    "EmptyDirMedium",
    "EmptyDirVolumeOptions",
    "EnvFieldPaths",
    "EnvValue",
    "EnvValueFromConfigMapOptions",
    "EnvValueFromFieldRefOptions",
    "EnvValueFromProcessOptions",
    "EnvValueFromResourceOptions",
    "EnvValueFromSecretOptions",
    "ExposeDeploymentViaIngressOptions",
    "ExposeDeploymentViaServiceOptions",
    "ExposeServiceViaIngressOptions",
    "FsGroupChangePolicy",
    "GCEPersistentDiskPersistentVolume",
    "GCEPersistentDiskPersistentVolumeProps",
    "GCEPersistentDiskVolumeOptions",
    "Handler",
    "HandlerFromHttpGetOptions",
    "HandlerFromTcpSocketOptions",
    "HostAlias",
    "HttpGetProbeOptions",
    "IConfigMap",
    "IPersistentVolume",
    "IPersistentVolumeClaim",
    "IPodSpec",
    "IPodTemplate",
    "IResource",
    "ISecret",
    "IServiceAccount",
    "IStorage",
    "ImagePullPolicy",
    "IngressV1Beta1",
    "IngressV1Beta1Backend",
    "IngressV1Beta1Props",
    "IngressV1Beta1Rule",
    "IngressV1Beta1Tls",
    "Job",
    "JobProps",
    "MemoryResources",
    "MountOptions",
    "MountPropagation",
    "PathMapping",
    "PercentOrAbsolute",
    "PersistentVolume",
    "PersistentVolumeAccessMode",
    "PersistentVolumeClaim",
    "PersistentVolumeClaimProps",
    "PersistentVolumeClaimVolumeOptions",
    "PersistentVolumeMode",
    "PersistentVolumeProps",
    "PersistentVolumeReclaimPolicy",
    "Pod",
    "PodManagementPolicy",
    "PodProps",
    "PodSecurityContext",
    "PodSecurityContextProps",
    "PodSpec",
    "PodSpecProps",
    "PodTemplate",
    "PodTemplateProps",
    "Probe",
    "ProbeOptions",
    "Protocol",
    "Resource",
    "ResourceFieldPaths",
    "ResourceProps",
    "Resources",
    "RestartPolicy",
    "Secret",
    "SecretProps",
    "SecretValue",
    "SecretVolumeOptions",
    "Service",
    "ServiceAccount",
    "ServiceAccountProps",
    "ServiceAccountTokenSecret",
    "ServiceAccountTokenSecretProps",
    "ServiceIngressV1BetaBackendOptions",
    "ServicePort",
    "ServicePortOptions",
    "ServiceProps",
    "ServiceType",
    "SshAuthSecret",
    "SshAuthSecretProps",
    "StatefulSet",
    "StatefulSetProps",
    "StatefulSetUpdateStrategy",
    "StatefulSetUpdateStrategyRollingUpdateOptions",
    "Sysctl",
    "TcpSocketProbeOptions",
    "TlsSecret",
    "TlsSecretProps",
    "Volume",
    "VolumeMount",
]

publication.publish()
