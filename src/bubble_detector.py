from ultralytics import YOLO
import cv2

model = YOLO("models/bubble_detector.pt")

def detect_bubbles(image_path):

    results = model(image_path)

    bubbles = []

    for r in results:
        for box in r.boxes.xyxy:
            x1, y1, x2, y2 = map(int, box)
            bubbles.append((x1,y1,x2,y2))

    return bubbles
