from game.cards import Cards


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """


    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.cards = []
        self.is_playing = True
        self.score = 0
        self.total_score = 300
        self.guess = ""
       
        card = Cards()
        self.cards.append(card)

        card1 = self.cards[0]
        card1.flip()


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()     


    def get_inputs(self):
        """Ask the user if they want to flip a card.

        Args:
            self (Director): An instance of Director.
        """
        top_card = self.cards[0]
    
        flip_card = input("\nDo you want to continue? [y/n]: ")
        while (flip_card != "y") and (flip_card != "n"):
            flip_card = input("\nInvalid response please choose [y/n]: ")

        self.is_playing = (flip_card == "y")

        if self.is_playing:
            print(f'\nThe top card is: {top_card.value}')
            self.guess = input("Will the next card be lower or higher? (l/h):")
            while (self.guess != "l") and (self.guess != "h"):
                self.guess = input("\nInvalid response please choose [l/h]: ")
        else:
            print('Thank you for playing.\n')


    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 
        # Flip a new card and append to self.cards list.
        new_card = Cards()
        self.cards.append(new_card)
        card2 = self.cards[1]
        card2.flip()
        value2 = card2.value

        card1 = self.cards[0]
        value1 = card1.value

        print(f"\ntop card: {value1}    new card: {value2}")

        # Compare card values.
        compare = value1 - value2
        
        if (self.guess == "l" and compare > 0) or (self.guess == 'h' and compare < 0):
            print('You win +100')
            self.total_score += 100
        elif compare == 0:
            print("It's a tie.")
        else:
            print('You lose -75')
            self.total_score -= 75

        if self.total_score <= 0:
            print(f'Your total score is: {self.total_score}. Better luck next time. Good Bye\n')
            self.is_playing = False


    def do_outputs(self):
        """Displays the card and the score. Also asks the player if they want to flip a new card. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        print(f"Your score is: {self.total_score}")
        self.cards.pop(0)



