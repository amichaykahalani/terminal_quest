from src.player import Player
import sys


class MenuManager:
    def __init__(self):
        self.current_options = {
            1: "View Player Info",
            2: "Show Inventory Options",
            3: "Current Mission",
            4: "Next Mission",
            5: "Exit",
        }
        self.is_inside_inventory = False

    def show_game_menu(self):
        print()
        for option, text in self.current_options.items():
            print(f"{option}. {text}")
        print()

    # Avior I have a problem. Why its keep printing "1" if i send "2"?
    # Problem solved.
    def action(self, player, option):
        print()
        if self.is_inside_inventory:
            item_name = input("Enter item name: ")
            actions = {
                "1": player.show_item_info,
                "2": player.use_item,
                "3": player.sell_item,
            }
            func = actions.get(option, self.exit)
            func(item_name)
            self.is_inside_inventory = False
        else:
            actions = {
                "1": self.view_stats,
                "2": self.show_inventory_menu,
                "3": self.show_current_mission,
                "4": self.next_mission_for_player,
                "5": self.exit,
            }
            func = actions.get(option, self.exit)
            func(player)

    def view_stats(self, player: Player):
        player.show_stats()

    def next_mission_for_player(self, player: Player):
        print("Next Mission:")
        print("---------------")
        player.next_mission()

    def exit(self, player: Player):
        sys.exit()

    def show_inventory_menu(self, player: Player):
        self.is_inside_inventory = True
        self.inventory_options = {1: "Show Item Info", 2: "Use Item", 3: "Sell Item"}
        for option, text in self.inventory_options.items():
            print(f"{option}. {text}")
        print()

        chosen_option = input("Enter option: ")

        self.action(player, chosen_option)

    def show_current_mission(self, player: Player):
        if player.current_mission:
            print(f"""Current Mission: {player.current_mission.description}""")
        else:
            print("You should take the next mission.")
