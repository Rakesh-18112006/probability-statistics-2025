
dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]
coin = ['H', 'T']
total_outcomes = []
for i in dice1:
    for j in dice2:
        for k in coin:    
            total_outcomes.append((i,j,k))
print(f'Total outcomes: {len(total_outcomes)}')
print(f'Outcomes: {total_outcomes}')



# dice1 = [1,2,3,4,5,6]
# dice2 = [1,2,3,4,5,6]
# coin = ['H', 'T']
# total_outcomes = []
# for i in coin:
#     for j in coin:
#          print(i+j)
        # for k in coin:
           
            # total_outcomes.append((i,j,k))
# print(f'Total outcomes: {len(total_outcomes)}')
# print(f'Outcomes: {total_outcomes}')