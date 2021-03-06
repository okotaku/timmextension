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


@pytest.mark.parametrize('backbone,size',
                         [('vit_small_patch16_dino', (1, 384)),
                          ('vit_small_patch16_dino_landmark', (1, 384)),
                          ('vit_small_patch8_dino', (1, 384)),
                          ('vit_base_patch16_dino', (1, 768)),
                          ('vit_base_patch8_dino', (1, 768))])
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
    model = timm.create_model(backbone, pretrained=False, num_classes=1000)
    assert not isinstance(model.head, nn.Identity)
    model.reset_classifier(0)
    assert isinstance(model.head, nn.Identity)
