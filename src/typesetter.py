import cv2

def draw_translation(image, bbox, text):

    x1,y1,x2,y2 = bbox

    center_x = (x1+x2)//2
    center_y = (y1+y2)//2

    cv2.putText(
        image,
        text,
        (center_x-100, center_y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0,0,0),
        2,
        cv2.LINE_AA
    )

    return image
