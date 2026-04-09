import cv2
import os

from bubble_detector import detect_bubbles
from ocr_engine import extract_text
from translator import translate
from cleaner import clean_bubble
from typesetter import draw_translation

INPUT = "../input"
OUTPUT = "../output"

for file in os.listdir(INPUT):

    if not file.endswith((".png",".jpg",".jpeg")):
        continue

    path = os.path.join(INPUT,file)

    image = cv2.imread(path)

    bubbles = detect_bubbles(path)

    for b in bubbles:

        x1,y1,x2,y2 = b

        crop = image[y1:y2,x1:x2]

        jp_text = extract_text(crop)

        en_text = translate(jp_text)

        image = clean_bubble(image,b)

        image = draw_translation(image,b,en_text)

    cv2.imwrite(os.path.join(OUTPUT,file),image)
