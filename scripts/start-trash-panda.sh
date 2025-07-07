#!/bin/bash

# === Trash Panda Blocker 9000 – Startup Script ===

echo "📹 Starting MJPEG stream..."
gst-launch-1.0 libcamerasrc ! \
  video/x-raw,width=1280,height=720,framerate=15/1 ! \
  videoconvert ! \
  videobalance ! \
  video/x-raw,format=I420 ! \
  jpegenc ! \
  multipartmux boundary=spionisto ! \
  tcpserversink host=0.0.0.0 port=8081 sync=false &
  
sleep 2

echo "🎯 Starting motion detection..."
python3 /home/pi/motion-detect.py
