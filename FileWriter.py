import numpy as np

def writeFile(data, filename):
    np.savetxt(filename + '.txt', data, delimiter=',')