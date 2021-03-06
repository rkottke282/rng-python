import BaseRandomPython
import RandomGen
import numpy as np
import time
import FileWriter

count = 1000
seed = 473
TWO_TO_THE_64 = 2**64 - 1

start_time1 = time.time()
baseRandom = BaseRandomPython.generateRandom(count, seed)
print('Base Random Number generator took {0} milliseconds to generate {1} numbers'.format((time.time()-start_time1)*1000, count))
FileWriter.writeFile(baseRandom, 'pythonBaseRandom')

start_time2 = time.time()
Xoshiro256Random = RandomGen.generateXoshiro256Random(count, seed)
print('RandomGen Xoshiro256 took {0} milliseconds to generate {1} numbers'.format((time.time()-start_time2)*1000, count))
Xoshiro256Random = np.true_divide(Xoshiro256Random, TWO_TO_THE_64)
FileWriter.writeFile(Xoshiro256Random, 'Xoshiro256Random')

start_time3 = time.time()
pcg64dxsmRandom = RandomGen.generatePcg64dxsm(count, seed)
print('RandomGen Permuted Congruential Generator 2.0 took {0} milliseconds to generate {1} numbers'.format((time.time()-start_time3)*1000, count))
pcg64dxsmRandom = np.true_divide(pcg64dxsmRandom, TWO_TO_THE_64)
FileWriter.writeFile(pcg64dxsmRandom, 'Pcg64dxsmRandom')

start_time4 = time.time()
JsfRandom = RandomGen.generateJsf(count, seed)
print('RandomGen Jenkins Small Fast Generator took {0} milliseconds to generate {1} numbers'.format((time.time()-start_time4)*1000, count))
JsfRandom = np.true_divide(JsfRandom, TWO_TO_THE_64)
FileWriter.writeFile(JsfRandom, 'JsfRandom')
