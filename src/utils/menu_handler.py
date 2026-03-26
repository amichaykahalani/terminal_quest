from src.player import Player
import sys


class MenuManager:
    def __init__(self):
        self.current_options = {1: "View Stats", 2: "Take the next task", 3: "Exit"}
        self.system_message = ""

    def show_menu(self):
        for option, text in self.current_options.items():
            print(f"{option}. {text}")

    # Avior I have a problem. Why its keep printing "1" if i send "2"?
    # Problem solved.
    def action(self, player, option):
        actions = {
            "1": self.view_stats,
            "2": self.take_next_task,
            "3": self.exit,
        }
        func = actions.get(option, self.exit)
        func(player)

    def view_stats(self, player: Player):
        player.show_stats()

    def take_next_task(self, player: Player):
        print("NEXT TASK:")

    def exit(self, player: Player):
        sys.exit()
