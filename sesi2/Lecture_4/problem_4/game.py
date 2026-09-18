import random

while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            continue
        else:
            break
    except ValueError:
        continue
    
answer = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            continue
        if guess == answer:
            print("Just right!")
            break
        if guess < answer:
            print("Too small!")
            continue
        if guess > answer:
            print('Too large!')
            continue
    except ValueError:
        continue