import random

low = 1
high = 100
guesses = 0
number = random.randint (low, high)

while True:
    guess = int(input (f"Enter a number between {low} - {high}: "))
    guesses += 1

    if guess < number:
        print ("guess is too low!!")
    elif guess > number:
        print ("guess is too high!!")
    else:
        print ("guess is correct")
        break

print (f"This round took {guesses} guesses")