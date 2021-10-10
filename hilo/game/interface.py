from game import card
class Interface:
    """A code template for the interface of the game. The responsibility of
    this class of objects is to keep track of the score, control the
    sequence of play, and display it to the user.
    Attributes:
        total_score (number): The total number of points earned.
        card (Card): An instance of the class of objects known as Card.
    """
    def __init__(self, initial_score=300):
        """Class constructor. Declares and initializes instance attributes.
        Args:
            self (Interface): An instance of Interface.
        """
        self.total_score = initial_score
        self.card = card.Card()
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        Args:
            self (Director): an instance of Director.
        """
        while True:
            self.do_round()
            if self.check_quit_game():
                print('Thanks for playing!')
                break
    def do_round(self):
        """This method calls the following methods to play the round:
            draw_card()
            choose_hi_lo()
            rotate_to_last()
        Args:
            self (Director): an instance of Director.
        Print:
            Next card and score
        """
        self.card.draw_card()
        self.choose_hi_lo()
        self.card.rotate_to_last()
        self.card.draw_card()
        print(f'Next card was: {self.card.pretty_card()}')
        self.total_score += self.card.mod_score()
        print(f'Your score is: {self.total_score}')
    def choose_hi_lo(self):
        """Get user input to determine if they think the next card will be higher or lower
        Args:
            self (Director): an instance of Director.
        """
        guess = ''
        while not self.card.valid_user_guess(guess):
            self.print_drawn_card()
            guess = input('Higher or lower? [h/l] ')
    def print_drawn_card(self):
        """Clears interface for the start of the round and starts round.
        Args:
            self (Director): an instance of Director.
        Print: the first card drawn for the round.
        """
        print('\033c')
        print(f'The card is: {self.card.pretty_card()}')
    def check_quit_game(self):
        """Check if score is <= 0, if it is end the game.
            Check if the player wants to keep playing, if they don't, end the game.
        Args:
            self (Director): an instance of Director.
        Return (bool): return True if total score is <= 0 or
            if the player doesn't want to continue.    
            """
        if self.total_score <= 0:
            return True
        quit = input('Keep playing? [y/n] ')
        if quit.lower() == 'n':
            return True
        # Assume keep playing if no valid input
        return False
