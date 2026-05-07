import random

# Established initial values for (respectively):
# Number of games played
# Total points earned
# Highest score
gamesPlayed = 0
PointsEarned = 0
highScore = 0

# Function for calculating the final score of a game
def scoringSystem(remaining_guesses, bank):
    score = 100 + (remaining_guesses* 250) + bank
    return score

# Function to show a summary of stats of the round just played
def summaryStats():
    print("\n--- SESSION SUMMARY ---")
    print(f"Games Played: {gamesPlayed}")
    print(f"Total Points: {PointsEarned}")
    print(f"Personal Best: {highScore}")
    print("-----------------------\n")

# Function to use the appropriate version of "guess" for text formatting    
def guessPluralise(count):
    if count == 1:
        return "guess"
    else:
        return "guesses"

# Main function where the guessing game logic is conducted
def guessingGame(gameNumber, maxGuesses=5):
    
    # Established the variables as global to ensure they can be updated for session-level stats
    global gamesPlayed, PointsEarned, highScore
    gamesPlayed+=1
    
    guesses=maxGuesses
    # Variable for accumulating the accuracy of the player's guesses compared to the actual number for the whole game
    proximityBank = 0
    finalScore = 0
    while guesses > 0:
        print(f"\n--- GUESS {9-guesses} ---\n")
        # Validating the user guess to ensure only integers between 1 and 100 are entered
        userInput = input("Please type in a number: ")
        try:
            number = int(userInput)
            if number > 100 or number < 1:
                print("Not in the correct range")
                continue
            # Logic for the user guessing the correct number
            elif number == gameNumber:
                print(f"\nCORRECT\n\nGood job, You guessed correctly with {guesses} {guessPluralise(guesses)} remaining")
                finalScore = scoringSystem(guesses, proximityBank)
                PointsEarned+=finalScore
                if finalScore>highScore:
                    highScore=finalScore
                print(f"\nYour final Score is {finalScore}")
                summaryStats()
                return True
            
            guesses -=1

            if guesses > 0:
                print(f"\nYou have {guesses} {guessPluralise(guesses)} left")
            else:
                finalScore = scoringSystem(guesses, proximityBank)
                print(f"Unlucky, the number was: {gameNumber}")
                if finalScore>highScore:
                    highScore=finalScore
                PointsEarned += finalScore
                summaryStats()
                break

            if number < gameNumber:
                print("\nINCORRECT\n\nHint: Too low!")
            else:
                print("\nINCORRECT\n\nHint: Too high!")
            prox = 100-abs(gameNumber-number)
            proximityBank += prox
            
        except ValueError:
            print("Not an integer try again")
    return False

print("\nWelcome to the guessing game!")

# Runs the game loop given that False is not returned 
while True:
    guessingNumber = random.randint(1,100)
    guessingGame(guessingNumber, 8)
    
    #Input is converted to lower case for easier text validation
    choice = input("Another? (y/n): ").lower()
    
    if choice != 'y':
        print("Thanks for playing")
        break
        


            
            
    
