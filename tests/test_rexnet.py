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


@pytest.mark.parametrize('backbone,size', [('rexnet_10', (2, 1280, 7, 7)),
                                           ('rexnet_13', (2, 1664, 7, 7)),
                                           ('rexnet_15', (2, 1920, 7, 7)),
                                           ('rexnet_20', (2, 2560, 7, 7)),
                                           ('rexnet_30', (2, 3840, 7, 7))])
def test_timm_backbone(backbone, size):
    # Test from timm
    model = TIMMBackbone(model_name=backbone, pretrained=False)
    model.train()
    assert check_norm_state(model.modules(), True)

    imgs = torch.randn(2, 3, 224, 224)
    feat = model(imgs)
    assert len(feat) == 1
    assert feat[0].shape == torch.Size(size)

    # test reset_classifier
    model = timm.create_model(backbone, pretrained=False)
    assert not isinstance(model.output, nn.Identity)
    model.reset_classifier(0)
    assert isinstance(model.output, nn.Identity)


@pytest.mark.parametrize('backbone', [('rexnet_10'), ('rexnet_13'),
                                      ('rexnet_15'), ('rexnet_20'),
                                      ('rexnet_30')])
def test_features_only(backbone):
    # Test all out_indices from timm
    model = timm.create_model(backbone,
                              pretrained=False,
                              features_only=True,
                              out_indices=(0, 1, 2, 3))

    imgs = torch.randn(2, 3, 224, 224)
    feat = model(imgs)
    assert len(feat) == 4
    for f, c, r in zip(feat, model.feature_info.channels(),
                       model.feature_info.reduction()):
        assert f.shape == torch.Size((2, c, 224 // r, 224 // r))

    # Test picked out_indices from timm
    model = timm.create_model(backbone,
                              pretrained=False,
                              features_only=True,
                              out_indices=(2, 3))

    imgs = torch.randn(2, 3, 224, 224)
    feat = model(imgs)
    assert len(feat) == 2
    for f, c, r in zip(feat, model.feature_info.channels(),
                       model.feature_info.reduction()):
        assert f.shape == torch.Size((2, c, 224 // r, 224 // r))