from transformers import VisionEncoderDecoderModel
from transformers import ViTImageProcessor
from transformers import AutoTokenizer
from PIL import Image
import torch

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

print("Loading model...")

model = VisionEncoderDecoderModel.from_pretrained(
    "nlpconnect/vit-gpt2-image-captioning"
)

image_processor = ViTImageProcessor.from_pretrained(
    "nlpconnect/vit-gpt2-image-captioning"
)

tokenizer = AutoTokenizer.from_pretrained(
    "nlpconnect/vit-gpt2-image-captioning"
)

model.to(device)

print("Model loaded!")


def generate_caption(image_path):
    img = Image.open(image_path).convert("RGB")

    pixels = image_processor(
        images=img,
        return_tensors="pt"
    ).pixel_values

    pixels = pixels.to(device)

    output = model.generate(
        pixels,
        max_length=20,
        num_beams=4
    )

    caption = tokenizer.decode(
        output[0],
        skip_special_tokens=True
    )

    return caption