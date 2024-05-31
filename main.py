from PIL import Image
from pillow_heif import register_heif_opener
import os

register_heif_opener()

files = [i for i in os.listdir("inputs") if i.endswith(".HEIC") or i.endswith(".heic")]

for i in files:
    image = Image.open(os.path.join("inputs", i))

    if i.endswith(".HEIC"):
        image.save(os.path.join("outputs", i.replace(".HEIC", ".jpg")))
    elif i.endswith(".heic"):
        image.save(os.path.join("outputs", i.replace(".heic", ".jpg")))