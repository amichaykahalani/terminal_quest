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
        XP: {self.xp}
        Level: {self.level}
        HP: {self.hp}
        Money: {self.money}$
        Inventory: {self.inventory}
        Has a girlfriend: {self.has_a_girlfriend}"""
        )
