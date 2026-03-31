from .player import Player
import json


class Item:

    def __init__(self, item_name, item_type, price, effect_value=None, quantity=None):
        self.item_name = item_name
        self.item_type = item_type
        self.effect_value = effect_value
        self.price = price
        self.quantity = quantity

    @staticmethod
    def add_item(player: Player, item_name: str):
        with open(
            r"C:\dev\python_projects\terminal_quest\data\items.json", "r"
        ) as items_json:
            items = json.load(items_json)
            for item in items["items"]:
                if item["item_name"] == item_name:
                    added_item = Item(
                        item_name,
                        item["item_type"],
                        item["effect_value"],
                        item["price"],
                    )
                    player.inventory.append(added_item)

    def show_item_info(self):
        print(
            f"""
    Name: {self.item_name}
    Type: {self.item_type}
    Effect Value: {self.effect_value}
    Price: {self.price}
    """
        )

    def use_item(self):
        pass

    def __str__(self):
        return f"{self.item_name}"
