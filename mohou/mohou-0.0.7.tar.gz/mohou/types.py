from abc import ABC, abstractmethod
import collections.abc
import copy
from dataclasses import dataclass
import functools
import operator
import queue
import random
from typing import Generic, Optional, List, Tuple, Type, TypeVar, Iterator, Sequence, ClassVar, Dict

import numpy as np
import matplotlib.pyplot as plt
import torch
import torchvision
import cv2

from mohou.constant import N_DATA_INTACT
from mohou.file import load_object, dump_object
from mohou.image_randomizer import _f_randomize_rgb_image, _f_randomize_depth_image
from mohou.constant import CONTINUE_FLAG_VALUE, TERMINATE_FLAG_VALUE
from mohou.utils import split_sequence, canvas_to_ndarray
from mohou.utils import assert_with_message, assert_isinstance_with_message

ElementT = TypeVar('ElementT', bound='ElementBase')
PrimitiveElementT = TypeVar('PrimitiveElementT', bound='PrimitiveElementBase')
PrimitiveImageT = TypeVar('PrimitiveImageT', bound='PrimitiveImageBase')
CompositeImageT = TypeVar('CompositeImageT', bound='CompositeImageBase')
ImageT = TypeVar('ImageT', bound='ImageBase')
VectorT = TypeVar('VectorT', bound='VectorBase')


class ElementBase(ABC):

    def __new__(cls, *args, **kwargs):
        # instantiationg blocking hack. Different but similar to
        # https://stackoverflow.com/a/7990308/7624196
        assert cls.is_concrete_type(),\
            '{} is an abstract class and thus cannot instantiate'.format(cls.__name__)
        # https://stackoverflow.com/questions/59217884/
        return super(ElementBase, cls).__new__(cls)

    @classmethod
    def is_concrete_type(cls):
        return len(cls.__abstractmethods__) == 0 and len(cls.__subclasses__()) == 0

    @property
    @abstractmethod
    def shape(self) -> Tuple[int, ...]:
        pass

    @abstractmethod
    def to_tensor(self) -> torch.Tensor:
        pass

    @classmethod
    @abstractmethod
    def from_tensor(cls: Type[ElementT], tensor: torch.Tensor) -> ElementT:
        pass


class PrimitiveElementBase(ElementBase):
    _data: np.ndarray  # cmposition over inheritance!

    def __init__(self, data: np.ndarray) -> None:
        assert_isinstance_with_message(data, np.ndarray)
        assert not np.isnan(data).any()
        assert not np.isinf(data).any()
        self._data = np.array(data)

    @property
    def shape(self) -> Tuple[int, ...]:
        return self._data.shape

    def numpy(self):
        return self._data

    def __iter__(self) -> Iterator:
        return self._data.__iter__()

    def __getitem__(self, index):
        return self._data[index]


class VectorBase(PrimitiveElementBase):

    def __init__(self, data: np.ndarray) -> None:
        super().__init__(data)
        assert self._data.ndim == 1

    def to_tensor(self) -> torch.Tensor:
        return torch.from_numpy(self._data).float()

    @classmethod
    def from_tensor(cls: Type[VectorT], tensor: torch.Tensor) -> VectorT:
        array = tensor.detach().clone().numpy()
        return cls(array)

    def __len__(self):
        return len(self._data)


class AngleVector(VectorBase):
    pass


class TerminateFlag(VectorBase):

    @classmethod
    def from_bool(cls, flag: bool) -> 'TerminateFlag':
        assert isinstance(flag, bool)
        val = TERMINATE_FLAG_VALUE if flag else CONTINUE_FLAG_VALUE
        data = np.array([val], dtype=np.float64)
        return cls(data)


class ImageBase(ElementBase):

    @classmethod
    @abstractmethod
    def channel(cls) -> int:
        pass

    @abstractmethod
    def randomize(self: ImageT) -> ImageT:
        pass

    @classmethod
    @abstractmethod
    def dummy_from_shape(cls: Type[ImageT], shape2d: Tuple[int, int]) -> ImageT:
        pass

    @abstractmethod
    def to_rgb(self, *args, **kwargs) -> 'RGBImage':
        pass

    @abstractmethod
    def resize(self, shape2d_new: Tuple[int, int]) -> None:
        pass


