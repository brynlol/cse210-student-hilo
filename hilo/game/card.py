import random


class Card:

    def __init__(self, initial_score=300):
        self.total_score = initial_score
        self.last_card = 0
        self.current_card = 0

    def draw_card(self):
        self.current_card = random.randint(1, 13)

    def check_lo_hi(self, hi_lo):
        """See if the current card is higher than the last

        Returns bool: true if higher, false if lower
        """
        if hi_lo == "h" and self.current_card > self.last_card:
            return True
        elif hi_lo == "l" and self.current_card < self.last_card:
            return True
        else:
            return False

    def rotate_to_last(self):
        self.last_card = self.current_card

    def mod_score(self, hi_lo):
        if self.check_lo_hi():
            if hi_lo == "h":
                score = 100
            else:
                score = -75
        elif self.check_lo_hi() == False:
            if hi_lo == "l":
                score = 100
            else:
                score = -75
        self.total_score += score
        