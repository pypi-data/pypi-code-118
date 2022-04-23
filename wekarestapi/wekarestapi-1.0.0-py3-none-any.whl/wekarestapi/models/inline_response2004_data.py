# coding: utf-8

"""
    @weka-api

    <div>The Weka system supports a RESTful API. This is useful when automating the interaction with the Weka system and when integrating it into your workflows or monitoring systems. The API is accessible at port 14000, via the /api/v2 URL, you can explore it via /api/v2/docs when accessing from the cluster (e.g. https://weka01:14000/api/v2/docs).<div style=\"margin-top: 15px;\">Note: Weka uses 64bit numbers. Please take special care when interacting with the API with different program languages (In JS for example you can use \"json-bigint\")</div></div>  # noqa: E501

    OpenAPI spec version: 3.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse2004Data(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'active_alerts_count': 'float',
        'activity': 'InlineResponse2004DataActivity',
        'block_upgrade_task': 'InlineResponse2004DataBlockUpgradeTask',
        'buckets': 'InlineResponse2004DataBuckets',
        'buckets_info': 'InlineResponse2004DataBucketsInfo',
        'capacity': 'InlineResponse2004DataCapacity',
        'cloud': 'InlineResponse2004DataCloud',
        'drives': 'InlineResponse2004DataDrives',
        'failure_domains_enabled': 'bool',
        'grim_reaper': 'InlineResponse2004DataGrimReaper',
        'guid': 'str',
        'hanging_ios': 'InlineResponse2004DataHangingIos',
        'hosts': 'InlineResponse2004DataHosts',
        'hot_spare': 'float',
        'init_stage': 'str',
        'init_stage_changed_time': 'str',
        'io_nodes': 'InlineResponse2004DataDrives',
        'io_status': 'str',
        'io_status_changed_time': 'str',
        'is_cluster': 'bool',
        'last_init_failure': 'str',
        'last_init_failure_code': 'str',
        'last_init_failure_time': 'str',
        'licensing': 'InlineResponse2004DataLicensing',
        'long_drive_grace_on_failure_secs': 'float',
        'name': 'str',
        'net': 'InlineResponse2004DataNet',
        'nodes': 'InlineResponse2004DataNodes',
        'overlay': 'InlineResponse2004DataOverlay',
        'rebuild': 'InlineResponse2004DataRebuild',
        'release': 'str',
        'release_hash': 'str',
        'scrubber_bytes_per_sec': 'float',
        'short_drive_grace_on_failure_secs': 'float',
        'start_io_starting_drives_grace_secs': 'float',
        'start_io_starting_io_nodes_grace_secs': 'float',
        'status': 'str',
        'stripe_data_drives': 'float',
        'stripe_protection_drives': 'float',
        'time': 'InlineResponse2004DataTime',
        'upgrade': 'str'
    }

    attribute_map = {
        'active_alerts_count': 'active_alerts_count',
        'activity': 'activity',
        'block_upgrade_task': 'block_upgrade_task',
        'buckets': 'buckets',
        'buckets_info': 'buckets_info',
        'capacity': 'capacity',
        'cloud': 'cloud',
        'drives': 'drives',
        'failure_domains_enabled': 'failure_domains_enabled',
        'grim_reaper': 'grim_reaper',
        'guid': 'guid',
        'hanging_ios': 'hanging_ios',
        'hosts': 'hosts',
        'hot_spare': 'hot_spare',
        'init_stage': 'init_stage',
        'init_stage_changed_time': 'init_stage_changed_time',
        'io_nodes': 'io_nodes',
        'io_status': 'io_status',
        'io_status_changed_time': 'io_status_changed_time',
        'is_cluster': 'is_cluster',
        'last_init_failure': 'last_init_failure',
        'last_init_failure_code': 'last_init_failure_code',
        'last_init_failure_time': 'last_init_failure_time',
        'licensing': 'licensing',
        'long_drive_grace_on_failure_secs': 'long_drive_grace_on_failure_secs',
        'name': 'name',
        'net': 'net',
        'nodes': 'nodes',
        'overlay': 'overlay',
        'rebuild': 'rebuild',
        'release': 'release',
        'release_hash': 'release_hash',
        'scrubber_bytes_per_sec': 'scrubber_bytes_per_sec',
        'short_drive_grace_on_failure_secs': 'short_drive_grace_on_failure_secs',
        'start_io_starting_drives_grace_secs': 'start_io_starting_drives_grace_secs',
        'start_io_starting_io_nodes_grace_secs': 'start_io_starting_io_nodes_grace_secs',
        'status': 'status',
        'stripe_data_drives': 'stripe_data_drives',
        'stripe_protection_drives': 'stripe_protection_drives',
        'time': 'time',
        'upgrade': 'upgrade'
    }

    def __init__(self, active_alerts_count=None, activity=None, block_upgrade_task=None, buckets=None, buckets_info=None, capacity=None, cloud=None, drives=None, failure_domains_enabled=None, grim_reaper=None, guid=None, hanging_ios=None, hosts=None, hot_spare=None, init_stage=None, init_stage_changed_time=None, io_nodes=None, io_status=None, io_status_changed_time=None, is_cluster=None, last_init_failure=None, last_init_failure_code=None, last_init_failure_time=None, licensing=None, long_drive_grace_on_failure_secs=None, name=None, net=None, nodes=None, overlay=None, rebuild=None, release=None, release_hash=None, scrubber_bytes_per_sec=None, short_drive_grace_on_failure_secs=None, start_io_starting_drives_grace_secs=None, start_io_starting_io_nodes_grace_secs=None, status=None, stripe_data_drives=None, stripe_protection_drives=None, time=None, upgrade=None):  # noqa: E501
        """InlineResponse2004Data - a model defined in Swagger"""  # noqa: E501
        self._active_alerts_count = None
        self._activity = None
        self._block_upgrade_task = None
        self._buckets = None
        self._buckets_info = None
        self._capacity = None
        self._cloud = None
        self._drives = None
        self._failure_domains_enabled = None
        self._grim_reaper = None
        self._guid = None
        self._hanging_ios = None
        self._hosts = None
        self._hot_spare = None
        self._init_stage = None
        self._init_stage_changed_time = None
        self._io_nodes = None
        self._io_status = None
        self._io_status_changed_time = None
        self._is_cluster = None
        self._last_init_failure = None
        self._last_init_failure_code = None
        self._last_init_failure_time = None
        self._licensing = None
        self._long_drive_grace_on_failure_secs = None
        self._name = None
        self._net = None
        self._nodes = None
        self._overlay = None
        self._rebuild = None
        self._release = None
        self._release_hash = None
        self._scrubber_bytes_per_sec = None
        self._short_drive_grace_on_failure_secs = None
        self._start_io_starting_drives_grace_secs = None
        self._start_io_starting_io_nodes_grace_secs = None
        self._status = None
        self._stripe_data_drives = None
        self._stripe_protection_drives = None
        self._time = None
        self._upgrade = None
        self.discriminator = None
        if active_alerts_count is not None:
            self.active_alerts_count = active_alerts_count
        if activity is not None:
            self.activity = activity
        if block_upgrade_task is not None:
            self.block_upgrade_task = block_upgrade_task
        if buckets is not None:
            self.buckets = buckets
        if buckets_info is not None:
            self.buckets_info = buckets_info
        if capacity is not None:
            self.capacity = capacity
        if cloud is not None:
            self.cloud = cloud
        if drives is not None:
            self.drives = drives
        if failure_domains_enabled is not None:
            self.failure_domains_enabled = failure_domains_enabled
        if grim_reaper is not None:
            self.grim_reaper = grim_reaper
        if guid is not None:
            self.guid = guid
        if hanging_ios is not None:
            self.hanging_ios = hanging_ios
        if hosts is not None:
            self.hosts = hosts
        if hot_spare is not None:
            self.hot_spare = hot_spare
        if init_stage is not None:
            self.init_stage = init_stage
        if init_stage_changed_time is not None:
            self.init_stage_changed_time = init_stage_changed_time
        if io_nodes is not None:
            self.io_nodes = io_nodes
        if io_status is not None:
            self.io_status = io_status
        if io_status_changed_time is not None:
            self.io_status_changed_time = io_status_changed_time
        if is_cluster is not None:
            self.is_cluster = is_cluster
        if last_init_failure is not None:
            self.last_init_failure = last_init_failure
        if last_init_failure_code is not None:
            self.last_init_failure_code = last_init_failure_code
        if last_init_failure_time is not None:
            self.last_init_failure_time = last_init_failure_time
        if licensing is not None:
            self.licensing = licensing
        if long_drive_grace_on_failure_secs is not None:
            self.long_drive_grace_on_failure_secs = long_drive_grace_on_failure_secs
        if name is not None:
            self.name = name
        if net is not None:
            self.net = net
        if nodes is not None:
            self.nodes = nodes
        if overlay is not None:
            self.overlay = overlay
        if rebuild is not None:
            self.rebuild = rebuild
        if release is not None:
            self.release = release
        if release_hash is not None:
            self.release_hash = release_hash
        if scrubber_bytes_per_sec is not None:
            self.scrubber_bytes_per_sec = scrubber_bytes_per_sec
        if short_drive_grace_on_failure_secs is not None:
            self.short_drive_grace_on_failure_secs = short_drive_grace_on_failure_secs
        if start_io_starting_drives_grace_secs is not None:
            self.start_io_starting_drives_grace_secs = start_io_starting_drives_grace_secs
        if start_io_starting_io_nodes_grace_secs is not None:
            self.start_io_starting_io_nodes_grace_secs = start_io_starting_io_nodes_grace_secs
        if status is not None:
            self.status = status
        if stripe_data_drives is not None:
            self.stripe_data_drives = stripe_data_drives
        if stripe_protection_drives is not None:
            self.stripe_protection_drives = stripe_protection_drives
        if time is not None:
            self.time = time
        if upgrade is not None:
            self.upgrade = upgrade

    @property
    def active_alerts_count(self):
        """Gets the active_alerts_count of this InlineResponse2004Data.  # noqa: E501


        :return: The active_alerts_count of this InlineResponse2004Data.  # noqa: E501
        :rtype: float
        """
        return self._active_alerts_count

    @active_alerts_count.setter
    def active_alerts_count(self, active_alerts_count):
        """Sets the active_alerts_count of this InlineResponse2004Data.


        :param active_alerts_count: The active_alerts_count of this InlineResponse2004Data.  # noqa: E501
        :type: float
        """

        self._active_alerts_count = active_alerts_count

    @property
    def activity(self):
        """Gets the activity of this InlineResponse2004Data.  # noqa: E501


        :return: The activity of this InlineResponse2004Data.  # noqa: E501
        :rtype: InlineResponse2004DataActivity
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this InlineResponse2004Data.


        :param activity: The activity of this InlineResponse2004Data.  # noqa: E501
        :type: InlineResponse2004DataActivity
        """

        self._activity = activity

    @property
    def block_upgrade_task(self):
        """Gets the block_upgrade_task of this InlineResponse2004Data.  # noqa: E501


        :return: The block_upgrade_task of this InlineResponse2004Data.  # noqa: E501
        :rtype: InlineResponse2004DataBlockUpgradeTask
        """
        return self._block_upgrade_task

    @block_upgrade_task.setter
    def block_upgrade_task(self, block_upgrade_task):
        """Sets the block_upgrade_task of this InlineResponse2004Data.


        :param block_upgrade_task: The block_upgrade_task of this InlineResponse2004Data.  # noqa: E501
        :type: InlineResponse2004DataBlockUpgradeTask
        """

        self._block_upgrade_task = block_upgrade_task

    @property
    def buckets(self):
        """Gets the buckets of this InlineResponse2004Data.  # noqa: E501


        :return: The buckets of this InlineResponse2004Data.  # noqa: E501
        :rtype: InlineResponse2004DataBuckets
        """
        return self._buckets

    @buckets.setter
    def buckets(self, buckets):
        """Sets the buckets of this InlineResponse2004Data.


        :param buckets: The buckets of this InlineResponse2004Data.  # noqa: E501
        :type: InlineResponse2004DataBuckets
        """

        self._buckets = buckets

    @property
    def buckets_info(self):
        """Gets the buckets_info of this InlineResponse2004Data.  # noqa: E501


        :return: The buckets_info of this InlineResponse2004Data.  # noqa: E501
        :rtype: InlineResponse2004DataBucketsInfo
        """
        return self._buckets_info

    @buckets_info.setter
    def buckets_info(self, buckets_info):
        """Sets the buckets_info of this InlineResponse2004Data.


        :param buckets_info: The buckets_info of this InlineResponse2004Data.  # noqa: E501
        :type: InlineResponse2004DataBucketsInfo
        """

        self._buckets_info = buckets_info

    @property
    def capacity(self):
        """Gets the capacity of this InlineResponse2004Data.  # noqa: E501


        :return: The capacity of this InlineResponse2004Data.  # noqa: E501
        :rtype: InlineResponse2004DataCapacity
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this InlineResponse2004Data.


        :param capacity: The capacity of this InlineResponse2004Data.  # noqa: E501
        :type: InlineResponse2004DataCapacity
        """

        self._capacity = capacity

    @property
    def cloud(self):
        """Gets the cloud of this InlineResponse2004Data.  # noqa: E501


        :return: The cloud of this InlineResponse2004Data.  # noqa: E501
        :rtype: InlineResponse2004DataCloud
        """
        return self._cloud

    @cloud.setter
    def cloud(self, cloud):
        """Sets the cloud of this InlineResponse2004Data.


        :param cloud: The cloud of this InlineResponse2004Data.  # noqa: E501
        :type: InlineResponse2004DataCloud
        """

        self._cloud = cloud

    @property
    def drives(self):
        """Gets the drives of this InlineResponse2004Data.  # noqa: E501


        :return: The drives of this InlineResponse2004Data.  # noqa: E501
        :rtype: InlineResponse2004DataDrives
        """
        return self._drives

    @drives.setter
    def drives(self, drives):
        """Sets the drives of this InlineResponse2004Data.


        :param drives: The drives of this InlineResponse2004Data.  # noqa: E501
        :type: InlineResponse2004DataDrives
        """

        self._drives = drives

    @property
    def failure_domains_enabled(self):
        """Gets the failure_domains_enabled of this InlineResponse2004Data.  # noqa: E501


        :return: The failure_domains_enabled of this InlineResponse2004Data.  # noqa: E501
        :rtype: bool
        """
        return self._failure_domains_enabled

    @failure_domains_enabled.setter
    def failure_domains_enabled(self, failure_domains_enabled):
        """Sets the failure_domains_enabled of this InlineResponse2004Data.


        :param failure_domains_enabled: The failure_domains_enabled of this InlineResponse2004Data.  # noqa: E501
        :type: bool
        """

        self._failure_domains_enabled = failure_domains_enabled

    @property
    def grim_reaper(self):
        """Gets the grim_reaper of this InlineResponse2004Data.  # noqa: E501


        :return: The grim_reaper of this InlineResponse2004Data.  # noqa: E501
        :rtype: InlineResponse2004DataGrimReaper
        """
        return self._grim_reaper

    @grim_reaper.setter
    def grim_reaper(self, grim_reaper):
        """Sets the grim_reaper of this InlineResponse2004Data.


        :param grim_reaper: The grim_reaper of this InlineResponse2004Data.  # noqa: E501
        :type: InlineResponse2004DataGrimReaper
        """

        self._grim_reaper = grim_reaper

    @property
    def guid(self):
        """Gets the guid of this InlineResponse2004Data.  # noqa: E501


        :return: The guid of this InlineResponse2004Data.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this InlineResponse2004Data.


        :param guid: The guid of this InlineResponse2004Data.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def hanging_ios(self):
        """Gets the hanging_ios of this InlineResponse2004Data.  # noqa: E501


        :return: The hanging_ios of this InlineResponse2004Data.  # noqa: E501
        :rtype: InlineResponse2004DataHangingIos
        """
        return self._hanging_ios

    @hanging_ios.setter
    def hanging_ios(self, hanging_ios):
        """Sets the hanging_ios of this InlineResponse2004Data.


        :param hanging_ios: The hanging_ios of this InlineResponse2004Data.  # noqa: E501
        :type: InlineResponse2004DataHangingIos
        """

        self._hanging_ios = hanging_ios

    @property
    def hosts(self):
        """Gets the hosts of this InlineResponse2004Data.  # noqa: E501


        :return: The hosts of this InlineResponse2004Data.  # noqa: E501
        :rtype: InlineResponse2004DataHosts
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this InlineResponse2004Data.


        :param hosts: The hosts of this InlineResponse2004Data.  # noqa: E501
        :type: InlineResponse2004DataHosts
        """

        self._hosts = hosts

    @property
    def hot_spare(self):
        """Gets the hot_spare of this InlineResponse2004Data.  # noqa: E501


        :return: The hot_spare of this InlineResponse2004Data.  # noqa: E501
        :rtype: float
        """
        return self._hot_spare

    @hot_spare.setter
    def hot_spare(self, hot_spare):
        """Sets the hot_spare of this InlineResponse2004Data.


        :param hot_spare: The hot_spare of this InlineResponse2004Data.  # noqa: E501
        :type: float
        """

        self._hot_spare = hot_spare

    @property
    def init_stage(self):
        """Gets the init_stage of this InlineResponse2004Data.  # noqa: E501


        :return: The init_stage of this InlineResponse2004Data.  # noqa: E501
        :rtype: str
        """
        return self._init_stage

    @init_stage.setter
    def init_stage(self, init_stage):
        """Sets the init_stage of this InlineResponse2004Data.


        :param init_stage: The init_stage of this InlineResponse2004Data.  # noqa: E501
        :type: str
        """

        self._init_stage = init_stage

    @property
    def init_stage_changed_time(self):
        """Gets the init_stage_changed_time of this InlineResponse2004Data.  # noqa: E501


        :return: The init_stage_changed_time of this InlineResponse2004Data.  # noqa: E501
        :rtype: str
        """
        return self._init_stage_changed_time

    @init_stage_changed_time.setter
    def init_stage_changed_time(self, init_stage_changed_time):
        """Sets the init_stage_changed_time of this InlineResponse2004Data.


        :param init_stage_changed_time: The init_stage_changed_time of this InlineResponse2004Data.  # noqa: E501
        :type: str
        """

        self._init_stage_changed_time = init_stage_changed_time

    @property
    def io_nodes(self):
        """Gets the io_nodes of this InlineResponse2004Data.  # noqa: E501


        :return: The io_nodes of this InlineResponse2004Data.  # noqa: E501
        :rtype: InlineResponse2004DataDrives
        """
        return self._io_nodes

    @io_nodes.setter
    def io_nodes(self, io_nodes):
        """Sets the io_nodes of this InlineResponse2004Data.


        :param io_nodes: The io_nodes of this InlineResponse2004Data.  # noqa: E501
        :type: InlineResponse2004DataDrives
        """

        self._io_nodes = io_nodes

    @property
    def io_status(self):
        """Gets the io_status of this InlineResponse2004Data.  # noqa: E501


        :return: The io_status of this InlineResponse2004Data.  # noqa: E501
        :rtype: str
        """
        return self._io_status

    @io_status.setter
    def io_status(self, io_status):
        """Sets the io_status of this InlineResponse2004Data.


        :param io_status: The io_status of this InlineResponse2004Data.  # noqa: E501
        :type: str
        """

        self._io_status = io_status

    @property
    def io_status_changed_time(self):
        """Gets the io_status_changed_time of this InlineResponse2004Data.  # noqa: E501


        :return: The io_status_changed_time of this InlineResponse2004Data.  # noqa: E501
        :rtype: str
        """
        return self._io_status_changed_time

    @io_status_changed_time.setter
    def io_status_changed_time(self, io_status_changed_time):
        """Sets the io_status_changed_time of this InlineResponse2004Data.


        :param io_status_changed_time: The io_status_changed_time of this InlineResponse2004Data.  # noqa: E501
        :type: str
        """

        self._io_status_changed_time = io_status_changed_time

    @property
    def is_cluster(self):
        """Gets the is_cluster of this InlineResponse2004Data.  # noqa: E501


        :return: The is_cluster of this InlineResponse2004Data.  # noqa: E501
        :rtype: bool
        """
        return self._is_cluster

    @is_cluster.setter
    def is_cluster(self, is_cluster):
        """Sets the is_cluster of this InlineResponse2004Data.


        :param is_cluster: The is_cluster of this InlineResponse2004Data.  # noqa: E501
        :type: bool
        """

        self._is_cluster = is_cluster

    @property
    def last_init_failure(self):
        """Gets the last_init_failure of this InlineResponse2004Data.  # noqa: E501


        :return: The last_init_failure of this InlineResponse2004Data.  # noqa: E501
        :rtype: str
        """
        return self._last_init_failure

    @last_init_failure.setter
    def last_init_failure(self, last_init_failure):
        """Sets the last_init_failure of this InlineResponse2004Data.


        :param last_init_failure: The last_init_failure of this InlineResponse2004Data.  # noqa: E501
        :type: str
        """

        self._last_init_failure = last_init_failure

    @property
    def last_init_failure_code(self):
        """Gets the last_init_failure_code of this InlineResponse2004Data.  # noqa: E501


        :return: The last_init_failure_code of this InlineResponse2004Data.  # noqa: E501
        :rtype: str
        """
        return self._last_init_failure_code

    @last_init_failure_code.setter
    def last_init_failure_code(self, last_init_failure_code):
        """Sets the last_init_failure_code of this InlineResponse2004Data.


        :param last_init_failure_code: The last_init_failure_code of this InlineResponse2004Data.  # noqa: E501
        :type: str
        """

        self._last_init_failure_code = last_init_failure_code

    @property
    def last_init_failure_time(self):
        """Gets the last_init_failure_time of this InlineResponse2004Data.  # noqa: E501


        :return: The last_init_failure_time of this InlineResponse2004Data.  # noqa: E501
        :rtype: str
        """
        return self._last_init_failure_time

    @last_init_failure_time.setter
    def last_init_failure_time(self, last_init_failure_time):
        """Sets the last_init_failure_time of this InlineResponse2004Data.


        :param last_init_failure_time: The last_init_failure_time of this InlineResponse2004Data.  # noqa: E501
        :type: str
        """

        self._last_init_failure_time = last_init_failure_time

    @property
    def licensing(self):
        """Gets the licensing of this InlineResponse2004Data.  # noqa: E501


        :return: The licensing of this InlineResponse2004Data.  # noqa: E501
        :rtype: InlineResponse2004DataLicensing
        """
        return self._licensing

    @licensing.setter
    def licensing(self, licensing):
        """Sets the licensing of this InlineResponse2004Data.


        :param licensing: The licensing of this InlineResponse2004Data.  # noqa: E501
        :type: InlineResponse2004DataLicensing
        """

        self._licensing = licensing

    @property
    def long_drive_grace_on_failure_secs(self):
        """Gets the long_drive_grace_on_failure_secs of this InlineResponse2004Data.  # noqa: E501


        :return: The long_drive_grace_on_failure_secs of this InlineResponse2004Data.  # noqa: E501
        :rtype: float
        """
        return self._long_drive_grace_on_failure_secs

    @long_drive_grace_on_failure_secs.setter
    def long_drive_grace_on_failure_secs(self, long_drive_grace_on_failure_secs):
        """Sets the long_drive_grace_on_failure_secs of this InlineResponse2004Data.


        :param long_drive_grace_on_failure_secs: The long_drive_grace_on_failure_secs of this InlineResponse2004Data.  # noqa: E501
        :type: float
        """

        self._long_drive_grace_on_failure_secs = long_drive_grace_on_failure_secs

    @property
    def name(self):
        """Gets the name of this InlineResponse2004Data.  # noqa: E501


        :return: The name of this InlineResponse2004Data.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2004Data.


        :param name: The name of this InlineResponse2004Data.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def net(self):
        """Gets the net of this InlineResponse2004Data.  # noqa: E501


        :return: The net of this InlineResponse2004Data.  # noqa: E501
        :rtype: InlineResponse2004DataNet
        """
        return self._net

    @net.setter
    def net(self, net):
        """Sets the net of this InlineResponse2004Data.


        :param net: The net of this InlineResponse2004Data.  # noqa: E501
        :type: InlineResponse2004DataNet
        """

        self._net = net

    @property
    def nodes(self):
        """Gets the nodes of this InlineResponse2004Data.  # noqa: E501


        :return: The nodes of this InlineResponse2004Data.  # noqa: E501
        :rtype: InlineResponse2004DataNodes
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this InlineResponse2004Data.


        :param nodes: The nodes of this InlineResponse2004Data.  # noqa: E501
        :type: InlineResponse2004DataNodes
        """

        self._nodes = nodes

    @property
    def overlay(self):
        """Gets the overlay of this InlineResponse2004Data.  # noqa: E501


        :return: The overlay of this InlineResponse2004Data.  # noqa: E501
        :rtype: InlineResponse2004DataOverlay
        """
        return self._overlay

    @overlay.setter
    def overlay(self, overlay):
        """Sets the overlay of this InlineResponse2004Data.


        :param overlay: The overlay of this InlineResponse2004Data.  # noqa: E501
        :type: InlineResponse2004DataOverlay
        """

        self._overlay = overlay

    @property
    def rebuild(self):
        """Gets the rebuild of this InlineResponse2004Data.  # noqa: E501


        :return: The rebuild of this InlineResponse2004Data.  # noqa: E501
        :rtype: InlineResponse2004DataRebuild
        """
        return self._rebuild

    @rebuild.setter
    def rebuild(self, rebuild):
        """Sets the rebuild of this InlineResponse2004Data.


        :param rebuild: The rebuild of this InlineResponse2004Data.  # noqa: E501
        :type: InlineResponse2004DataRebuild
        """

        self._rebuild = rebuild

    @property
    def release(self):
        """Gets the release of this InlineResponse2004Data.  # noqa: E501


        :return: The release of this InlineResponse2004Data.  # noqa: E501
        :rtype: str
        """
        return self._release

    @release.setter
    def release(self, release):
        """Sets the release of this InlineResponse2004Data.


        :param release: The release of this InlineResponse2004Data.  # noqa: E501
        :type: str
        """

        self._release = release

    @property
    def release_hash(self):
        """Gets the release_hash of this InlineResponse2004Data.  # noqa: E501


        :return: The release_hash of this InlineResponse2004Data.  # noqa: E501
        :rtype: str
        """
        return self._release_hash

    @release_hash.setter
    def release_hash(self, release_hash):
        """Sets the release_hash of this InlineResponse2004Data.


        :param release_hash: The release_hash of this InlineResponse2004Data.  # noqa: E501
        :type: str
        """

        self._release_hash = release_hash

    @property
    def scrubber_bytes_per_sec(self):
        """Gets the scrubber_bytes_per_sec of this InlineResponse2004Data.  # noqa: E501


        :return: The scrubber_bytes_per_sec of this InlineResponse2004Data.  # noqa: E501
        :rtype: float
        """
        return self._scrubber_bytes_per_sec

    @scrubber_bytes_per_sec.setter
    def scrubber_bytes_per_sec(self, scrubber_bytes_per_sec):
        """Sets the scrubber_bytes_per_sec of this InlineResponse2004Data.


        :param scrubber_bytes_per_sec: The scrubber_bytes_per_sec of this InlineResponse2004Data.  # noqa: E501
        :type: float
        """

        self._scrubber_bytes_per_sec = scrubber_bytes_per_sec

    @property
    def short_drive_grace_on_failure_secs(self):
        """Gets the short_drive_grace_on_failure_secs of this InlineResponse2004Data.  # noqa: E501


        :return: The short_drive_grace_on_failure_secs of this InlineResponse2004Data.  # noqa: E501
        :rtype: float
        """
        return self._short_drive_grace_on_failure_secs

    @short_drive_grace_on_failure_secs.setter
    def short_drive_grace_on_failure_secs(self, short_drive_grace_on_failure_secs):
        """Sets the short_drive_grace_on_failure_secs of this InlineResponse2004Data.


        :param short_drive_grace_on_failure_secs: The short_drive_grace_on_failure_secs of this InlineResponse2004Data.  # noqa: E501
        :type: float
        """

        self._short_drive_grace_on_failure_secs = short_drive_grace_on_failure_secs

    @property
    def start_io_starting_drives_grace_secs(self):
        """Gets the start_io_starting_drives_grace_secs of this InlineResponse2004Data.  # noqa: E501


        :return: The start_io_starting_drives_grace_secs of this InlineResponse2004Data.  # noqa: E501
        :rtype: float
        """
        return self._start_io_starting_drives_grace_secs

    @start_io_starting_drives_grace_secs.setter
    def start_io_starting_drives_grace_secs(self, start_io_starting_drives_grace_secs):
        """Sets the start_io_starting_drives_grace_secs of this InlineResponse2004Data.


        :param start_io_starting_drives_grace_secs: The start_io_starting_drives_grace_secs of this InlineResponse2004Data.  # noqa: E501
        :type: float
        """

        self._start_io_starting_drives_grace_secs = start_io_starting_drives_grace_secs

    @property
    def start_io_starting_io_nodes_grace_secs(self):
        """Gets the start_io_starting_io_nodes_grace_secs of this InlineResponse2004Data.  # noqa: E501


        :return: The start_io_starting_io_nodes_grace_secs of this InlineResponse2004Data.  # noqa: E501
        :rtype: float
        """
        return self._start_io_starting_io_nodes_grace_secs

    @start_io_starting_io_nodes_grace_secs.setter
    def start_io_starting_io_nodes_grace_secs(self, start_io_starting_io_nodes_grace_secs):
        """Sets the start_io_starting_io_nodes_grace_secs of this InlineResponse2004Data.


        :param start_io_starting_io_nodes_grace_secs: The start_io_starting_io_nodes_grace_secs of this InlineResponse2004Data.  # noqa: E501
        :type: float
        """

        self._start_io_starting_io_nodes_grace_secs = start_io_starting_io_nodes_grace_secs

    @property
    def status(self):
        """Gets the status of this InlineResponse2004Data.  # noqa: E501


        :return: The status of this InlineResponse2004Data.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse2004Data.


        :param status: The status of this InlineResponse2004Data.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def stripe_data_drives(self):
        """Gets the stripe_data_drives of this InlineResponse2004Data.  # noqa: E501


        :return: The stripe_data_drives of this InlineResponse2004Data.  # noqa: E501
        :rtype: float
        """
        return self._stripe_data_drives

    @stripe_data_drives.setter
    def stripe_data_drives(self, stripe_data_drives):
        """Sets the stripe_data_drives of this InlineResponse2004Data.


        :param stripe_data_drives: The stripe_data_drives of this InlineResponse2004Data.  # noqa: E501
        :type: float
        """

        self._stripe_data_drives = stripe_data_drives

    @property
    def stripe_protection_drives(self):
        """Gets the stripe_protection_drives of this InlineResponse2004Data.  # noqa: E501


        :return: The stripe_protection_drives of this InlineResponse2004Data.  # noqa: E501
        :rtype: float
        """
        return self._stripe_protection_drives

    @stripe_protection_drives.setter
    def stripe_protection_drives(self, stripe_protection_drives):
        """Sets the stripe_protection_drives of this InlineResponse2004Data.


        :param stripe_protection_drives: The stripe_protection_drives of this InlineResponse2004Data.  # noqa: E501
        :type: float
        """

        self._stripe_protection_drives = stripe_protection_drives

    @property
    def time(self):
        """Gets the time of this InlineResponse2004Data.  # noqa: E501


        :return: The time of this InlineResponse2004Data.  # noqa: E501
        :rtype: InlineResponse2004DataTime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this InlineResponse2004Data.


        :param time: The time of this InlineResponse2004Data.  # noqa: E501
        :type: InlineResponse2004DataTime
        """

        self._time = time

    @property
    def upgrade(self):
        """Gets the upgrade of this InlineResponse2004Data.  # noqa: E501


        :return: The upgrade of this InlineResponse2004Data.  # noqa: E501
        :rtype: str
        """
        return self._upgrade

    @upgrade.setter
    def upgrade(self, upgrade):
        """Sets the upgrade of this InlineResponse2004Data.


        :param upgrade: The upgrade of this InlineResponse2004Data.  # noqa: E501
        :type: str
        """

        self._upgrade = upgrade

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InlineResponse2004Data, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2004Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
