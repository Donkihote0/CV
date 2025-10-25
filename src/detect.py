import argparse
from ultralytics import YOLO

parser = argparse.ArgumentParser()
parser.add_argument('--model', default='models/yolov11s.pt')
parser.add_argument('--source', default='data/valid/images')
parser.add_argument('--save', action='store_true')
args = parser.parse_args()

model = YOLO(args.model)
print('Running detect on', args.source)
results = model.predict(source=args.source, save=args.save)
print('Done.')
