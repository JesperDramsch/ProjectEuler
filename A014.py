# -*- coding: utf-8 -*-
import time as t
start = t.time()

"""
def collatz(n):
    out=[n]
    while not n==1:
        if n%2==0:
            n=int(n*.5)
        else:
            n=int(3*n+1)
        out.append(n)
    return len(out)

maxi=0
for k in xrange(1,10**6+1):
    col=collatz(k)
    if col > maxi:
        maxi=col
        act=k
        
print act
"""

def collatz(n):
    while not n == 1:
        n=int(n*.5 if n&1==0 else 3*n+1)
	yield n

maxi=0
for k in xrange(1,10**6+1):
    col=sum(1 for l in collatz(k))
    if col > maxi:
	maxi=col
        act=k
        print k
        
print act


end = t.time()
print end-start