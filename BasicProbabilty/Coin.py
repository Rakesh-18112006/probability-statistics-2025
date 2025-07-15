import random 

coin = ['Heads', 'Tails']

heads_count = 0
loss = 0
entry_fee = 0
for i in range(100):
    entry_fee += 55
    toss = random.choice(coin)
    if toss == 'Heads':
        loss += 70
    else: 
        loss += 30


print(f'Entry fee: {entry_fee}')
print(f'Total loss: {loss}')
print(f'Total profit: {entry_fee - loss}')