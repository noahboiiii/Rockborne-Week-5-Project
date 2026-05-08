import random

# Established initial values for (respectively):
# Number of games played
# Total points earned
# Highest score
gamesPlayed = 0
scoreAccumulated = 0
highScore = 0

# Function for calculating the final score of a game
# with the number of remaining guesses and the total accumulation of accuracy for each round played
def scoringSystem(remaining_guesses, bank):
    score = (remaining_guesses* 250) + bank
    return score

# Function to show a summary of stats of the round just played
def summaryStats():
    print("\n--- SESSION SUMMARY ---")
    print(f"Games Played: {gamesPlayed}")
    print(f"Total Points: {scoreAccumulated}")
    print(f"Personal Best: {highScore}")
    print("-----------------------\n")

# Function to use the appropriate version of "guess" for text formatting    
def guessPluralise(count):
    if count == 1:
        return "guess"
    else:
        return "guesses"

# Function for
#   - updating the total score for the session
#   - comparing the high score and final score and updating the high score if the final score is higher       
def scoreUpdate(final):
    global scoreAccumulated, highScore 
    scoreAccumulated+=final
    if highScore == 0:
        highScore=final
    if final>highScore:
        high=final    

# Main function where the guessing game logic is conducted
def guessingGame(gameNumber, maxGuesses):
    
    # Established the variables as global to ensure they can be updated for session-level stats
    global gamesPlayed, scoreAccumulated, highScore
    gamesPlayed+=1
    # Established seperate guess variable to the maxGuesses to symbolise number of guesses used by the player
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
                # Calculates the final score when the player guesses the number using the scoringSystem function defined above 
                finalScore = scoringSystem(guesses, proximityBank)
                # Updates the total score and high score using scoreUpdate()
                scoreUpdate(finalScore)
                print(f"\nYou scored {finalScore} in this round")
                # Shows the round stats using summaryStats()
                summaryStats()
                return True
            
            # Decrements the guesses each attempt
            guesses -=1
            
            if guesses > 0:
                print(f"\nYou have {guesses} {guessPluralise(guesses)} left")
            #Logic for the user being unable to guess the correct number
            else:
                # Calculates the final score when the player doesn't guess the number using the scoringSystem function defined above
                finalScore = scoringSystem(guesses, proximityBank)
                print(f"\nINCORRECT\n\nUnlucky, the number was: {gameNumber}")
                # Updates the total score and high score using scoreUpdate()
                scoreUpdate(finalScore)
                print(f"\nYou scored {finalScore} in this round")
                # Shows the round stats using summaryStats()
                summaryStats()
                break

            # Logic for hints
            if number < gameNumber:
                print("\nINCORRECT\n\nHint: Too low!")
            else:
                print("\nINCORRECT\n\nHint: Too high!")
            # Value repesenting how far the player's guess was to the actual number
            prox = 100-abs(gameNumber-number)
            # Increments the proximityBank value with the proximity value
            proximityBank += prox
        
        #Catching ValueErrors and returning appropriate response    
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
    
    # Choice for the user to continue with 'y' only or quit with any other input
    if choice != 'y':
        print("Thanks for playing")
        break
        


            
            
    
