import time

from random import randint

right = 0
right = right + 0

questions = 10

def questions():
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    answer = num1 * num2
    question = "What is " + str(num1) + " times " + str(num2) + "? "
    return question, answer

start = time.time()


for _ in range(10):
    question, answer = questions()
    response = int(input(question))
    print(int(input("Enter a number: ")))

    
    if response == answer:
        right += 1
        print("Correct! Way to go!")
    else:
        print('Incorrect :(')

end = time.time()
total_time = end-start

print("I asked you " + str(10) + " questions. You got " + str(right) + " of them right.")

print(f"Time taken: {total_time:.2f} seconds")

print("Well done!")
