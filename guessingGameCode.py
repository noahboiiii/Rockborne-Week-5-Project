import random

gamesPlayed = 0
PointsEarned = 0
highScore = 0

def scoringSystem(remaining_guesses, bank):
    score = 100 + (remaining_guesses* 250) + bank
    return score

def summaryStats():
    print("\n--- SESSION SUMMARY ---")
    print(f"Games Played: {gamesPlayed}")
    print(f"Total Points: {PointsEarned}")
    print(f"Personal Best: {highScore}")
    print("-----------------------\n")
    
def guessPluralise(count):
    if count == 1:
        return "guess"
    else:
        return "guesses"

def guessingGame(gameNumber, maxGuesses=5):
    
    global gamesPlayed, PointsEarned, highScore
    gamesPlayed+=1
    
    guesses=maxGuesses
    proximityBank = 0
    finalScore = 0
    while guesses > 0:
        print(f"\n--- GUESS {9-guesses} ---\n")
        userInput = input("Please type in a number: ")
        try:
            number = int(userInput)
            if number > 100 or number < 1:
                print("Not in the correct range")
                continue
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
 
while True:
    guessingNumber = random.randint(1,100)
    guessingGame(guessingNumber, 8)
    
    choice = input("Another? (y/n): ").lower()
    
    if choice != 'y':
        print("Thanks for playing")
        break
        


            
            
    
