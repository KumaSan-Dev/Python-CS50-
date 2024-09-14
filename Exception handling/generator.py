# Variation 1

"""import random

coin = random.choice(["heads", "tails"])
print(coin)
"""

# Variation 2

"""from random import choice
coin = choice(["Heads", "Tails"])
print(coin)"""

# Randint()
"""import random

number = random.randint(1, 10)
print(number)"""

import random

# Variation 1

"""cards = ["Jack", "Queen", "King"]
random.shuffle(cards)
print(cards)
"""

# Variation 2

cards = ["Jack", "King", "Queen"]
random.shuffle(cards)
for card in cards:
    print(card)
