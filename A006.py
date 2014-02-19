import numpy as np

def sumsquare(up):
    return (up**4+2*up**3+up**2)/4
    
def squaresum(up):
    return sum(np.power(range(1,up+1),2))

up=100
print(sumsquare(up)-squaresum(up))