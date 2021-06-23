import string
import random


class Robot:
    def __init__(self):
        self.name = self.generateName()

    def generateName(self):
        return "".join(random.choices(string.ascii_uppercase, k=2)) + str(random.randint(100, 999))

    def reset(self):
        random.seed()
        self.name = self.generateName()
