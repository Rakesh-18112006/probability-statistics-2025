# import random
# coin1 = ['H', 'T']

# def flipcoin():
#  return random.choice(coin1)

# no_of_heads_ = 0
# no_of_tails = 0
# for i in range(10000):
#     result = flipcoin()
#     if(result == 'H'):
#        no_of_heads_ += 1
#     else:
#        no_of_tails += 1
# print(f'Heads: {no_of_heads_}, Tails: {no_of_tails}')


import random

total_outcomes = []
coins = ['H', 'T']
for i in coins:
    for j in coins:
        for k in coins:
            total_outcomes.append((i, j, k))

print(f'Total outcomes: {len(total_outcomes)}')

def flipcoin():
    return random.choice(total_outcomes)

no_of_heads = 0
no_of_tails = 0 

for i in range(10000):
    result = flipcoin()
    if result.count('H') > result.count('T'):
        no_of_heads += 1
    else:
        no_of_tails += 1

print(f'Heads: {no_of_heads}, Tails: {no_of_tails}')