class PrimitiveImageBase(PrimitiveElementBase, ImageBase):
    _channel: ClassVar[int]

    def __init__(self, data: np.ndarray) -> None:
        super().__init__(data)
        assert_with_message(self._data.ndim, 3, 'image_dim')
        assert_with_message(data.shape[2], self.channel(), 'channel')

    @classmethod
    def channel(cls) -> int:
        return cls._channel


class RGBImage(PrimitiveImageBase):
    _channel: ClassVar[int] = 3

    def __init__(self, data: np.ndarray) -> None:
        super().__init__(data)
        assert_with_message(self._data.dtype.type, np.uint8, 'numpy type')

    def to_tensor(self) -> torch.Tensor:
        return torchvision.transforms.ToTensor()(self._data).float()

    @classmethod
    def from_tensor(cls, tensor: torch.Tensor) -> 'RGBImage':
        tf = torchvision.transforms.ToPILImage()
        pil_iamge = tf(tensor)
        return cls(np.array(pil_iamge))

    def randomize(self) -> 'RGBImage':
        assert _f_randomize_rgb_image is not None
        rand_image_arr = _f_randomize_rgb_image(self._data)
        return RGBImage(rand_image_arr)

    @classmethod
    def dummy_from_shape(cls, shape2d: Tuple[int, int]) -> 'RGBImage':
        shape = (shape2d[0], shape2d[1], cls.channel())
        dummy_array = np.random.randint(0, high=255, size=shape, dtype=np.uint8)
        return cls(dummy_array)

    def to_rgb(self, *args, **kwargs) -> 'RGBImage':
        return self

    def resize(self, shape2d_new: Tuple[int, int]) -> None:
        self._data = cv2.resize(self._data, shape2d_new, interpolation=cv2.INTER_AREA)


class DepthImage(PrimitiveImageBase):
    _channel: ClassVar[int] = 1
    _max_value: ClassVar[float] = 4.0
    _min_value: ClassVar[float] = -1.0

    def __init__(self, data: np.ndarray) -> None:
        super().__init__(data)
        assert_with_message(self._data.dtype.type, [np.float16, np.float32, np.float64], 'numpy type')

    def to_tensor(self) -> torch.Tensor:
        data_cutoff = np.maximum(np.minimum(self._data, self._max_value), self._min_value)
        data_normalized = (data_cutoff - self._min_value) / (self._max_value - self._min_value)
        return torch.from_numpy(data_normalized.transpose((2, 0, 1))).contiguous().float()

    @classmethod
    def from_tensor(cls, tensor: torch.Tensor) -> 'DepthImage':
        data = tensor.detach().clone().numpy().transpose((1, 2, 0))
        data_denormalized = data * (cls._max_value - cls._min_value) + cls._min_value
        return cls(data_denormalized)

    def randomize(self) -> 'DepthImage':
        assert _f_randomize_depth_image is not None
        rand_depth_arr = _f_randomize_depth_image(self._data)
        return DepthImage(rand_depth_arr)

    @classmethod
    def dummy_from_shape(cls, shape2d: Tuple[int, int]) -> 'DepthImage':
        shape = (shape2d[0], shape2d[1], cls.channel())
        dummy_array = np.random.rand(*shape)
        return cls(dummy_array)

    def to_rgb(self, *args, **kwargs) -> 'RGBImage':
        fig = plt.figure()
        ax = plt.subplot(1, 1, 1)
        ax.imshow(self._data[:, :, 0])
        fig.canvas.draw()
        arr = canvas_to_ndarray(fig)
        plt.close(fig)
        return RGBImage(arr)

    def resize(self, shape2d_new: Tuple[int, int]) -> None:
        tmp = cv2.resize(self._data, shape2d_new, interpolation=cv2.INTER_CUBIC)
        self._data = np.expand_dims(tmp, axis=2)


