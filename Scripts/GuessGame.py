import random
print("Hello, what is your name?")
name = input()

secretNumber = random.randint(1,20)

print("Well, " + name + " I am thinking of a number between 1 and 20.")

for guessesTaken in range(1,7):
    print("Take a guess.")
    guess = int(input())
    if guess < secretNumber:
        print("Guess too low, try again")
    elif guess > secretNumber:
        print("Guess too high, try again")
    else:
        # This would be the correct guess.
        break
if guess == secretNumber:
    print("Good Job " + name + " you guessed correctly.")
else:
    print("No the number that I was thinking of is " + str(secretNumber))
    
