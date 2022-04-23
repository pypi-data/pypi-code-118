from enum import Enum
from typing import Optional
from .common import GraphBase


class ThroughputType(Enum):
    """
    吞吐量类型
    https://ndnsim.net/current/metric.html
    """
    InInterests = 0
    OutInterests = 1
    InData = 2
    OutData = 3
    InNacks = 4
    OutNacks = 5
    InSatisfiedInterests = 6
    InTimedOutInterests = 7
    OutSatisfiedInterests = 8
    OutTimedOutInterests = 9

    # 下面的类型只在 FaceId = -1 有效
    SatisfiedInterests = 10
    TimedOutInterests = 11


class ThroughputTarget(Enum):
    """
    吞吐量目标
    https://ndnsim.net/current/metric.html
    """
    Packets = 0  # estimated rate (EWMA average) of packets within the last averaging period (number of packets/s)
    Kilobytes = 1  # estimated rate (EWMA average) within last averaging period (kilobytes/s)
    PacketRaw = 2  # absolute number of packets within last averaging period (number of packets).
    KilobytesRaw = 3  # absolute number of kilobytes transferred within the last averaging period (number of packets).


class ThroughputItem:
    """
    一个用于描述 ndnsim 吞吐量采样结果的类
    """

    def __init__(self, Time: float, Node: str, FaceId: int, FaceDescr: str, Type: ThroughputType,
                 Packets: float, Kilobytes: float, PacketRaw: float, KilobytesRaw: float):
        """
        :param Time:        时间，例如: 0.5
        :param Node:        节点名称，例如：C1
        :param FaceId:      Face id
        :param FaceDescr:   Face 描述
        :param Type:
        :param Packets:
        :param Kilobytes:
        :param PacketRaw:
        :param KilobytesRaw:
        """
        self.Time = Time  # simulation time
        self.Node = Node  # node id, globally unique
        self.FaceId = FaceId  # interface ID (-1 for combined metric)
        self.FaceDescr = FaceDescr
        self.Type = Type
        self.Packets = Packets
        self.Kilobytes = Kilobytes
        self.PacketRaw = PacketRaw
        self.KilobytesRaw = KilobytesRaw

    def getValueByThroughputTarget(self, throughputTarget: ThroughputTarget):
        if throughputTarget == ThroughputTarget.Packets:
            return self.Packets
        elif throughputTarget == ThroughputTarget.Kilobytes:
            return self.Kilobytes
        elif throughputTarget == ThroughputTarget.PacketRaw:
            return self.PacketRaw
        else:
            return self.KilobytesRaw

    @staticmethod
    def parseLine(line: str):
        # 0.5	C1	1	internal://	InInterests	0	0	0	0
        values = line.strip().split("\t")
        if len(values) < 9:
            return None
        return ThroughputItem(float(values[0].strip()),
                              values[1].strip(),
                              int(values[2].strip()),
                              values[3].strip(),
                              ThroughputType[values[4].strip()],
                              float(values[5].strip()),
                              float(values[6].strip()),
                              float(values[7].strip()),
                              float(values[8].strip()),
                              )


class NodeFaceThroughput:
    """
    一个用于描述节点某个接口吞吐量的类
    """

    def __init__(self, Node: str, FaceId: int):
        self.Node = Node
        self.FaceId = FaceId
        self.typeMap = dict()  # 用于存储不同 Throughput Type 的采样记录
        for throughputType in ThroughputType:
            self.typeMap[throughputType.name] = []

    def appendItem(self, item: ThroughputItem):
        """
        新增一条采样记录
        :param item:
        :return:
        """
        # 如果不是当前接口的统计记录，忽略
        if item.Node != self.Node or item.FaceId != self.FaceId:
            return
        self.typeMap[item.Type.name].append(item)

    def getX(self, throughputType: ThroughputType = ThroughputType.OutData, samplingInterval: float = 1.0):
        """
        获取采样时间列表
        :param throughputType:
        :param samplingInterval:
        :return:
        """
        lastCount, res = 0, []
        for item in self.typeMap[throughputType.name]:
            if int(item.Time / samplingInterval) != lastCount:
                lastCount = int(item.Time / samplingInterval)
            else:
                continue
            res.append(lastCount * samplingInterval)
        return res

    def getY(self, throughputType: ThroughputType = ThroughputType.OutData,
             throughputTarget: ThroughputTarget = ThroughputTarget.Kilobytes,
             samplingInterval: float = 1.0):
        """
        获取吞吐量列表
        :param throughputType:          吞吐量类型
        :param throughputTarget:        吞吐量目标
        :param samplingInterval:       采样间隔
        :return:
        """
        lastCount, res = 0, []
        for item in self.typeMap[throughputType.name]:
            if int(item.Time / samplingInterval) != lastCount:
                lastCount = int(item.Time / samplingInterval)
            else:
                continue
            res.append(item.getValueByThroughputTarget(throughputTarget))
        return res


