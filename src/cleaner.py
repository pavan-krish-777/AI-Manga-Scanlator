import cv2
import numpy as np

def clean_bubble(image, bbox):

    x1,y1,x2,y2 = bbox

    bubble = image[y1:y2, x1:x2]

    mask = cv2.threshold(
        cv2.cvtColor(bubble, cv2.COLOR_BGR2GRAY),
        200,
        255,
        cv2.THRESH_BINARY_INV
    )[1]

    cleaned = cv2.inpaint(
        bubble,
        mask,
        3,
        cv2.INPAINT_TELEA
    )

    image[y1:y2, x1:x2] = cleaned

    return image
