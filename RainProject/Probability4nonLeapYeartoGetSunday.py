import random
weeks = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
def get_sunday_probability(year):
    # Count the number of Sundays in the year
    sundays = sum(1 for month in range(1, 13) for day in range(1, 32)
                  if (day <= 31 and (month != 2 or day <= 28 or (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))))
                  and random.choice(weeks) == 'sunday')
    return sundays / 365
print(f"Probability of a random day being a Sunday in {2023}: {get_sunday_probability(2023):.2%}")
