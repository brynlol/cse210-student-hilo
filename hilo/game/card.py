import random
from game.interface import Interface

class Card:

    def __init__(self, initial_score=300):
        self.total_score = initial_score
        self.last_card = 0
        self.current_card = 0

    def draw_card(self):
        self.current_card = random.randint(1, 13)

    def check_lo_hi(self):
        """See if the current card is higher than the last

        Returns bool: true if higher, false if lower
        """
        return (self.current_card > self.last_card) 

    def rotate_to_last(self):
        self.last_card = self.current_card

    def mod_score(self):
        if self.check_lo_hi():
            if self.interface.choose_hi_lo() == "h":
                score = 100
            else:
                score = -75
        elif self.check_lo_hi == False:
            if self.interface.choose_hi_lo() == "l":
                score = 100
            else:
                score = -75
        self.total_score += score
        return self.total_score