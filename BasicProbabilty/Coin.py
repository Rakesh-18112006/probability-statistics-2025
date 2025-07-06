import random 

coin = ['Heads', 'Tails']

toss = random.choice(coin)
print(f'The coin landed on: {toss}')
heads_count = 0

for i in range(10):
    toss = random.choice(coin)
    if toss == 'Heads':
        heads_count += 1

print(f'heads_count: {heads_count}')
print(f'tails_count: {10 - heads_count}')