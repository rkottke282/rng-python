import BaseRandomPython
import numpy as np
import time

count = 100000000
seed=473

start_time = time.time()
baseRandomNumbers = BaseRandomPython.generateRandom(count, seed)
print('Base Random Number generator took {} seconds to generate {} numbers',time.time()-start_time, count)
