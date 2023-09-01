#Example file 2, Method 2 (Efficient)

import numpy as np
import matplotlib.pyplot as plt
from time import time

start = time()
num_days = 10000

temps = np.random.uniform(40, 60, num_days)
tols = np.random.normal(55, 5, num_days)
daily_calories = np.random.exponential(200, num_days)

daily_calories[temps < tols] = 0

end = time()
print(end - start)

plt.hist(daily_calories)
plt.title(np.mean(daily_calories))