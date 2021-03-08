# Ants Vs. SomeBees

# CS61A - project 3 

This is a tower defense defense game called Ants Vs. SomeBees. As the ant queen, you populate your colony with the bravest ants you can muster. Your ants must protect their queen from the evil bees that invade your territory. Irritate the bees enough by throwing leaves at them, and they will be vanquished. Fail to pester the airborne intruders adequately, and your queen will succumb to the bees' wrath. This game is inspired by PopCap Games' Plants Vs. Zombies ®.

This project combines functional and object-oriented programming paradigms, focusing on the material from Chapter 2.5 of Composing Programs. The project also involves understanding, extending, and testing a large program.

Rules of the game:
- A game of Ants Vs. SomeBees consists of a series of turns. In each turn, new bees may enter the ant colony. Then, new ants are placed. Finally, all insects (ants, then bees) take individual actions. Bees either try to move toward the end of the tunnel or they sting ants in their way. Ants perform a different action depending on their type, such as throwing leaves at the bees. The game ends either when a bee reaches the ant queen (you lose), or the entire bee flotilla has been vanquished (you win).

To play a text-based game, run:

python3 ants.py

To play a graphical game, run:

python3 gui.py

To play an older version of the graphics, run:

python3 ants_gui.py

There are many options to configure:

-h, --help show this help message and exit
-d DIFFICULTY sets difficulty of game (test/easy/medium/hard/insane)
-w, --water loads a full layout with water
--food FOOD number of food to start with when testing

usage:

python3 ants.py [-h] [-d DIFFICULTY] [-w] [--food FOOD]

For more information: https://inst.eecs.berkeley.edu/~cs61a/sp18/proj/ants/
