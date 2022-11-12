import random


# This is the class declaration.
class Cards:
    """A deck of cards with a different values 1-13

    The responsibility of Cards is to keep track of the face-up card 
   
    Attributes:
        value (int): The value of the face-up card
    """

# This is the class constructor.
    def __init__(self):
        """Constructs a new instance of Card with a value attribute.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0


# Flips the next card. 
    def flip(self):
        """Generates a new random value.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1,13)


        
