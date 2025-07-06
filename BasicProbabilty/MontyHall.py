import random
switch_wins = 0
stay_wins = 0
def monty_hall(trials):
    global switch_wins, stay_wins
    for _ in range(trials):
        doors = ['A', 'B', 'C']
        car = random.choice(doors)
        choice = random.choice(doors)
        doors.remove(choice)
        
        if car in doors:
            doors.remove(car)
        
        monty_door = random.choice(doors)
        
        doors = [door for door in ['A', 'B', 'C'] if door != choice and door != monty_door]
        
        switch_wins_choice = random.choice(doors)

        if switch_wins_choice == car:
            switch_wins += 1
        else:
            stay_wins += 1
    
  
monty_hall(100000)
print(f'Switch wins: {switch_wins}')
print(f'Stay wins: {stay_wins}')
