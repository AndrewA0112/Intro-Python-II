# Implement a class to hold room information. This should have name and
# description attributes.
class Room:

    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
    
    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items

    def __str__(self):
        return f"{self.name}\n{self.description}\n{self.items}"