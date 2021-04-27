from randomgen import Xoshiro256, PCG64DXSM, JSF
import numpy as np

TWO_TO_THE_64 = 2**64 - 1

def generateXoshiro256Random(count, seed):
    generator = Xoshiro256(seed, mode="sequence")
    randomNumbers = generator.random_raw(size=(count,1), output=True)
    return randomNumbers

def generatePcg64dxsm(count, seed):
    generator = PCG64DXSM(seed)
    randomNumbers = generator.random_raw(size=(count,1), output=True)
    return randomNumbers

def generateJsf(count, seed):
    generator = JSF(seed, mode="sequence")
    randomNumbers = generator.random_raw(size=(count,1), output=True)
    return randomNumbers
