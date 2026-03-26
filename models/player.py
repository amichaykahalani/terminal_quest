from models.girlfriend import GirlFriend


class Player:
    def __init__(self, name=""):
        self.name = name
        self.xp = 0
        self.level = 0
        self.hp = 0
        self.inventory = []
        self.girlfriend = GirlFriend()
        self.has_a_girlfriend = True

    def show_stats(self):
        print(
            f"""{self.name} Stats:
        XP: {self.xp}
        Level: {self.level}
        HP: {self.hp}
        Inventory: {self.inventory}
        Have a girlfriend: {self.has_a_girlfriend}"""
        )
