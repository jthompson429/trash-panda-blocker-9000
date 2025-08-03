# 🦝 Trash Panda Blocker 9000

A Raspberry Pi–powered motion-triggered AI deterrent system designed to keep raccoons out of your cat food. Features real-time object classification, servo-based food protection, live MJPEG video streaming, weatherproof hardware, and a growing suite of smart detection tools.

---

## 💡 Creator’s Intent

Trash Panda Blocker 9000 was created to support the humane feeding of stray and feral cats while deterring raccoons from consuming resources intended for them. This project is not about harm, exclusion, or control—it’s about protection, balance, and compassionate problem-solving.

It began as a way to manage food costs and reduce loss from raccoon interference, but also as a tribute to a lost kitten and a beloved stepfather who found pride in building things that served others. What started as a tech project became a form of healing, grief management, and quiet resistance to apathy.

If you build upon or share this project, please do so with care—and always in a way that honors its core intent: **to protect life, not restrict it**.

---

## 🚀 Features

- Motion detection using OpenCV with reduced sensitivity
- MJPEG live streaming with overlay text (timestamp, CPU temp, signature message)
- Raccoon vs. Cat image classification via TFLite model
- Dual-servo deterrent lid system with coordinated rotation and cooldown
- Snapshot capture with labeling and event logging
- Systemd autostart and hourly watchdog health check
- Adjustable camera angle via script or servo bracket
- USB-C weatherproof power + safe AC conduit and outdoor outlet support

---

## 🧰 Hardware

- Raspberry Pi 4 or Pi 5
- Raspberry Pi Camera Module 3 NoIR
- 2x MG996R servo motors (GPIO 18 and GPIO 13)
- Weatherproof Pi enclosure with ventilation and fan
- Servo extension wires, turnbuckles, mounting brackets
- USB-C external port for sealed charging
- Outdoor Leviton dual USB + 120V outlet with conduit feed

---

## 🗃️ File Structure

```
📁 trash-panda-blocker-9000
├── scripts/              # Core Python code (motion, classification, streaming)
├── snapshots/            # Saved detection images
├── templates/            # HTML index template for live stream
├── systemd/              # .service and .timer files for daemon setup
├── DOCS/                 # Bash snippets and startup instructions
├── LICENSE
└── README.md
```

---

## 📸 Live Stream

Once deployed and running, you can view the real-time stream at:  
**http://raspberrypi2.local:5000**

---

## 📈 AI Classifier Info

- TFLite model (`cat_raccoon.tflite`) classifies between cat and raccoon
- Confidence threshold: 70%
- Snapshots are logged and saved only when motion is confirmed and classification confidence is high

---

## 🧠 Coming Soon

- Expanded classification model with possum detection
- Auto-labeling retrain set generator
- Web dashboard for reviewing past events
- Servo-driven camera gimbal (manual or script-adjustable)
- Optional deterrent timer scheduling and feeding windows

---

## ⚖️ License & Usage

This project is released under the **[Insert License Name Here]**, with the following ethical use guidance:

- ✅ **Permitted**: Humane, non-commercial use to support animal welfare, feeding station management, research, or personal learning.
- ❌ **Not Permitted**: Use for profit, animal harm, exclusionary surveillance, or systems designed to restrict resources to living beings in need.

If you'd like to use this project or build on it for other applications, please be mindful of the original purpose—and credit the creator wherever possible.

---

## 🌍 Archived & Authenticated

The contents of this project are archived in public repositories to ensure provenance, transparency, and to protect against unethical repurposing. This version reflects the original intent of the creator and is timestamped accordingly.

---

## 🤝 Contribute or Contact

If you're interested in contributing to this project or adapting it for another humane use case, feel free to fork it—or reach out with questions or feedback.
_Last updated: 2025-08-03_