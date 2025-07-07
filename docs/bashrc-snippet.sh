# Trash Panda Blocker 9000 greeting
if [ "$(tty)" = "/dev/tty1" ] || [ -n "$SSH_CONNECTION" ]; then
  echo -e "\n👋 Welcome, pi! Raspberry Pi is ready."
  echo -e "💡 Run 'status-check' for Trash Panda Blocker 9000 system overview.\n"
fi
