# Board Battleship

Board Battleship is a python terminal game, which runs the Code Institute mock terminal on Heroku.

The User can try beat the Computer by finding all of the battleships co-ordinates before the computer find your battleship co-ordinates. One battleship occupies one square on the board.


## How to play

Board Battleships is based on the classic Battleships game . In this game the player starts the game and the computers battleship co-ordinates are randomly generated for the computer board and the player board. '-' marks guessed and missed co-ordinates, # marks battleships and 'X' marks hit battleships.
The winner is whoever sinks the opponents battleships first.

## Existing Features 

- Random board is generated and the player cannot see where the computer's ships are.

- Play against the computer.

- Accepts user input and rejects/reacts to invalid input.

- Maintains score

- Input validation: 
You cannot enter coordinates outside of the grid.
You cannot enter the same guess twice.
You must enters letters in the row and numbers un the column.

## Future Features

- Allow player to select the board size and number of ships
- Allow player to place their own ships on the Battlefield.
- Have ships larger than 1x1


## Testing

I have manually tested the project by doing the following:

- Passed the code through a PEP8 linter and confirmed there are no problems.
- Given invalid inputs: strings when numbers are expected and numbers when strings are expected.
-T ested by local terminal and Code Institute Heroku terminal.

## Bugs 
Solved Bugs 
- When I wrote the project I had syntax errors until I fixed them by revising past challenges.
- I passed the code through pep8 and returned to my project to fix the errors such as 'whitespace' and 'line too long'

Remaining Bugs 
- No bugs remaining

Validator Testing
- PEP8
No errors were returned from PEP8online.com

## Deployment 
This project was deployed using Code Institute's ock terminal for Heroku. 

- Steps for deployment:
Fork or clone this respository

Creates a new Heroku app

Set the buildbacks to Python and NodeJS in the order 

Link the Heroku app to the respository

Click on Deploy


## Credits 

- Code Institute for the deployment terminal and Python lessons.

- Codecademy Python2 free lessons.

- Wikipedia for the details of the Battleship game
