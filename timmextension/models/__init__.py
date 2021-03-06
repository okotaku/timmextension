# flake8: noqa:F401
from .contnet import contnet_b, contnet_m
from .convmlp import convmlp_l, convmlp_m, convmlp_s
from .cvt import (cvt_13_224, cvt_13_384, cvt_13_384_22k, cvt_21_224,
                  cvt_21_384, cvt_21_384_22k, cvt_w24)
from .cyclemlp import (cyclemlp_b1, cyclemlp_b2, cyclemlp_b3, cyclemlp_b4,
                       cyclemlp_b5)
from .irpe import (deit_base_patch16_224_ctx_product_50_shared_qkv,
                   deit_small_patch16_224_ctx_product_50_shared_qkv)
from .lesa import lesa_resnet50, lesa_wrn50
from .resnet_dino import resnet50_dino
from .rexnetv1 import rexnet_10, rexnet_13, rexnet_15, rexnet_20, rexnet_30
from .shuffle_transformer import (shuffle_vit_base_patch4_window7_224,
                                  shuffle_vit_small_patch4_window7_224,
                                  shuffle_vit_tiny_patch4_window7_224)
# yapf:disable
from .swin_ssl import (swin_base_patch4_window7_224_in22k_ssl,
                       swin_base_patch4_window7_224_ssl,
                       swin_base_patch4_window12_384_in22k_ssl,
                       swin_base_patch4_window12_384_ssl,
                       swin_large_patch4_window7_224_in22k_ssl,
                       swin_large_patch4_window7_224_ssl,
                       swin_large_patch4_window12_384_in22k_ssl,
                       swin_large_patch4_window12_384_ssl,
                       swin_small_patch4_window7_224_ssl,
                       swin_tiny_patch4_window7_224_ssl)
# yapf:enable
from .vip import vip_l7, vip_m7, vip_s7, vip_s14
from .vit_dino import (vit_base_patch8_dino, vit_base_patch16_dino,
                       vit_small_patch8_dino, vit_small_patch16_dino,
                       vit_small_patch16_dino_landmark)
