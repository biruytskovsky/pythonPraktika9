import numpy as np
x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
max = 0
for i in range(len(x)-1):
    if x[i] == 0 and max < x[i+1]:
        max = x[i+1]
print(max)