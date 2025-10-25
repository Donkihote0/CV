import argparse
import cv2
from ultralytics import YOLO

parser = argparse.ArgumentParser()
parser.add_argument('--model', default='models/yolov11s.pt')
parser.add_argument('--source', default='0', help='0 for local cam or http link for IP webcam')
parser.add_argument('--show', action='store_true', default=True)
args = parser.parse_args()

model = YOLO(args.model)

try:
    source = int(args.source)
except:
    source = args.source

cap = cv2.VideoCapture(source)
if not cap.isOpened():
    raise RuntimeError(f'Cannot open source {args.source}')

while True:
    ret, frame = cap.read()
    if not ret:
        print('Frame not received, exiting...')
        break
    results = model(frame)
    annotated = results[0].plot()
    if args.show:
        cv2.imshow('LP Detect', annotated)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
