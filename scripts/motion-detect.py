# scripts/motion-detect.py

import cv2
import time
import pigpio

# === Servo Setup ===
SERVO_GPIO = 18  # Adjust if using different pin
SERVO_MIN = 500  # microseconds
SERVO_MAX = 2500  # microseconds
COOLDOWN_SECONDS = 60  # Cooldown between detections

print("🔧 Connecting to PiGPIO daemon...")
pi = pigpio.pi()
if not pi.connected:
    print("❌ Failed to connect to pigpiod.")
    exit()

print("🔧 Initializing servo...")
pi.set_servo_pulsewidth(SERVO_GPIO, 0)

# === Camera Setup ===
print("📷 Initializing camera...")
gst_str = (
    "libcamerasrc ! "
    "video/x-raw,width=640,height=480,framerate=30/1 ! "
    "videoconvert ! "
    "appsink"
)

cap = cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)
if not cap.isOpened():
    print("❌ Failed to open camera.")
    pi.stop()
    exit()

ret, frame1 = cap.read()
ret2, frame2 = cap.read()
if not ret or not ret2:
    print("❌ Failed to read initial frames.")
    cap.release()
    pi.stop()
    exit()

print("🎯 Motion detection running...")
last_detection_time = 0

try:
    while True:
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        now = time.time()
        if contours and now - last_detection_time > COOLDOWN_SECONDS:
            print("👀 Motion detected!")
            pi.set_servo_pulsewidth(SERVO_GPIO, SERVO_MAX)
            time.sleep(0.5)
            pi.set_servo_pulsewidth(SERVO_GPIO, SERVO_MIN)
            time.sleep(0.5)
            pi.set_servo_pulsewidth(SERVO_GPIO, 0)
            last_detection_time = now

        frame1 = frame2
        ret, frame2 = cap.read()
        if not ret:
            print("❌ Failed to read next frame.")
            break

        time.sleep(0.1)

except KeyboardInterrupt:
    print("🛑 Interrupted by user. Cleaning up...")

finally:
    cap.release()
    pi.set_servo_pulsewidth(SERVO_GPIO, 0)
    pi.stop()
    print("✅ Motion detection stopped and resources released.")
