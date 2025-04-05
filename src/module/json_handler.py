import json
import os

class JsonHandler:
    def __init__(self, json_path, default_json):
        self.json_path = json_path
        self.default_json = default_json

        self.setup()
        self.load()

    def load(self):
        try:
            with open(self.json_path, 'r') as file:
                self.data = json.load(file)

        except json.JSONDecodeError:
            print(f"Error decoding JSON from {self.json_path}. Using default JSON.")
            self.data = self.default_json
            self.dump()

    def dump(self):
        with open(self.json_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def setup(self):
        directory = os.path.dirname(self.json_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        if not os.path.exists(self.json_path):
            with open(self.json_path, 'w') as file:
                json.dump(self.default_json, file, indent=4)

accounts_json_handler = JsonHandler(
    json_path='src/data/accounts.json',
    default_json=[]
)

current_user_json_handler = JsonHandler(
    json_path='src/data/current_user.json',
    default_json={
        "current_user": None,
        "auto_login": False,
    }
)

user_data_json_handler = JsonHandler(
    json_path='src/data/user_data.json',
    default_json=[]
)
    