# Rockborne Week 5 Project - Guessing Game
A terminal-based game where a player must guess the secret number within 8 guesses using hints, and is scored by how quickly and accurately their guesses are

## Repositiory Link
https://github.com/noahboiiii/Rockborne-Week-5-Project.git

## Key Features
Dynamic Scoring - Score is calculated using the formula ***(remaining_guesses x 250) + bank***
- ***remaining_guesses*** represents the number of guesses left when either the player guesses the number or defaults to 0 when the player is unable to guess the number
- ***(remaining_guesses x 250)*** represents the efficiency bonus for guessing the number in as few attempts as possible
- ***bank*** represents the accumulation of the accuracy of the player's guesses throughout the entirety of the game
  
Input Validation - Ensures that the game only processes numbers between 1 and 100 and that if disallowed inputs are input, they are handled appropriately
Multiple Rounds - Gives the player the option to play multiple times
Session Stats - The game tracks total points, number of games, and the high score for both one round and across an entire session of multiple rounds

## How to play
1. Execute the script and observe the terminal
2. Input a guess as a number between and including 1 and 100
3. View the output in the terminal to determine the accuracy of the guess, using the hints to narrow the search
4. When correctly guessed or out of guesses, view the stat summary of the round or session
5. Choose to play again to beat the high score or end the game

## Prerequisites
- Developed on Python 3.13.9+ but 3.10+ is recommended for best compatibility
- Uses the random library. Included with Python by default
### Environment
- Recommended: Visual Studio Code with the Python extension
- Terminal: Can be executed via python guessingGameCode.py (ensuring you are in the project directory)




