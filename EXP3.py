import random

# generate random number
number = random.randint(1, 100)

# set number of chances/trials
chances = 10

# start loop for 10 chances
for i in range(chances):
    # ask user to guess the number
    guess = int(input("Guess the number between 1 and 100: "))
    
    # check if the guess is too low, too high, or correct
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("Correct!")
        break

# check if the guess is correct or not
if guess == number:
    print("You guessed the number in", i+1, "tries")
else:
    print("You did not guess the number. The number was", number)
