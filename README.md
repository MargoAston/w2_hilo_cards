# Hilo Cards
Are you willing to risk everything? Play Hilo and you might be surprised. The rules are simple. The player begins the game with 300 points. The current card is displayed. The player guesses if the next card will be higher or lower. The player earns 100 points if they guess correct; the player loses 75 points if the guess is incorrect. If the player reaches 0 points the game is over. As long as the player has more than 0 points they may chose to try again. If not the game is over.

## Getting Started
---
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and 
browse to the project's root folder. Start the program by running the following command.
```
python3 hilo_cards 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the hilo_cards folder and click the "run" button.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- hilo_cards          (source code for game)
  +-- game              (specific classes)
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0

## Authors
---
* Margo Aston margo.aston@yahoo.com

Object: Director

Responsibilitiy: control the sequence of play

Behaviors:
  start game
  show card
  get input
  show next card
  make evaluation
  show score
  play again? (end game)
  
State:
  card
  next card
  guess
  score
  total score

-----------------
Object: Card

Responsibilitiy: create a random card with a value from 1-13

Behaviors:
  get value


State:
  value (1-13)


-----------------

Class: Director

Variables:
  card: Card
  next_card: Card
  score: integer
  guess: string
  is_playing: boolean
  total_score: integer


Methods:
  start_game(): None
  show_card(): None
  get_input(): None
  show_next_card(): None
  make_evaluation(): None
  show_score(): None
  play_again(): None


Class: Card

Variables:
  value: integer

Methods:
  get_value(): None


The relationship between objects: The director has cards.