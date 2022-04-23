"""
saved_query

This module defines saved_query class
:copyright: (c) 2022 by Timeplus
:license: Apache2, see LICENSE for more details.
"""

from timeplus.resource import ResourceBase


class SavedQuery(ResourceBase):
    """
    SavedQuery class defines saved query object
    """

    _resource_name = "savedqueries"

    def __init__(self, env=None):
        ResourceBase.__init__(self, env)

    @classmethod
    def build(cls, val, env=None):
        obj = cls(env=env)
        obj._data = val
        return obj

    def description(self, *args):
        return self.prop("description", *args)

    def id(self):
        return self.prop("id")

    def name(self, *args):
        return self.prop("name", *args)

    def sql(self, *args):
        return self.prop("sql", *args)

    def tags(self, *args):
        return self.prop("tags", *args)
