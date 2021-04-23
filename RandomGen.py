from randomgen import Xoshiro256, PCG64DXSM, JSF
import numpy as np

def generateXoshiro256Random(count, seed):
    generator = Xoshiro256(seed, mode="sequence")
    randomNumbers = np.empty((count,1))
    for i in range(count):
        randomNumbers[i][0] = generator.random_raw()
    return randomNumbers

def generatePcg64dxsm(count, seed):
    generator = PCG64DXSM(seed)
    randomNumbers = np.empty((count,1))
    for i in range(count):
        randomNumbers[i][0] = generator.random_raw()
    return randomNumbers

def generateJsf(count, seed):
    generator = JSF(seed, mode="sequence")
    randomNumbers = np.empty((count,1))
    for i in range(count):
        randomNumbers[i][0] = generator.random_raw()
    return randomNumbers
