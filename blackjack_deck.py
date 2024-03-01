import random
from constants import *


class Deck:
    def __init__(self):
        self.cards = []
        self.build()