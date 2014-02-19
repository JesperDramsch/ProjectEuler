import numpy as np



for a in range(1,500):
    for b in range(1,500):
        if a + b + np.sqrt(a**2 + b**2) == 1000:
            print(int(a*b*np.sqrt(a**2 + b**2)))



