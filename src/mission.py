# TODO: import tasks from the json file
from player import Player


class Mission:
    id = 0

    def __init__(
        self, difficulty_level, description, xp_reward, success_rate, item_reward=None
    ):
        self.mission_id = id
        self.difficulty_level = difficulty_level
        self.description = description
        self.xp_reward = xp_reward
        self.item_reward = item_reward
        self.success_rate = success_rate
        id = id + 1

        Mission.tasks.append(self)

    @staticmethod
    def get_task(player: Player):
        return Mission.tasks