class CompositeImageBase(ImageBase):
    image_types: ClassVar[List[Type[PrimitiveImageBase]]]
    images: List[PrimitiveImageBase]

    def __init__(self, images: List[PrimitiveImageBase], check_size=True):

        image_shape = images[0].shape[:2]

        if check_size:
            for image in images:
                assert_with_message(image.shape[:2], image_shape, 'image w-h')

        for image, image_type in zip(images, self.image_types):
            assert_isinstance_with_message(image, image_type)

        self.images = images

    def to_tensor(self) -> torch.Tensor:
        return torch.cat([im.to_tensor() for im in self.images])

    @property
    def shape(self) -> Tuple[int, int, int]:
        shape_2d = self.images[0].shape[:2]
        return (shape_2d[0], shape_2d[1], self.channel())

    def randomize(self: CompositeImageT) -> CompositeImageT:
        rand = copy.deepcopy(self)
        for i in range(len(rand.images)):
            rand.images[i] = self.images[i].randomize()
        return rand

    @classmethod
    def channel(cls) -> int:
        return sum([t.channel() for t in cls.image_types])

    @classmethod
    def from_tensor(cls: Type[CompositeImageT], tensor: torch.Tensor) -> CompositeImageT:
        channel_list = [t.channel() for t in cls.image_types]
        images = []
        for image_type, sub_tensor in zip(cls.image_types, split_sequence(tensor, channel_list)):
            image = image_type.from_tensor(sub_tensor)
            images.append(image)
        return cls(images)

    @classmethod
    def dummy_from_shape(cls: Type[CompositeImageT], shape2d: Tuple[int, int]) -> CompositeImageT:
        images = [t.dummy_from_shape(shape2d) for t in cls.image_types]
        return cls(images)

    def get_primitive_image(self, image_type: Type[PrimitiveImageT]) -> PrimitiveImageT:
        for image in self.images:
            if isinstance(image, image_type):
                return image
        assert False

    def resize(self, shape2d_new: Tuple[int, int]) -> None:
        for image in self.images:
            image.resize(shape2d_new)


class RGBDImage(CompositeImageBase):
    image_types = [RGBImage, DepthImage]

    def to_rgb(self, *args, **kwargs) -> RGBImage:
        for image in self.images:
            if isinstance(image, RGBImage):
                return image
        assert False


class ElementDict(Dict[Type[ElementBase], ElementBase]):

    def __init__(self, elems: Sequence[ElementBase]):
        for elem in elems:
            self[elem.__class__] = elem
        assert_with_message(len(set(self.keys())), len(elems), 'num of element')

    def __getitem__(self, key: Type[ElementT]) -> ElementT:
        if issubclass(key, PrimitiveElementBase):
            return super().__getitem__(key)  # type: ignore

        elif issubclass(key, CompositeImageBase):
            if key in self:
                return super().__getitem__(key)  # type: ignore

            # TODO(HiroIshida) somehow, if the following is written in comprehension
            # then we get "TypeError: super(type, obj): obj must be an instance or subtype of type"
            images = []
            for imt in key.image_types:
                images.append(super().__getitem__(imt))
            return key(images)  # type: ignore

        else:
            assert False


def get_all_concrete_types() -> List[Type[ElementBase]]:
    concrete_types: List[Type] = []
    q = queue.Queue()  # type: ignore
    q.put(ElementBase)
    while not q.empty():
        t: Type = q.get()
        if len(t.__subclasses__()) == 0:
            concrete_types.append(t)

        for st in t.__subclasses__():
            q.put(st)
    return list(set(concrete_types))


def get_element_type(type_name: str) -> Type[ElementBase]:
    for t in get_all_concrete_types():
        if type_name == t.__name__:
            return t
    assert False, 'type {} not found'.format(type_name)


