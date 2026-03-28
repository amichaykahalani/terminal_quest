from .girlfriend import GirlFriend
import typing


class Player:
    def __init__(self, name=""):
        self.name: str = name
        self.xp: int = 0
        self.level: int = 0
        self.hp: int = 100
        self.money: int = 0
        self.inventory: list = []
        self.girlfriend: GirlFriend = GirlFriend()
        self.has_a_girlfriend: bool = True

    def show_stats(self):
        print(
            f"""{self.name} Stats:
    #----------------
    XP: {self.xp}
    Level: {self.level}
    HP: {self.hp}
    Money: {self.money}$
    Has a girlfriend: {self.has_a_girlfriend}
    #----------------
    Inventory: [""",
            end="",
        )
        self.print_inventory()

    def print_inventory(self):
        for item in self.inventory:
            print(item, end=" ")
        print("]")

    def show_item_info(self, item_name):
        for item in self.inventory:
            if item.item_name.lower() == item_name:
                item.show_item_info()

    def use_item(self, item_name):
        for item in self.inventory:
            if item.item_name.lower() == item_name:
                self.inventory.remove(item)
