#!/usr/bin/env python3

# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

import torch
from .lookup_args import *



#import os
#torch.ops.load_library(os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), "fbgemm_gpu_py.so")))



def invoke(
    common_args: CommonArgs,
    optimizer_args: OptimizerArgs,
    
    
    
) -> torch.Tensor:
    if (common_args.host_weights.numel() > 0):
        return torch.ops.fbgemm.split_embedding_codegen_lookup_approx_sgd_function_cpu(
            # common_args
            host_weights=common_args.host_weights,
            weights_placements=common_args.weights_placements,
            weights_offsets=common_args.weights_offsets,
            D_offsets=common_args.D_offsets,
            total_D=common_args.total_D,
            max_D=common_args.max_D,
            hash_size_cumsum=common_args.hash_size_cumsum,
            total_hash_size_bits=common_args.total_hash_size_bits,
            indices=common_args.indices,
            offsets=common_args.offsets,
            pooling_mode=common_args.pooling_mode,
            indice_weights=common_args.indice_weights,
            feature_requires_grad=common_args.feature_requires_grad,
            # optimizer_args
            gradient_clipping = optimizer_args.gradient_clipping,
            max_gradient=optimizer_args.max_gradient,
            stochastic_rounding=optimizer_args.stochastic_rounding,
            
            learning_rate=optimizer_args.learning_rate,
            
            
            
            
            
            
            
            
            # momentum1
            
            # momentum2
            
            # iter
            
        )
    else:
        return torch.ops.fbgemm.split_embedding_codegen_lookup_approx_sgd_function(
            # common_args
            
            placeholder_autograd_tensor=common_args.placeholder_autograd_tensor,
            
            dev_weights=common_args.dev_weights,
            uvm_weights=common_args.uvm_weights,
            lxu_cache_weights=common_args.lxu_cache_weights,
            weights_placements=common_args.weights_placements,
            weights_offsets=common_args.weights_offsets,
            D_offsets=common_args.D_offsets,
            total_D=common_args.total_D,
            max_D=common_args.max_D,
            hash_size_cumsum=common_args.hash_size_cumsum,
            total_hash_size_bits=common_args.total_hash_size_bits,
            indices=common_args.indices,
            offsets=common_args.offsets,
            pooling_mode=common_args.pooling_mode,
            indice_weights=common_args.indice_weights,
            feature_requires_grad=common_args.feature_requires_grad,
            lxu_cache_locations=common_args.lxu_cache_locations,
            # optimizer_args
            gradient_clipping = optimizer_args.gradient_clipping,
            max_gradient=optimizer_args.max_gradient,
            stochastic_rounding=optimizer_args.stochastic_rounding,
            
            learning_rate=optimizer_args.learning_rate,
            
            
            
            
            
            
            
            
            # momentum1
            
            # momentum2
            
            # iter
            
            output_dtype=common_args.output_dtype,
        )