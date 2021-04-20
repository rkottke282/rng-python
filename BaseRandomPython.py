import random
import numpy as np

def generateRandom(count, seed):
    random.seed(seed)
    randomNumbers = np.empty((count,1))
    for i in range(count):
        randomNumbers[i][0] = random.random()
    return randomNumbers