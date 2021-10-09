import random


class Card:

    def __init__(self):
        self.last_card = 0
        self.current_card = 0
        self.current_card_type = ''
        self.stored_guess = ''

    def draw_card(self):
        self.current_card = random.randint(1, 13)
        card_types = ('spade', 'heart', 'diamond', 'club')
        self.current_card_type = random.choice(card_types)

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
    
    def pretty_card(self):
        card_types = {
            'spade': 0x1f0a0,
            'heart': 0x1f0b0,
            'diamond': 0x1f0c0,
            'club': 0x1f0d0
        }
        card_val = {
            1: 'Ace',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: '10',
            11: 'Jack',
            12: 'Queen',
            13: 'King'
        }
        pretty_val = card_val[self.current_card]
        unicode_val = card_types[self.current_card_type] + self.current_card
        return f'{chr(unicode_val)} ({pretty_val} of {self.current_card_type.title()}s)'