class ElementSequence(collections.abc.Sequence, Generic[ElementT]):
    elem_type: Optional[Type[ElementT]] = None
    elem_shape: Optional[Tuple[int, ...]] = None
    elem_list: List[ElementT]

    def __init__(self, elem_list: Optional[List[ElementT]] = None):
        if elem_list is None or len(elem_list) == 0:
            self.elem_list = []
        else:
            assert len(set([type(elem) for elem in elem_list])) == 1
            assert len(set([elem.shape for elem in elem_list])) == 1
            self.elem_list = elem_list
            self.elem_type = type(elem_list[0])
            self.elem_shape = elem_list[0].shape

    def __len__(self):
        return len(self.elem_list)

    def __getitem__(self, index):
        return self.elem_list[index]

    def __iter__(self) -> Iterator[ElementT]:
        return self.elem_list.__iter__()

    def append(self, elem: ElementT):
        if self.elem_type is None:
            self.elem_type = type(elem)
        if self.elem_shape is None:
            self.elem_shape = elem.shape
        assert type(elem) == self.elem_type
        assert elem.shape == self.elem_shape
        self.elem_list.append(elem)

    def get_partial(self, indices: List[int]) -> 'ElementSequence[ElementT]':
        elems = [self.elem_list[idx] for idx in indices]
        return ElementSequence(elems)


def create_composite_image_sequence(
        composite_image_type: Type[CompositeImageT],
        elem_seqs: List[ElementSequence[PrimitiveImageBase]]) -> ElementSequence[CompositeImageT]:

    n_len_seq = len(elem_seqs[0])
    composite_image_seq = ElementSequence[CompositeImageT]([])
    for i in range(n_len_seq):
        composite_image = composite_image_type([seq[i] for seq in elem_seqs])
        composite_image_seq.append(composite_image)
    return composite_image_seq


@dataclass(frozen=True)
class EpisodeData:
    type_shape_table: Dict[Type[ElementBase], Tuple[int, ...]]
    sequence_list: List[ElementSequence]

    def __post_init__(self):
        ef_seq = self.filter_by_type(TerminateFlag)
        self.check_terminate_seq(ef_seq)

    @staticmethod
    def create_default_terminate_flag_seq(n_length) -> ElementSequence[TerminateFlag]:
        flag_lst = [TerminateFlag.from_bool(False) for _ in range(n_length - 1)]
        flag_lst.append(TerminateFlag.from_bool(True))
        elem_seq = ElementSequence(flag_lst)
        return elem_seq

    @staticmethod
    def check_terminate_seq(ef_seq: ElementSequence[TerminateFlag]):
        # first index must be CONTINUE
        assert ef_seq[0].numpy().item() == CONTINUE_FLAG_VALUE
        # last index must be END
        assert ef_seq[-1].numpy().item() == TERMINATE_FLAG_VALUE

        # sequence must be like ffffffftttttt not ffffttffftttt
        change_count = 0
        for i in range(len(ef_seq) - 1):
            if ef_seq[i + 1].numpy().item() != ef_seq[i].numpy().item():
                change_count += 1
        assert change_count == 1

    @classmethod
    def from_seq_list(cls, sequence_list: List[ElementSequence]):

        for sequence in sequence_list:
            assert isinstance(sequence, ElementSequence)

        all_same_length = len(set(map(len, sequence_list))) == 1
        assert all_same_length

        types = [type(seq[0]) for seq in sequence_list]

        if TerminateFlag not in set(types):
            terminate_flag_seq = cls.create_default_terminate_flag_seq(len(sequence_list[0]))
            sequence_list.append(terminate_flag_seq)
            types.append(TerminateFlag)

        shapes = [seq[0].shape for seq in sequence_list]
        type_shape_table = dict({t: s for (t, s) in zip(types, shapes)})

        n_type = len(set(types))
        all_different_type = n_type == len(sequence_list)
        assert all_different_type, 'all sequences must have different type'
        return cls(type_shape_table, sequence_list)

    def filter_by_primitive_type(self, elem_type: Type[PrimitiveElementT]) -> ElementSequence[PrimitiveElementT]:
        for seq in self.sequence_list:
            if isinstance(seq[0], elem_type):
                # thanks to all_different_type
                return seq
        assert False

    def filter_by_type(self, elem_type: Type[ElementT]) -> ElementSequence[ElementT]:

        if issubclass(elem_type, PrimitiveElementBase):
            return self.filter_by_primitive_type(elem_type)  # type: ignore
        elif issubclass(elem_type, CompositeImageBase):
            seqs = [self.filter_by_primitive_type(t) for t in elem_type.image_types]
            return create_composite_image_sequence(elem_type, seqs)  # type: ignore
        else:
            assert False

    def get_partial(self, indices: List[int], flag_seq: Optional[ElementSequence[TerminateFlag]] = None) -> 'EpisodeData':

        partial_sequence_list = []
        for seq in self.sequence_list:
            if seq.elem_type == TerminateFlag:
                # TerminateFlag is only the spatial type!
                n_partial_length = len(indices)
                if flag_seq is None:
                    seq_partial = self.create_default_terminate_flag_seq(n_partial_length)
                else:
                    assert len(flag_seq) == n_partial_length
                    seq_partial = flag_seq
            else:
                seq_partial = seq.get_partial(indices)
            partial_sequence_list.append(seq_partial)
        return EpisodeData.from_seq_list(partial_sequence_list)

    def __iter__(self):
        return self.sequence_list.__iter__()


