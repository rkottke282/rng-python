import BaseRandomPython
import RandomGen
import numpy as np
import time

count = 100000000
seed=473

start_time1 = time.time()
baseRandomNumbers = BaseRandomPython.generateRandom(count, seed)
print('Base Random Number generator took {0} milliseconds to generate {1} numbers'.format((time.time()-start_time1)*1000, count))

start_time2 = time.time()
baseRandomNumbers = RandomGen.generateXoshiro256Random(count, seed)
print('RandomGen Xoshiro256 took {0} milliseconds to generate {1} numbers'.format((time.time()-start_time2)*1000, count))

start_time3 = time.time()
baseRandomNumbers = RandomGen.generatePcg64dxsm(count, seed)
print('RandomGen Permuted Congruential Generator 2.0 took {0} milliseconds to generate {1} numbers'.format((time.time()-start_time3)*1000, count))

start_time4 = time.time()
baseRandomNumbers = RandomGen.generateJsf(count, seed)
print('RandomGen Jenkins Small Fast Generator took {0} milliseconds to generate {1} numbers'.format((time.time()-start_time4)*1000, count))
