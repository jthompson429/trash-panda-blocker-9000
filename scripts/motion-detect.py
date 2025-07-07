#!/usr/bin/env python3

import cv2
import time
import pigpio
from datetime import datetime

# === Config ===
SERVO_GPIO = 18
SERVO_MIN = 500
SERVO_MAX = 2500
COOLDOWN_SECONDS = 60  # Production-level cooldown between servo triggers

# === Initialize pigpio ===
print("🔧 Connecting to PiGPIO daemon...")
pi = pigpio.pi()
if not pi.connected:
    print("❌ Failed to connect to pigpiod.")
    exit()

print("🔧 Initializing servo...")
pi.set_servo_pulsewidth(SERVO_GPIO, 0)

# === Initialize camera ===
print("📷 Initializing camera...")
gst_str = (
    "libcamerasrc ! "
    "video/x-raw,width=640,height=480,framerate=30/1 ! "
    "videoconvert ! "
    "appsink"
)
cap = cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)
print("Camera opened:", cap.isOpened())

ret, frame1 = cap.read()
ret, frame2 = cap.read()

# === Motion Detection Loop ===
print("🎯 Motion detection running...")
last_trigger = 0

try:
    while True:
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if contours and (time.time() - last_trigger) > COOLDOWN_SECONDS:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"👀 Motion detected! [{timestamp}]")

            pi.set_servo_pulsewidth(SERVO_GPIO, SERVO_MAX)
            time.sleep(0.5)
            pi.set_servo_pulsewidth(SERVO_GPIO, SERVO_MIN)
            time.sleep(0.5)
            pi.set_servo_pulsewidth(SERVO_GPIO, 0)

            last_trigger = time.time()

        frame1 = frame2
        ret, frame2 = cap.read()
        if not ret:
            print("❌ Failed to read next frame")
            break

        time.sleep(0.1)

except KeyboardInterrupt:
    print("🛑 Interrupted by user. Cleaning up...")

finally:
    cap.release()
    pi.set_servo_pulsewidth(SERVO_GPIO, 0)
    pi.stop()
    print("✅ Motion detection stopped and resources released.")
