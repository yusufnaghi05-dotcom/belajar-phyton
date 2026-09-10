# import random
# coin = random.choice(["heads", "tail"])
# print(coin)

# import random

# number = random.randint(1, 10)
# print(number)

import random

cards = ["Jack", "King", "Queen"]
random.shuffle(cards)
for card in cards:
    print(card)