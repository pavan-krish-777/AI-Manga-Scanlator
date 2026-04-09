from manga_ocr import MangaOcr
from PIL import Image

mocr = MangaOcr()

def extract_text(image_crop):

    pil_image = Image.fromarray(image_crop)

    text = mocr(pil_image)

    return text
