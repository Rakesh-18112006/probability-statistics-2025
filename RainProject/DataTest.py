import pandas as pd
import matplotlib.pyplot as plt

# 1. Load and clean data as before
df = pd.read_csv(r"C:\\Users\\Rakesh Mummana\\Downloads\\imdlib_rain_2025-03-24_to_2025-07-21_points.csv")

df.columns = ['date', 'rainfall_mm']
df['date'] = pd.to_datetime(df['date'])
df['rainfall_mm'] = pd.to_numeric(df['rainfall_mm'], errors='coerce').fillna(0)

# 2. Create rain_day indicator
df['rain_day'] = df['rainfall_mm'] > 0

# 3. Calculate overall daily rain probability
rain_probability = df['rain_day'].mean()
print(f"Probability of rain on any given day: {rain_probability:.2%}")

# 4. (Optional) Calculate probability of rain, given it rained yesterday
df['rain_yesterday'] = df['rain_day'].shift(1)
conditional_probability = df[df['rain_yesterday'] == True]['rain_day'].mean()
# print(f"If it rained yesterday, probability it rains today: {conditional_probability:.2%}")

# 5. (Optional) Monthly probability plot
df['month'] = df['date'].dt.to_period('M')
monthly_prob = df.groupby('month')['rain_day'].mean()
monthly_prob.plot(kind='bar', ylabel='Rain Probability', xlabel='Month', title='Monthly Rainfall Probability')
plt.tight_layout()
plt.show()

