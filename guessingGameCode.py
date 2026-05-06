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

def guessingGame(gameNumber, maxGuesses=5):
    
    global gamesPlayed, PointsEarned, highScore
    gamesPlayed+=1
    
    guesses=maxGuesses
    proximityBank = 0
    finalScore = 0
    while guesses > 0:
        userInput = input("Please type in a number: ")
        try:
            number = int(userInput)
            if number > 100 or number < 1:
                print("Not in the correct range")
                continue
            elif number == gameNumber:
                print(f"Thats the correct number with {guesses}")
                finalScore = scoringSystem(guesses, proximityBank)
                PointsEarned+=finalScore
                if finalScore>highScore:
                    highScore=finalScore
                print(f"Final Score is {finalScore}")
                summaryStats()
                return True
            
            guesses -=1
            
            if number < gameNumber:
                print("Too low")
            else:
                print("Too high")
            prox = 100-abs(gameNumber-number)
            proximityBank += prox
            
            if guesses > 0:
                print(f"You have {guesses} left")
            else:
                finalScore = scoringSystem(guesses, proximityBank)
                if finalScore>highScore:
                    highScore=finalScore
                PointsEarned += finalScore
                summaryStats()
                break
        except ValueError:
            print("Not an integer try again")
    return False
 
while True:
    guessingNumber = random.randint(1,100)
    guessingGame(guessingNumber, 5)
    
    choice = input("Another? (y/n): ").lower()
    
    if choice != 'y':
        print("Thanks for playing")
        break
        


            
            
    
