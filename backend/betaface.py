import json


def get_facial_features(path: str) -> [int, json]:
    with open("demo-persona.json", "r") as file:
        data = json.load(file)
        return 0, data