class NodeThroughput:
    """
    一个用于描述节点各个接口吞吐量的类
    """

    def __init__(self, Node: str):
        self.faceIdMap = dict()
        self.Node = Node

    def appendItem(self, item: ThroughputItem):
        """
        新增一条采样记录
        :param item:
        :return:
        """
        # 如果不是当前节点的统计记录，忽略
        if item.Node != self.Node:
            return
        if item.FaceId not in self.faceIdMap:
            self.faceIdMap[item.FaceId] = NodeFaceThroughput(item.Node, item.FaceId)
        self.faceIdMap[item.FaceId].appendItem(item)

    def getX(self, FaceId: int, throughputType: ThroughputType = ThroughputType.OutData,
             samplingInterval: float = 1.0) -> [float]:
        """
        获取采样时间列表
        :param FaceId:
        :param throughputType:
        :param samplingInterval:
        :return:
        """
        if FaceId not in self.faceIdMap:
            return []
        return self.faceIdMap[FaceId].getX(throughputType, samplingInterval)

    def getY(self, FaceId: int, throughputType: ThroughputType = ThroughputType.OutData,
             throughputTarget: ThroughputTarget = ThroughputTarget.Kilobytes, samplingInterval: float = 1.0):
        """
        获取吞吐量列表
        :param FaceId:                  FaceId
        :param throughputType:          吞吐量类型
        :param throughputTarget:        吞吐量目标
        :param samplingInterval:       采样间隔
        :return:
        """
        if FaceId not in self.faceIdMap:
            return []
        return self.faceIdMap[FaceId].getY(throughputType, throughputTarget, samplingInterval)


class Throughput:
    """
    一个用于解析 ndnsim 吞吐量采样结果的类
    """

    def __init__(self):
        self.nodeMap = dict()

    def getByNode(self, node: str) -> Optional[NodeThroughput]:
        if node not in self.nodeMap:
            return None
        return self.nodeMap[node]

    @staticmethod
    def parse(inputFile: str):
        """
        传入一个 ndnsim 采集的吞吐量结果文件，从中解析出吞吐量
        :param inputFile:
        :return:
        """
        throughput = Throughput()
        with open(inputFile, "r") as f:
            # 首先忽略表头
            # Time	Node	FaceId	FaceDescr	Type	Packets	Kilobytes	PacketRaw	KilobytesRaw
            f.readline()

            # 从第一行开始解析
            line = f.readline()
            while line:
                if line.strip() != "":
                    item = ThroughputItem.parseLine(line)
                    if item:
                        if item.Node not in throughput.nodeMap:
                            throughput.nodeMap[item.Node] = NodeThroughput(item.Node)
                        throughput.nodeMap[item.Node].appendItem(item)
                line = f.readline()
        return throughput


class ThroughputGraph(GraphBase):
    """
    一个用于实现绘制吞吐量图的类
    """

    def __init__(self, throughput: Throughput):
        super().__init__()
        self.throughput = throughput
        self.samplingInterval = 1.0
        self.throughputType = ThroughputType.OutData
        self.throughputTarget = ThroughputTarget.Kilobytes

    def setSamplingInterval(self, samplingInterval: float):
        """
        设置采样间隔 => 如果 samplingInterval = 1.0 表示绘图时，每秒采样一次
        :param samplingInterval:
        :return:
        """
        self.samplingInterval = samplingInterval
        return self

    def setThroughputType(self, throughputType: ThroughputType):
        """
        设置吞吐量类型
        :param throughputType:
        :return:
        """
        self.throughputType = throughputType
        return self

    def setThroughputTarget(self, throughputTarget: ThroughputTarget):
        """
        设置吞吐量目标
        :param throughputTarget:
        :return:
        """
        self.throughputTarget = throughputTarget
        return self

    def plot(self, node: str, faceId: int, *args,
             color: str = "&&",
             linewidth: float = 2, linestyle: str = "dotted", marker: str = "&&",
             markerfacecolor: str = "none", markersize: float = 6,
             **kwargs):
        node = self.throughput.getByNode(node)
        if not node:
            print("not exist node: ", node)
            return
        if "label" not in kwargs:
            kwargs["label"] = node.Node
        x, y = node.getX(faceId, samplingInterval=self.samplingInterval), \
               node.getY(faceId, self.throughputType, self.throughputTarget, self.samplingInterval)
        super().plot(x, y, *args, **kwargs)
        return self

    @staticmethod
    def parse(inputFile: str):
        return ThroughputGraph(Throughput.parse(inputFile))
