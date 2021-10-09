from game import card

class Interface:

    def __init__(self, initial_score=300):
        self.total_score = initial_score
        self.card = card.Card()

    def start_game(self):
        while True:
            self.do_round()
            if self.check_quit_game():
                print('Thanks for playing!')
                break

    def do_round(self):
        self.card.draw_card()
        self.choose_hi_lo()
        self.card.rotate_to_last()
        self.card.draw_card()
        print(f'Next card was: {self.card.pretty_card()}')
        self.total_score += self.card.mod_score()
        print(f'Your score is: {self.total_score}')

    def choose_hi_lo(self):
        guess = ''
        while not self.card.valid_user_guess(guess):
            self.print_drawn_card()
            guess = input('Higher or lower? [h/l] ')

    def print_drawn_card(self):
        print('\033c')
        print(f'The card is: {self.card.pretty_card()}')

    def check_quit_game(self):
        if self.total_score <= 0:
            return True

        quit = input('Keep playing? [y/n] ')

        if quit.lower() == 'n':
            return True
        
        # Assume keep playing if no valid input
        return False