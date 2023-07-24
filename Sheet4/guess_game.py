from random import randint

number = randint(1, 1000)

while True:
    question = "I have chosen a number between 1 and 1000. Guess my number:"
    answer = int(input(question))
    guesses = 0
    if answer < number:
            print ("That is too low. Try again!")
            guesses += 1

    if answer > number:
            print ("That is too high. Try again!")
            guesses += 1

    if answer == number:
        print ("CONGRATS! You correctly guessed my number!")
        break
