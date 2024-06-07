import numpy as np
array = np.random.normal(0, 1, (10, 4))
print(array.max())
print(array.min())
print(array.mean())
print(array.std())
fiveStr = array[:5]
print(fiveStr)