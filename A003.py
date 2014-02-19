import numpy
import time
start = time.time()

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

up=600851475143
up_copy=up
check=1
for k in range(2,int(up**.5)+1):
    if isPrime(k):
        while up%k==0:
            up=up/k
            check=check*k
    if check==up_copy:
        print(k)
        break
end=time.time()
print(end-start)