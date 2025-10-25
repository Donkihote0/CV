\
@echo off
REM Usage: run_realtime.bat "http://192.168.0.101:8080/video"
if "%1"=="" (
    python src/capture_phone_cam.py --model models/yolov11s.pt --source 0
) else (
    python src/capture_phone_cam.py --model models/yolov11s.pt --source "%1"
)
