# Copyright (c) MONAI Consortium
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
from typing import Optional, Sequence, Union

import cv2
import numpy as np
import skimage.measure as measure
from monai.config import KeysCollection
from monai.transforms import MapTransform, Resize, generate_spatial_bounding_box, get_extreme_points
from monai.transforms.spatial.dictionary import InterpolateModeSequence
from monai.utils import InterpolateMode, ensure_tuple_rep
from shapely.geometry import Polygon

from monailabel.utils.others.label_colors import get_color

logger = logging.getLogger(__name__)


# TODO:: Move to MONAI ??


class LargestCCd(MapTransform):
    def __init__(self, keys: KeysCollection, has_channel: bool = True):
        super().__init__(keys)
        self.has_channel = has_channel

    @staticmethod
    def get_largest_cc(label):
        largest_cc = np.zeros(shape=label.shape, dtype=label.dtype)
        for i, item in enumerate(label):
            item = measure.label(item, connectivity=1)
            if item.max() != 0:
                largest_cc[i, ...] = item == (np.argmax(np.bincount(item.flat)[1:]) + 1)
        return largest_cc

    def __call__(self, data):
        d = dict(data)
        for key in self.keys:
            result = self.get_largest_cc(d[key] if self.has_channel else d[key][np.newaxis])
            d[key] = result if self.has_channel else result[0]
        return d


class ExtremePointsd(MapTransform):
    def __init__(self, keys: KeysCollection, result: str = "result", points: str = "points"):
        super().__init__(keys)
        self.result = result
        self.points = points

    def __call__(self, data):
        d = dict(data)
        for key in self.keys:
            try:
                points = get_extreme_points(d[key])
                if d.get(self.result) is None:
                    d[self.result] = dict()
                d[self.result][self.points] = np.array(points).astype(int).tolist()
            except ValueError:
                pass
        return d


class BoundingBoxd(MapTransform):
    def __init__(self, keys: KeysCollection, result: str = "result", bbox: str = "bbox"):
        super().__init__(keys)
        self.result = result
        self.bbox = bbox

    def __call__(self, data):
        d = dict(data)
        for key in self.keys:
            bbox = generate_spatial_bounding_box(d[key])
            if d.get(self.result) is None:
                d[self.result] = dict()
            d[self.result][self.bbox] = np.array(bbox).astype(int).tolist()
        return d


class Restored(MapTransform):
    def __init__(
        self,
        keys: KeysCollection,
        ref_image: str,
        has_channel: bool = True,
        mode: InterpolateModeSequence = InterpolateMode.NEAREST,
        align_corners: Union[Sequence[Optional[bool]], Optional[bool]] = None,
        meta_key_postfix: str = "meta_dict",
    ):
        super().__init__(keys)
        self.ref_image = ref_image
        self.has_channel = has_channel
        self.mode = ensure_tuple_rep(mode, len(self.keys))
        self.align_corners = ensure_tuple_rep(align_corners, len(self.keys))
        self.meta_key_postfix = meta_key_postfix

    def __call__(self, data):
        d = dict(data)
        meta_dict = d[f"{self.ref_image}_{self.meta_key_postfix}"]
        for idx, key in enumerate(self.keys):
            result = d[key]
            current_size = result.shape[1:] if self.has_channel else result.shape
            spatial_shape = meta_dict["spatial_shape"]
            spatial_size = spatial_shape[-len(current_size) :]

            # Undo Spacing
            if np.any(np.not_equal(current_size, spatial_size)):
                resizer = Resize(spatial_size=spatial_size, mode=self.mode[idx])
                result = resizer(result, mode=self.mode[idx], align_corners=self.align_corners[idx])

            d[key] = result if len(result.shape) <= 3 else result[0] if result.shape[0] == 1 else result

            meta = d.get(f"{key}_{self.meta_key_postfix}")
            if meta is None:
                meta = dict()
                d[f"{key}_{self.meta_key_postfix}"] = meta
            meta["affine"] = meta_dict.get("original_affine")
        return d


class FindContoursd(MapTransform):
    def __init__(
        self,
        keys: KeysCollection,
        min_positive=10,
        min_poly_area=80,
        result="result",
        result_output_key="annotation",
        key_label_colors="label_colors",
        labels=None,
    ):
        super().__init__(keys)

        self.min_positive = min_positive
        self.min_poly_area = min_poly_area
        self.result = result
        self.result_output_key = result_output_key
        self.key_label_colors = key_label_colors

        labels = labels if labels else dict()
        labels = [labels] if isinstance(labels, str) else labels
        if not isinstance(labels, dict):
            labels = {v: k + 1 for k, v in enumerate(labels)}

        labels = {v: k for k, v in labels.items()}
        self.labels = labels

    def __call__(self, data):
        d = dict(data)
        location = d.get("location", [0, 0])
        size = d.get("size", [0, 0])
        min_poly_area = d.get("min_poly_area", self.min_poly_area)
        color_map = d.get(self.key_label_colors)

        elements = []
        label_names = set()
        for key in self.keys:
            p = d[key]
            if np.count_nonzero(p) < self.min_positive:
                continue

            labels = [label for label in np.unique(p).tolist() if label > 0]
            logger.debug(f"Total Unique Masks (excluding background): {labels}")
            for label_idx in labels:
                p = d[key]
                p[p == label_idx] = 1
                label_name = self.labels.get(label_idx, label_idx)
                label_names.add(label_name)

                polygons = []
                contours, _ = cv2.findContours(p, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
                for contour in contours:
                    contour = np.squeeze(contour)
                    if len(contour) < 3:
                        continue

                    contour[:, 0] += location[0]  # X
                    contour[:, 1] += location[1]  # Y

                    coords = contour.astype(int).tolist()
                    pobj = Polygon(coords)
                    if pobj.area < min_poly_area:  # Ignore poly with lesser area
                        continue

                    logger.debug(f"Area: {pobj.area}; Perimeter: {pobj.length}; Count: {len(coords)}")
                    polygons.append(coords)

                if len(polygons):
                    logger.debug(f"+++++ {label_idx} => Total Polygons Found: {len(polygons)}")
                    elements.append({"label": label_name, "contours": polygons})

        if elements:
            if d.get(self.result) is None:
                d[self.result] = dict()
            d[self.result][self.result_output_key] = {
                "location": location,
                "size": size,
                "elements": elements,
                "labels": {n: get_color(n, color_map) for n in label_names},
            }
            logger.debug(f"+++++ ALL => Total Annotation Elements Found: {len(elements)}")
        return d
