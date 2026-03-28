from src.player import Player
import sys


class MenuManager:
    def __init__(self):
        self.current_options = {
            1: "View Player Info",
            2: "Show Inventory Options",
            3: "Take the next task",
            4: "Exit",
        }
        self.is_inside_inventory = False

    def show_game_menu(self):
        for option, text in self.current_options.items():
            print(f"{option}. {text}")

    # Avior I have a problem. Why its keep printing "1" if i send "2"?
    # Problem solved.
    def action(self, player, option):
        if self.is_inside_inventory:
            item_name = input("Enter item name: ")
            actions = {"1": player.show_item_info, "2": player.use_item}
            func = actions.get(option, self.exit)
            func(item_name)
            self.is_inside_inventory = False
        else:
            actions = {
                "1": self.view_stats,
                "2": self.show_inventory_menu,
                "3": self.take_a_task,
                "4": self.exit,
            }
            func = actions.get(option, self.exit)
            func(player)

    def view_stats(self, player: Player):
        player.show_stats()

    def take_a_task(self, player: Player):
        print("NEXT TASK:")

    def exit(self, player: Player):
        sys.exit()

    def show_inventory_menu(self, player: Player):
        self.is_inside_inventory = True
        self.inventory_options = {1: "Show Item Info", 2: "Use Item"}
        for option, text in self.inventory_options.items():
            print(f"{option}. {text}")

        chosen_option = input()

        self.action(player, chosen_option)
