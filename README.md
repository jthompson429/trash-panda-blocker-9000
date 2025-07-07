# 🦝 Trash Panda Blocker 9000

A Raspberry Pi–powered motion-triggered raccoon deterrent system with live video streaming, servo-based deterrent activation, and AI-driven enhancements on the way.

---

## 🚀 Features

- Motion detection using OpenCV
- MJPEG live streaming via GStreamer
- Servo motor deterrent triggered on motion
- Systemd autostart and hourly health checks
- Future plans for raccoon vs. cat recognition and timed access

---

## 🧰 Hardware

- Raspberry Pi 4
- Raspberry Pi Camera Module 3 NoIR
- Servo motor (GPIO 18, PWM-capable)
- USB power bank or wall adapter
- Optional: external monitor for debugging

---

## 🗃️ File Structure
📁 trash-panda-blocker-9000
├── bin/                  # Shell scripts (startup, status check)
├── config/               # .service unit files
├── scripts/              # Python motion detection and core logic
├── web/                  # MJPEG streaming web server
├── README.md
└── LICENSE

---

## 📸 Live Stream

Once deployed, view your stream at:
http://raspberrypi2.local:8081

---

## 🧠 Coming Soon

- Object classification (cat vs. raccoon)
- Web dashboard and alerting system
- Timed feeding access
- Activity logs and detection snapshots

  
