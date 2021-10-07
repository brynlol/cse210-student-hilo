import random

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
        pass

    def rotate_to_last(self):
        self.last_card = self.current_card

    def mod_score(self):
        pass