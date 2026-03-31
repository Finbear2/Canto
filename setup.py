import sys
import os

# [Unit]
# Description=Canto
# After=network.target

# [Service]
# # Change these!
# ExecStart=/usr/bin/python3.11 /path/to/your/script.py
# Restart=always
# User=youruser
# WorkingDirectory=/path/to/your/project/

# [Install]
# WantedBy=multi-user.target

sys.path.append(os.path.join(os.path.dirname(__file__), "code"))

from funcs import logo

logo()

# with open("canto.service", "w") as f:
#     f.write("Test")