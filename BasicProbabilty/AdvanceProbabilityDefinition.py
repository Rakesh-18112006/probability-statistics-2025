import random
import matplotlib.pyplot as plt
coin = ["T", "H"]

def flip_coin():
    return random.choice(coin)

heads = 0
series = []
for i in range(1, 100):
    result = flip_coin()
    if result == "H":
        heads += 1
    series.append(heads/i)
print(f" series: {series}")

plt.plot(series)
plt.xlabel("Number of flips")
plt.ylabel("Proportion of Heads")
plt.title("Coin Flip Simulation")
plt.show()