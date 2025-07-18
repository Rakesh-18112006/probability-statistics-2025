# import random

# dice = [1, 2, 3, 4, 5, 6]
# def throw_dice():
#     return random.choice(dice)

# even_count = 0
# odd_count = 0  

# for i in range(1000):
#     result = throw_dice()
#     if result == 2 or result == 4 or result == 6:
#         even_count = even_count + 1 
#     else:
#         odd_count = odd_count + 1

# print(f'Even numbers: {even_count}, Odd numbers: {odd_count}')


import random
dice = [1, 2, 3, 4, 5, 6]
def roll_dice():
    return random.choice(dice)

no_of_sixes = 0

for i in range(1000):
    result = roll_dice()
    if result == 6:
        no_of_sixes += 1
print(f'Number of sixes: {no_of_sixes}')
print(f'Probability of rolling a six: {no_of_sixes / 1000:.2f}')