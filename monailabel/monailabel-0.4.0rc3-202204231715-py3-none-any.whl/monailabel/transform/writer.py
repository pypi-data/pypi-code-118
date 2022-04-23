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
import tempfile

import itk
import numpy as np
from monai.data import write_nifti

from monailabel.utils.others.generic import file_ext
from monailabel.utils.others.pathology import create_asap_annotations_xml, create_dsa_annotations_json

logger = logging.getLogger(__name__)


# TODO:: Move to MONAI ??
def write_itk(image_np, output_file, affine, dtype, compress):
    if len(image_np.shape) > 2:
        image_np = image_np.transpose().copy()
    if dtype:
        image_np = image_np.astype(dtype)

    result_image = itk.image_from_array(image_np)
    logger.debug(f"ITK Image size: {itk.size(result_image)}")

    # https://github.com/RSIP-Vision/medio/blob/master/medio/metadata/affine.py#L108-L121
    if affine is not None:
        convert_aff_mat = np.diag([-1, -1, 1, 1])
        if affine.shape[0] == 3:
            convert_aff_mat = np.diag([-1, -1, 1])
        affine = convert_aff_mat @ affine

        dim = affine.shape[0] - 1
        _origin_key = (slice(-1), -1)
        _m_key = (slice(-1), slice(-1))

        origin = affine[_origin_key]
        spacing = np.linalg.norm(affine[_m_key] @ np.eye(dim), axis=0)
        direction = affine[_m_key] @ np.diag(1 / spacing)

        logger.debug(f"Affine: {affine}")
        logger.debug(f"Origin: {origin}")
        logger.debug(f"Spacing: {spacing}")
        logger.debug(f"Direction: {direction}")

        result_image.SetDirection(itk.matrix_from_array(direction))
        result_image.SetSpacing(spacing)
        result_image.SetOrigin(origin)

    itk.imwrite(result_image, output_file, compress)


class Writer:
    def __init__(
        self,
        label="pred",
        json=None,
        ref_image=None,
        key_extension="result_extension",
        key_dtype="result_dtype",
        key_compress="result_compress",
        key_write_to_file="result_write_to_file",
        meta_key_postfix="meta_dict",
        nibabel=False,
    ):
        self.label = label
        self.json = json
        self.ref_image = ref_image if ref_image else label

        # User can specify through params
        self.key_extension = key_extension
        self.key_dtype = key_dtype
        self.key_compress = key_compress
        self.key_write_to_file = key_write_to_file
        self.meta_key_postfix = meta_key_postfix
        self.nibabel = nibabel

    def __call__(self, data):
        logger.setLevel(data.get("logging", "INFO").upper())

        ext = file_ext(data.get("image_path"))
        dtype = data.get(self.key_dtype, None)
        compress = data.get(self.key_compress, False)
        write_to_file = data.get(self.key_write_to_file, True)
        ext = data.get(self.key_extension) if data.get(self.key_extension) else ext
        logger.info(f"Result ext: {ext}; write_to_file: {write_to_file}; dtype: {dtype}")

        image_np = data[self.label]
        meta_dict = data.get(f"{self.ref_image}_{self.meta_key_postfix}")
        affine = meta_dict.get("affine") if meta_dict else None
        logger.debug(f"Image: {image_np.shape}; Data Image: {data[self.label].shape}")

        output_file = None
        output_json = data.get(self.json, {})
        if write_to_file:
            output_file = tempfile.NamedTemporaryFile(suffix=ext).name
            logger.debug(f"Saving Image to: {output_file}")

            # Issue with slicer:: https://discourse.itk.org/t/saving-non-orthogonal-volume-in-nifti-format/2760/22
            if self.nibabel and ext.lower() in [".nii", ".nii.gz"]:
                logger.debug("Using MONAI write_nifti...")
                write_nifti(image_np, output_file, affine=affine, output_dtype=dtype)
            else:
                write_itk(image_np, output_file, affine, dtype, compress)

        return output_file, output_json


class ClassificationWriter:
    def __init__(self, label="pred", label_names=None):
        self.label = label
        self.label_names = label_names

    def __call__(self, data):
        result = []
        for label in data[self.label]:
            result.append(self.label_names[int(label)])
        return None, {"prediction": result}


class PolygonWriter:
    def __init__(
        self,
        label="pred",
        json="result",
        key_write_to_file="result_write_to_file",
        key_annotations="annotations",
        key_label_colors="label_colors",
        key_output_format="output",
    ):
        self.label = label
        self.json = json
        self.key_write_to_file = key_write_to_file
        self.key_annotations = key_annotations
        self.key_label_colors = key_label_colors
        self.key_output_format = key_output_format
        self.format = format

    def __call__(self, data):
        loglevel = data.get("logging", "INFO").upper()
        logger.setLevel(loglevel)

        output = data.get(self.key_output_format, "dsa")
        logger.info(f"+++ Output Type: {output}")

        output_json = data.get(self.json, {})
        write_to_file = data.get(self.key_write_to_file, True)
        if not write_to_file:
            return None, output_json

        res_json = {
            "name": f"MONAILabel Annotations - {data.get('model')}",
            "description": data.get("description"),
            "model": data.get("model"),
            "location": data.get("location"),
            "size": data.get("size"),
            "annotations": [output_json],
        }

        output_file = None
        if output == "asap":
            logger.info("+++ Generating ASAP XML Annotation")
            output_file = create_asap_annotations_xml(res_json, loglevel=loglevel)
        elif output == "dsa":
            logger.info("+++ Generating DSA JSON Annotation")
            output_file = create_dsa_annotations_json(res_json, loglevel=loglevel)
        else:
            logger.info("+++ Return Default JSON Annotation")

        return output_file, res_json
