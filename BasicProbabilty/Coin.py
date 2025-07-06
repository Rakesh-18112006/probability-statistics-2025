import random 

coin = ['Heads', 'Tails']

heads_count = 0

for i in range(100000):
    toss = random.choice(coin)
    if toss == 'Heads':
        heads_count += 1

print(f'heads_count: {heads_count}')
print(f'tails_count: {100000 - heads_count}')