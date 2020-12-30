# money

import random

heads = 0
tails = 0
tossing = 0

while tossing != 100:
    heads_or_tails = random.randint(1, 2)
    if heads_or_tails == 1:
        heads += 1
        tossing += 1
    elif heads_or_tails == 2:
        tails += 1
        tossing += 1
print("ОРЁЛ", heads, "РЕШКА", tails)
