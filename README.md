# YOLOv11 Vietnam License Plate Recognition

This archive contains a ready-to-run project scaffold for detecting Vietnamese license plates
using YOLOv11 (Ultralytics). It's prepared for running locally on Windows with Python.

**Important:** The actual pretrained weight `yolov11s.pt` is *NOT* included due to file-size and licensing.
A small placeholder is provided; download the real `yolov11s.pt` from Ultralytics and place it in `models/`.

## Quick start (Windows local)
1. Create and activate a Python environment (recommended).
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Download `yolov11s.pt` from Ultralytics and put it in `models/`:
   - Official repo/releases: https://github.com/ultralytics/assets/releases
   - Put the file path: `yolov11_vn_license_plate/models/yolov11s.pt`
4. Run a quick training dry-run (or actual training):
   ```
   python src/train.py --model yolov11s --epochs 1 --imgsz 320
   ```
   Note: using `--model yolov11s` will let Ultralytics auto-download if needed.
5. Test detection on demo images:
   ```
   python src/detect.py --model models/yolov11s.pt --source data/valid/images --save
   ```
6. Run realtime from IP Webcam on your phone (example):
   ```
   python src/capture_phone_cam.py --model models/yolov11s.pt --source "http://192.168.0.101:8080/video"
   ```

## Contents
- `src/` : training, detect, and capture scripts.
- `data/` : small demo images and labels (very small toy examples).
- `models/` : contains a placeholder file; replace with real `yolov11s.pt`.
- `configs/` : model yaml example.
- `requirements.txt` and this README.

