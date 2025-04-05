import json

class JsonHandler:
    def __init__(self, json_path):
        self.json_path = json_path

    def readJson(self):
        with open(self.json_path, 'r') as file:
            data = json.load(file)
        return data

    def writeJson(self, data):
        with open(self.json_path, 'w') as file:
            json.dump(data, file, indent=4)

user_json_handler = JsonHandler('src/data/user.json')