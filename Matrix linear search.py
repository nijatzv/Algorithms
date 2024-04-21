import numpy as np

def linearSearch(matris, element):
    for row in range(matris.shape[0]):
        for col in range(matris.shape[1]):
            if matris[row, col] == element:
                return element, (row, col)
    return -1

matrisim = np.array([
    [1, 2, 3, 4], 
    [5, 6, 7, 8], 
    [9, 10, 11, 12]
    ])

axtaris = 5
print(linearSearch(matrisim, axtaris))