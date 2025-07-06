import random
dice = [1, 2, 3, 4, 5, 6]
def roll_dice():
    return random.choice(dice)


no_of_ones = 0
no_of_twos = 0
no_of_threes = 0
no_of_fours = 0
no_of_fives = 0
no_of_sixes = 0


for i in range(10):
    result = roll_dice()
    if result == 1:
        no_of_ones += 1
    elif result == 2:  
        no_of_twos += 1
    elif result == 3:
        no_of_threes += 1
    elif result == 4:
        no_of_fours += 1
    elif result == 5:
        no_of_fives += 1
    elif result == 6:
        no_of_sixes += 1
        
print(f'Number of ones: {no_of_ones}')
print(f'Number of twos: {no_of_twos}')
print(f'Number of threes: {no_of_threes}')
print(f'Number of fours: {no_of_fours}')
print(f'Number of fives: {no_of_fives}')
print(f'Number of sixes: {no_of_sixes}')
