import json


class PostDAO:
    def __init__(self, source):
        self.source = source
        with open(source, 'r', encoding='utf-8') as file:
            items = json.load(file)
        self.items = items

    def get_all(self):
        return self.items

    def get_one(self, pk):
        for item in self.items:
            if item['pk'] == pk:
                return item
