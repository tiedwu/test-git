import json

file = "camp_history.json"
with open(file, "r") as f:
	dict = json.load(f)
	print(dict)
	view_data = [{'index': k, 'content': dict[k]} for k in dict.keys()]
	print(view_data)
