
import json

file = "user_data.json"

with open(file, "r") as f:
    data = json.load(f)
    print(data)
