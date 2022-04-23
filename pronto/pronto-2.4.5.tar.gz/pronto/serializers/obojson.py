from typing import BinaryIO

import fastobo

from ._fastobo import FastoboSerializer
from .base import BaseSerializer


class OboJSONSerializer(FastoboSerializer, BaseSerializer):

    format = "json"

    def dump(self, file: BinaryIO):
        doc = self._to_obodoc(self.ont)
        fastobo.dump_graph(doc, file)
