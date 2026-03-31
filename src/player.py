from .girlfriend import GirlFriend
from .entity import Entity
from .status import Status


class Player(Entity):
    def __init__(self, name=""):
        from .mission import Mission

        super().__init__(name)
        self.xp: int = 0
        self.level: int = 1
        self.hp: int = 100
        self.money: int = 0
        self.inventory: list = []
        self.missions: list = []
        self.current_mission: Mission = None
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

    def next_mission(self):
        from .mission import Mission

        mission: Mission
        for mission in self.missions:
            if mission.status == Status.AVAILABLE:
                if mission.start():
                    self.current_mission = mission
            break

    def sell_item(self, item_name):
        from .item import Item

        item: Item
        for item in self.inventory:
            if item.item_name.lower() == item_name:
                confirm_sell_string = f"Are you sure you want to sell {item.item_name} for {item.price} dollar? (yes / no): "
                if input(confirm_sell_string).lower() == "yes":
                    print(f"{item.item_name} sold for {item.price} dollars.")
                    self.money += item.price
                    self.inventory.remove(item)
                else:
                    pass
