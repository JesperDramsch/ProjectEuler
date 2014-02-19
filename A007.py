import numpy as np

def isPrime(n):
    if n < 2:
            return False
                
    if n==2:
        return True

    if not n & 1:
        return False
        
    for x in range(3,int(n**.5)+1,2):
        if n%x==0:
                return False        
    return True
k=0
prim=1
while k<=10000:
    prim+=1
    if isPrime(prim):
        k+=1
    
print(prim)