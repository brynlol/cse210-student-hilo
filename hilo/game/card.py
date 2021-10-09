import random


class Card:

    def __init__(self):
        self.last_card = 0
        self.current_card = 0
        self.stored_guess = ""

    def draw_card(self):
        self.current_card = random.randint(1, 13)

    def valid_user_guess(self, hi_lo):
        """Stores the guess from the interface into an attribute.
        
        Preforms additional validation on input.

        Returns bool: True on valid input, False on invalid input
        """
        if len(hi_lo) > 1 or len(hi_lo) == 0:
            return False
        hi_lo = hi_lo.lower()
        if (not hi_lo == 'h') and (not hi_lo == 'l'):
            return False
        if type(hi_lo) is not str:
            return False
        
        # All validation checks passed, store it
        self.stored_guess = hi_lo
        return True

    def check_user_guess(self):
        """See if the user's guess is correct.

        Returns bool: True if correct, False if incorrect
        """
        if self.stored_guess == "h" and self.current_card > self.last_card:
            return True
        elif self.stored_guess == "l" and self.current_card < self.last_card:
            return True
        else:
            return False

    def rotate_to_last(self):
        self.last_card = self.current_card

    def mod_score(self):
        if self.check_user_guess():
            points = 100
        elif not self.check_user_guess():
            points = -75
        return points
        