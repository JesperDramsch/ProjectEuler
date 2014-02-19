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
    
summe=2
for x in range(3,2*10**6,2):
    if isPrime(x):
        summe+=x
    
print(summe)
end=time.time()
print(end-start)