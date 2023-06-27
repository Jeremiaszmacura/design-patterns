import json


class AnalitycsLibrary():
    def __init__(self, data: str):
        self.data = json.loads(data)

    def __str__(self):
        return str(self.data)