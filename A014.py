import numpy as np

def collatz(n):
    out=[n]
    while not n==1:
        if n%2==0:
            n=int(n*.5)
        else:
            n=int(3*n+1)
        out.append(n)
    return len(out)


for k in xrange(1,10**6+1):
    max=0
    col=collatz(k)
    if col > max:
        max=col
        act=k
        
print act