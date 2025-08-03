# 🦝 Trash Panda Blocker 9000

A Raspberry Pi–powered motion-triggered raccoon deterrent system with live video streaming, servo-based deterrent activation, and AI-driven enhancements on the way.

## 💡 Creator’s Intent

Trash Panda Blocker 9000 was created to support the humane feeding of stray and feral cats while deterring raccoons from consuming resources intended for them. This project is not about harm, exclusion, or control—it’s about protection, balance, and compassionate problem-solving.

It began as a way to manage food costs and reduce loss from raccoon interference, but also as a tribute to a lost kitten and a beloved stepfather who found pride in building things that served others. What started as a tech project became a form of healing, grief management, and quiet resistance to apathy.

If you build upon or share this project, please do so with care—and always in a way that honors its core intent: **to protect life, not restrict it**.

---

## 🚀 Features

- Motion detection using OpenCV  
- MJPEG live streaming via GStreamer  
- Servo motor deterrent triggered on motion  
- Systemd autostart and hourly health checks  
- Future support for AI classification (cat vs. raccoon)  
- Lightweight and offline-capable

---

## 🧰 Hardware

- Raspberry Pi 4  
- Raspberry Pi Camera Module 3 NoIR  
- Servo motors (GPIO 18 and GPIO 13, PWM-capable)  
- USB power bank or wall adapter  
- Optional: external monitor for debugging  
- Weatherproof housing for outdoor use (IP65+ recommended)

---

## 📁 File Structure
trash-panda-blocker-9000/
├── bin/         # Shell scripts (startup, status check)
├── config/      # systemd unit files and timers
├── scripts/     # Python motion detection and core logic
├── web/         # MJPEG streaming server and interface
├── README.md
└── LICENSE

---

## 📸 Live Stream

Once deployed, view your stream locally at:  
**http://raspberrypi2.local:8081**

---

## 🧠 Coming Soon

- Object classification (cat vs. raccoon)
- Web dashboard with detection alerting
- Timed feeding access windows
- Detection-based activity logs and snapshots
- Humane deterrent timer logic

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