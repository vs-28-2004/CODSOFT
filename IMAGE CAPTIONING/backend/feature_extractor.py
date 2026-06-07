# feature_extractor.py

import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image

model = models.resnet50(
    weights=models.ResNet50_Weights.DEFAULT
)

model = torch.nn.Sequential(
    *list(model.children())[:-1]
)

model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])


def extract_feature(image_path):
    img = Image.open(image_path).convert("RGB")

    img = transform(img)

    img = img.unsqueeze(0)

    with torch.no_grad():
        features = model(img)

    return features.squeeze()