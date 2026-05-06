import random

def guessingGame(maxGuesses=5):
    gameNumber = random.randint(1,100)
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
                if abs(gameNumber-number) == 0:
                    finalScore = 100 + (guesses*250) + proximityBank
                    print(f"Final Score is {finalScore}")
                return True
            
            guesses -=1
            # print(f"Difference is {gameNumber-number}")
            print(f"RECORD THIS SPECIFICALLY {100-abs(gameNumber-number)}")
            
            if number < gameNumber:
                print("Too low")
            else:
                print("Too high")
            prox = 100-abs(gameNumber-number)
            proximityBank += prox
            print(proximityBank)
            
            if guesses > 0:
                print(f"You have {guesses} left")
            else:
                print("Out of guesses")
                print(f"Unlucky, the number was {gameNumber}")
                break
        except ValueError:
            print("Not an integer try again")
    return False

# def scoringSystem(gameNumber, number):
    

guessingGame(5)
            
            
    
