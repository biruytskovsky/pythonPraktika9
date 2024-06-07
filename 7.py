import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris = np.genfromtxt(url, delimiter=',', dtype='object')

species = iris[:, 4]

uniqueSpecies, counts = np.unique(species, return_counts=True)

for species, count in zip(uniqueSpecies, counts):
    print(f'{species.decode("utf-8")}: {count}')