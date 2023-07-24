from random import randint

guesses = 0
number = randint(1, 1000)

question = "I have chosen a number between 1 and 1000. Guess my number:"
answer = int(input(question))

while answer != number:
    question = "I have chosen a number between 1 and 1000. Guess my number:"
    answer = int(input(question))
    if answer < number:
            print ("That is too low. Try again!")
            guesses += 1

    if answer > number:
            print ("That is too high. Try again!")
            guesses += 1

print ("CONGRATS! You correctly guessed my number! It took you " + str(guesses) + " guesses.")

