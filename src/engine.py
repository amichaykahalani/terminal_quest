from .player import Player
from .utils.menu_handler import MenuManager
from .item import Item
import threading
import time


class GameEngine:

    def __init__(self):
        self.player = Player()
        self.is_doing_task = True

    def run(self):
        # app logic goes here
        print("Game is running..")

        self.welcome_message()
        self.player.name = self.choose_name()

        self.what_is_a_beutiful_name(self.player.name)
        print(
            """
        And now, please choose a name for your girlfriend: """
        )

        self.player.girlfriend.name = self.choose_name()
        self.what_is_a_beutiful_name(self.player.girlfriend.name)
        print(
            """
        And now, we can start the game."""
        )

        self.start_menu_listener()
        self.get_girlfriend_some_food()

        print(
            """
        some people see the situation and feel uncomfortable..
        """
        )
        self.get_money(500)
        time.sleep(1)
        print(
            f"""
        {self.player.name} buy {self.player.girlfriend.name} a cookie!
        {self.player.girlfriend.name}: Yum Yum Yum! I liked it!
        """
        )
        self.first_kiss()

    def welcome_message(self):
        WELCOME_MESSAGE = """
        Hello and we glad that you here!
        This is a Terminal game.
        Before we begin, What is your name?
        """
        print(WELCOME_MESSAGE)

    def choose_name(self):
        self.is_doing_task = True
        name = input()
        return name

    def what_is_a_beutiful_name(self, name):
        print(
            f"""
        WOW! {name}, what a beautiful name!
        """,
            end="",
        )

    def start_menu_listener(self):
        menu_listener = threading.Thread(target=self.show_menu)
        menu_listener.start()

    def show_menu(self):
        menu = MenuManager()
        while True:
            if self.is_doing_task:
                continue
            else:
                key = input()
                if key == "s":
                    menu.show_menu()
                    chosen_option = input("Enter option: ")
                    menu.action(self.player, chosen_option)

    def get_girlfriend_some_food(self):
        self.is_doing_task = True
        print(
            f"""
        {self.player.girlfriend.name}: {self.player.name}! wake up!
        Im hungry, can you buy me some food? (Yes / No)
        """
        )
        buying_food_for_girlfriend = input()
        while True:
            if buying_food_for_girlfriend.lower() == "yes":
                print(
                    f"""
                {self.player.name}: ok ok fine, let me look at my cash..
                {self.player.name} is looking and see nothing.
                """
                )
                break

            else:
                print(
                    f"""
                {self.player.girlfriend.name}: please pleaseee pleaseeeeeeeee (Yes / No)
                """
                )
                buying_food_for_girlfriend = input()

        self.is_doing_task = False

    def get_money(self, amount_of_money: int):
        self.player.money += amount_of_money
        print(
            f"""
        {self.player.name} got {amount_of_money} dollar!
        """
        )

    def first_kiss(self):
        print(
            f"""
        {self.player.name} got his first kiss!
        """
        )
        time.sleep(1)
        print(
            f"""
        And some cupon for food from a stranger.
        {self.player.name} put the cupon in his bag.  
        """
        )
        Item.add_item(self.player, "cupon")
