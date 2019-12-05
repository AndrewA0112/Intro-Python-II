# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:

    def __init__(self, current_room):
        self.current_room = current_room
        self.items = []
        
    def get_current_room(self):
        return self.current_room

    def set_current_room(self, room):
        self.current_room = room

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items

    def __str__(self):
        return f"Inventory: {self.items}\nCurrent Room: {self.current_room}"
