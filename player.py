# Your Name: Nurmukhammed
# Date: March 7
# Player class for the adventure game

class Player:
    def __init__(self, name):
        self.name = name
        self.path = ""
        self.chapter2_result = ""
        self.item = ""
        self.health = 100

    def lose_health(self, amount):
        self.health -= amount

    def get_status(self):
        return f"{self.name} | Health: {self.health}"