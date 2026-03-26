from .player import Player
import json


class Item:

    def __init__(self, item_name, item_type, effect_value, quantity):
        self.item_name = item_name
        self.item_type = item_type
        self.effect_value = effect_value
        self.quantity = quantity

    @staticmethod
    def add_item(player: Player, item_name: str):
        with open(
            r"C:\dev\python_projects\terminal_quest\data\items.json", "r"
        ) as items_json:
            items = json.load(items_json)
            for item in items["items"]:
                if item["item_name"] == item_name:
                    player.inventory.append(item_name)

    def use_item(self):
        pass
