import argparse
from ultralytics import YOLO
import os

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--model', default='yolov11s', help='pretrained model or config (use name like yolov11s to auto-download)')
    p.add_argument('--data', default='data/data.yaml')
    p.add_argument('--epochs', type=int, default=50)
    p.add_argument('--imgsz', type=int, default=640)
    p.add_argument('--project', default='outputs/runs')
    p.add_argument('--name', default='yolov11_lp')
    return p.parse_args()

def main():
    args = parse_args()
    os.makedirs(args.project, exist_ok=True)
    print('Loading model:', args.model)
    model = YOLO(args.model)
    print('Start training...')
    model.train(data=args.data, epochs=args.epochs, imgsz=args.imgsz,
                project=args.project, name=args.name)
    print('Training finished. Check outputs in', os.path.join(args.project, args.name))

if __name__ == '__main__':
    main()
