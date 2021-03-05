CS61A-Hog

My first project for CS61A. A strategic dice game for two players with a few interesting twists!
Rules:

    Roll 0-10 dice, you get the score of the sum of the faces of the dice, but if you roll a one on any of those dice, 
    you will add that number of dice to the opponent's score and you receive 0 points for that turn
    Rolling 0 dice will add one greater than the highest digit of the opponents score to your own.
    If the sum of the two player's score is seven, special four-sided dice are used for the current turn.
    If two players have scores that are reverse of each other (ex: 07 and 70), then the players swap scores.
    If a player has a prime number score, that score is raised to the next prime number.
    First player to 100 points wins. Have fun! :)

To play, simply use the following command: python3 hog.py
