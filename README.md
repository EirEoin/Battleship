#Board Battleship

Board Battleship is a python terminal game, which runs the Code Institute mock terminal on Heroku.

The User can try beat the Computer by finding all of the battleships co-ordinates in a limited amount of guesses! One battleship occupies one square on the board.


###How to play

Board Battleships is based on the classic Battleships game . In this game the player starts the game and the computers battleship co-ordinates are randomly generated. '-' marks guessed and missed co-ordinates and 'X' marks hit battleships.
The winner is either The Player after guessing all of the battleship co-ordinates, or the computer when the `player fails to do so.

###Existing Features 

-Random board is generated and the player cannot see where the computer's ships are.

-Play against the computer.

-Accepts user input and rejects/reacts to invalid input.

-Maintains score

-Input validation: 
You cannot enter coordinates outside of the grid.
You cannot enter the same guess twice.
You must enters letters in the row and numbers un the column.

###Future Features

- Allow player to select the board size and number of ships
- Create a user game board for the computer to guess against
- Allow player to place their own ships on the Battlefield.
-Have ships larger than 1x1

##Data Model
I decided to use a Board class as my model. The game creates an instance for the computers board.

##Testing

I have manually tested the project by doing the following:

- Passed the code through a PEP8 linter and confirmed there are no problems.
-Given invalid inputs: strings when numbers are expected and numbers when strings are expected.
-Tested by local terminal and Code Institute Heroku terminal.

##Bugs 
Solved Bugs 
- When I wrote the project I had syntax errors until I fixed them by revising past challenges.

Remaining Bugs 
- No bugs remaining

Validator Testing
- PEP8
No errors were returned from PEP8online.com

###Deployment 
This project was deployed using Code Institute's ock terminal for Heroku. 

-Steps for deployment:
Fork or clone this respository

Creates a new Heroku app

Set the buildbacks to Python and NodeJS in the order 

Link the Heroku app to the respository

Click on Deploy


##Credits 

-Code Institute for the deployment terminal and Python lessons.

-Codecademy Python2 free lessons.

- Wikipedia for the details of the Battleship game
