import pytest
import timm
import torch
from torch import nn
from torch.nn.modules.batchnorm import _BatchNorm

# todo: use timm backbone from mmcls
from timmextension import TIMMBackbone


def check_norm_state(modules, train_state):
    """Check if norm layer is in correct train state."""
    for mod in modules:
        if isinstance(mod, _BatchNorm):
            if mod.training != train_state:
                return False
    return True


@pytest.mark.parametrize('backbone,size', [('cvt_13_224', (1, 384)),
                                           ('cvt_13_384_22k', (1, 384)),
                                           ('cvt_13_384', (1, 384)),
                                           ('cvt_21_224', (1, 384)),
                                           ('cvt_21_384_22k', (1, 384)),
                                           ('cvt_21_384', (1, 384)),
                                           ('cvt_w24', (1, 1024))])
def test_timm_backbone(backbone, size):
    # Test from timm
    model = TIMMBackbone(model_name=backbone, pretrained=False)
    model.train()
    assert check_norm_state(model.modules(), True)

    imgs = torch.randn(1, 3, 224, 224)
    feat = model(imgs)
    assert len(feat) == 1
    assert feat[0].shape == torch.Size(size)

    # test reset_classifier
    model = timm.create_model(backbone, pretrained=False)
    assert not isinstance(model.head, nn.Identity)
    model.reset_classifier(0)
    assert isinstance(model.head, nn.Identity)
