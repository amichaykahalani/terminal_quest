# TODO: import tasks from the json file
from .player import Player
from .status import Status
import json


class Mission:

    def __init__(
        self,
        id,
        difficulty_level,
        description,
        xp_reward,
        success_rate,
        item_reward=None,
    ):
        self.mission_id = id
        self.difficulty_level = difficulty_level
        self.description = description
        self.xp_reward = xp_reward
        self.success_rate = success_rate
        self.item_reward = item_reward
        self.status = Status.AVAILABLE

    @staticmethod
    def add_missions(player: Player):
        with open(
            r"C:\dev\python_projects\terminal_quest\data\mission_list.json", "r"
        ) as missions_json:
            missions = json.load(missions_json)
            for mission in missions["missions"]:
                mission_to_add = Mission(
                    mission["id"],
                    mission["difficulty_level"],
                    mission["description"],
                    mission["xp_reward"],
                    mission["success_rate"],
                    mission["item_reward_name"],
                )
                player.missions.append(mission_to_add)

    def start(self):
        print(f"""{self.description}""")
        print()
        is_mission_taken = input("Start Mission? (yes / no): ")
        if is_mission_taken.lower() == "yes":
            print("Mission Started.")
            self.status = Status.IN_PROGRESS
            return True
        else:
            return False
