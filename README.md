# 🦝 Trash Panda Blocker 9000

A Raspberry Pi–powered, motion-triggered AI deterrent system designed to keep raccoons out of your cat food. Features real-time object classification, servo-based food protection, live MJPEG video streaming, weatherproof hardware, and a growing suite of smart detection tools.

---

## 💡 Creator’s Intent

**Trash Panda Blocker 9000** was created to support the humane feeding of stray and feral cats while deterring raccoons from consuming resources intended for them. This project is not about harm, exclusion, or control—it’s about protection, balance, and compassionate problem-solving.

It began as a practical way to manage food costs and reduce loss from raccoon interference. But it quickly became something more: a tribute to a lost kitten and a stepfather who took pride in building things that served others. What started as a tech project became a form of healing, grief management, and quiet resistance to indifference.

If you build upon or share this project, please do so with care—and always in a way that honors its core intent: **to protect life, not restrict it.**

---

## 🚀 Features

- Motion detection using OpenCV with tuned sensitivity  
- MJPEG live streaming with overlay text (timestamp, CPU temp, and a signature message)  
- Raccoon vs. cat image classification via custom TFLite model  
- Dual-servo deterrent lid system with mirrored rotation and cooldown logic  
- Snapshot capture with classification label and timestamped event logging  
- Systemd-based autostart and hourly watchdog health check  
- Adjustable camera angle via script or servo bracket  
- Sunwait integration: starts at dusk, stops at dawn  
- USB-C weatherproof power + safe AC conduit and outdoor outlet support  

---

## 🧰 Hardware

- Raspberry Pi 4 or 5  
- Raspberry Pi Camera Module 3 NoIR  
- 2× MG996R servo motors (GPIO 18 and GPIO 13)  
- Weatherproof Pi enclosure with ventilation and fan  
- Servo extension wires, turnbuckles, mounting brackets  
- USB-C external port for sealed charging  
- Outdoor Leviton dual USB + 120V outlet with conduit feed  

---

## 🗃️ File Structure
trash-panda-blocker-9000/
├── scripts/       # Core Python code (motion, classification, streaming)
├── snapshots/     # Saved detection images
├── templates/     # HTML index template for live stream
├── systemd/       # .service and .timer files for daemon setup
├── DOCS/          # Bash snippets and startup instructions
├── LICENSE
└── README.md
---

## 📸 Live Stream

Once deployed and running, view the real-time stream at:  
**http://raspberrypi2.local:5000**

---

## 📈 AI Classifier Info

- Uses `cat_raccoon.tflite` to distinguish between cats and raccoons  
- Confidence threshold: 70%  
- Snapshots and logs are only created if:
  - Motion is detected, **and**  
  - Classification confidence exceeds threshold  

---

## 🧠 Coming Soon

- Possum detection model expansion  
- Auto-labeling retrain set generator  
- Web dashboard for reviewing event history  
- Servo-driven camera gimbal (manual or script-adjustable)  
- Optional deterrent scheduling and timed access windows  

---

## ⚖️ License & Usage

This project is released under the **[Insert License Name Here]**, with the following ethical use guidance:

- ✅ **Permitted**: Humane, non-commercial use to support animal welfare, feeding station management, research, or personal learning  
- ❌ **Not Permitted**: Use for profit, animal harm, exclusionary surveillance, or systems designed to restrict access to food, care, or resources

If you build on this project or adapt it for new use cases, please credit the original creator—and always honor the spirit in which it was built.

---

## 🌍 Archived & Authenticated

The contents of this project are archived in public repositories to ensure provenance, transparency, and protection against unethical repurposing. This version reflects the original intent of the creator and is timestamped accordingly.

---

## 🤝 Contribute or Contact

If you're interested in contributing to this project or adapting it for another humane purpose, feel free to fork it—or reach out with feedback, questions, or ideas.  

**Last updated: 2025-08-03**