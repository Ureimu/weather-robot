import json

def get_pythonlic_json(json_text):
    text = json.load(json_text)
    print(text)
