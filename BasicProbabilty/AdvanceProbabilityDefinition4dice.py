import random
import matplotlib.pyplot as plt
dice = [1, 2, 3, 4, 5, 6]
def roll_dice():
    return random.choice(dice)

series = []
no_of_sixes = 0
#  Count the number of times a six is rolled
for i in range(1000):
    result = roll_dice()
    if result == 6:
        no_of_sixes += 1
    series.append(no_of_sixes / (i + 1))
print(f'series: {series}')

plt.plot(series)
plt.xlabel("Number of rolls")
plt.ylabel("Proportion of Sixes")
plt.title("Dice Roll Simulation")
plt.grid(True)
plt.axhline(y=1/6, color='r', linestyle='--', label='Expected Probability (1/6)')
plt.legend()
plt.xticks(range(0, 1000, 100))
plt.yticks([i/10 for i in range(0, 11)])        
plt.show()