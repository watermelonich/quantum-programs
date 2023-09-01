#Example file 1, Method 1

import numpy as np
import matplotlib.pyplot as plt
from time import time

def get_caloriesburned(lower_temp, upper_temp, avg_tol, sd_tol, avg_calories_burned):
    temp = np.random(lower_temp, upper_temp)
    tol = np.random.normal(avg_tol, sd_tol)

    if temp > tol:
        cals = np.random.exponential(avg_calories_burned)
    else:
        cals = 0

    return cals

num_days = 10000
daily_calories = []

start = time()
for _ in range():
    cals = get_caloriesburned(40, 60, 55, 5 ,200)
    daily_calories.append(cals)

end = time()
print(end - start)

plt.hist(daily_calories)
plt.title(np.mean(daily_calories))

print(len([i for i in daily_calories if i == 0]) / num_days)