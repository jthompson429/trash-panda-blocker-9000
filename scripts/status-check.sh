#!/bin/bash

echo "🦝  Trash Panda Blocker 9000 - System Status Overview"
echo "─────────────────────────────────────────────────────"
echo "📅  Date/Time       : $(date)"
echo "📡  Hostname        : $(hostname)"
echo "📶  IP Address      : $(hostname -I | awk '{print $1}')"
echo ""

# MJPEG stream status
echo "🎥  MJPEG Stream Status:"
STREAM_PORT=8081
if ss -tuln | grep ":$STREAM_PORT" &>/dev/null; then
    echo "   ✅ MJPEG stream appears to be running on port $STREAM_PORT"
else
    echo "   ❌ MJPEG stream not detected on port $STREAM_PORT"
fi

# Motion detection service
echo ""
echo "🎯  Motion Detection Status:"
if pgrep -f motion-detect.py > /dev/null; then
    echo "   ✅ motion-detect.py is running"
else
    echo "   ❌ motion-detect.py is NOT running"
fi

# Servo test (optional pulse check)
echo ""
echo "🛠️  PiGPIO Daemon Status:"
if systemctl is-active --quiet pigpiod; then
    echo "   ✅ pigpiod is active"
else
    echo "   ❌ pigpiod is NOT running"
fi

# System uptime
echo ""
echo "⏱️  System Uptime    : $(uptime -p)"
echo ""
