# Few imports

import torch
from torch import nn
import torch.nn.functional as F
from torchvision import transforms
import torchvision.models as models


# Model

class ResNet(nn.Module):
    def __init__(self):
        super(ResNet, self).__init__()
        self.resnet = models.resnet34(pretrained=True)
        for param in self.resnet.parameters():
            param.requires_grad = False
        self.resnet.fc = nn.Linear(self.resnet.fc.in_features, 2)

    def forward(self, input):
        return self.resnet(input)


# Load model weights

def load_checkpoint(filepath):
    model = ResNet()
    model.load_state_dict(torch.load(filepath, map_location='cpu'))
    return model


# Feed image to the model

def get_prediction(image):
    test_transforms = transforms.Compose(
        [transforms.Resize((256, 256)), transforms.ToTensor()])
    image_tensor = test_transforms(image)
    image_tensor = image_tensor.unsqueeze_(0)
    model = load_checkpoint(PATH)
    outputs = model(image_tensor)
    _, predicted = torch.max(outputs.data, 1)
    return ["Cat", "Dog"][predicted.item()]


PATH = 'app/model.pth'
