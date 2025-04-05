import json
import os

class JsonHandler:
    def __init__(self, json_path, defauld_json):
        self.json_path = json_path

        directory = os.path.dirname(self.json_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        if not os.path.exists(self.json_path):
            with open(self.json_path, 'w') as file:
                json.dump(defauld_json, file, indent=4)

    def load(self):
        with open(self.json_path, 'r') as file:
            data = json.load(file)
        return data

    def dump(self, data):
        with open(self.json_path, 'w') as file:
            json.dump(data, file, indent=4)

user_json_handler = JsonHandler(
    json_path='src/data/user.json',
    defauld_json={
        "accounts": [],
        "latest_user": "None",
        "auto_login": False,
    })