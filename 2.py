import numpy as np

x = np.array([1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 2, 2, 2])
values = [x[0]]
counts = [1]

for i in range(1, len(x)):
    if x[i] == x[i - 1]:
        counts[-1] += 1
    else:
        values.append(x[i])
        counts.append(1)

np.array(values), np.array(counts)

print(values)
print(counts)