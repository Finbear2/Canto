import json
import os

SETTINGS = {}

fileLoc = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")

with open(fileLoc, "rb") as f:
    SETTINGS = json.load(f)