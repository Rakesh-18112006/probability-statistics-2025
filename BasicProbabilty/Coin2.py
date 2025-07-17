import random
coin1 = ['H', 'T']

def flipcoin():
 return random.choice(coin1)

no_of_heads_ = 0
no_of_tails = 0
for i in range(10000):
    result = flipcoin()
    if(result == 'H'):
       no_of_heads_ += 1
    else:
       no_of_tails += 1
print(f'Heads: {no_of_heads_}, Tails: {no_of_tails}')