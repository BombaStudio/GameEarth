import json
import os


with open(os.path.dirname(__file__) + "/data/data.json", "r+") as f:
    data = json.load(f)