class MultiEpisodeChunk:
    data_list: List[EpisodeData]
    data_list_intact: List[EpisodeData]
    type_shape_table: Dict[Type[ElementBase], Tuple[int, ...]]

    def __init__(
            self, data_list: List[EpisodeData],
            shuffle: bool = True, with_intact_data: bool = True):

        set_types = set(functools.reduce(
            operator.add,
            [list(data.type_shape_table.keys()) for data in data_list]))

        n_type_appeared = len(set_types)
        n_type_expected = len(data_list[0].type_shape_table.keys())
        assert_with_message(n_type_appeared, n_type_expected, 'num of element in chunk')

        if shuffle:
            random.shuffle(data_list)

        if with_intact_data:
            self.data_list_intact = data_list[:N_DATA_INTACT]
            self.data_list = data_list[N_DATA_INTACT:]
        else:
            self.data_list_intact = []
            self.data_list = data_list

        self.type_shape_table = data_list[0].type_shape_table

    def __iter__(self) -> Iterator[EpisodeData]:
        return self.data_list.__iter__()

    def __getitem__(self, index):
        return self.data_list.__getitem__(index)

    def get_element_shape(self, elem_type: Type[ElementBase]) -> Tuple[int, ...]:
        return self.type_shape_table[elem_type]

    @classmethod
    def load(cls, project_name: str, postfix: Optional[str] = None) -> 'MultiEpisodeChunk':
        return load_object(cls, project_name, postfix)

    @classmethod
    def load_aux(cls, project_name: str) -> 'MultiEpisodeChunk':
        return load_object(cls, project_name, postfix='auxiliary')

    def dump(self, project_name: str, postfix: Optional[str] = None) -> None:
        dump_object(self, project_name, postfix)

    def dump_aux(self, project_name: str) -> None:
        dump_object(self, project_name, postfix='auxiliary')

    def get_intact_chunk(self) -> 'MultiEpisodeChunk':
        return MultiEpisodeChunk(self.data_list_intact, shuffle=False, with_intact_data=False)

    def get_not_intact_chunk(self) -> 'MultiEpisodeChunk':
        return MultiEpisodeChunk(self.data_list, shuffle=False, with_intact_data=False)

    def merge(self, other: 'MultiEpisodeChunk') -> None:
        keys_self = set(self.type_shape_table.keys())
        keys_other = set(other.type_shape_table.keys())
        assert keys_other.issubset(keys_self)  # TODO(HiroIshida) current limitation, and easily remove this assertion
        keys_common = keys_self.intersection(keys_other)

        def filter_episode_data_list(episode_data_list):
            # TODO(HiroIshida) not efficient at all...
            episode_data_list_filtered = []
            for episode_data in episode_data_list:
                seqs = []
                for key in keys_common:
                    seqs.append(episode_data.filter_by_type(key))
                episode_data_list_filtered.append(EpisodeData.from_seq_list(seqs))
            assert len(episode_data_list) == len(episode_data_list_filtered)
            return episode_data_list_filtered

        data_list_new = other.data_list
        data_list_intact_new = other.data_list_intact
        data_list_new.extend(filter_episode_data_list(self.data_list))
        self.data_list = data_list_new
        self.data_list_intact = data_list_intact_new
        self.type_shape_table = other.type_shape_table
