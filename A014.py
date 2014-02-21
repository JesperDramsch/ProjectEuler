# -*- coding: utf-8 -*-
#!/usr/bin/python
import time as t
start = t.time()
import numpy as np
import operator

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


def load_collatz(up):
    global coll_dict 
    coll_dict = {1:1}
    for m in xrange(1,int(np.log2(up)+1)):
	coll_dict[2**m]=m
    
    for k in xrange(3,int(up+1),2):
	count=0
	l=k
	while not l == 1:
	    if not coll_dict.has_key(l):
		if l&1==0:
		    l=int(l*.5)
		    count+=1
		else:
		    l=int(1.5*l+.5)
		    count+=2
	    else:
		count+=coll_dict[l]
		l=1
	coll_dict[k]=count
	if k < up*.5:
	    coll_dict[k*2]=count+1
	

load_collatz(10**6)
print max(coll_dict.iteritems(), key=operator.itemgetter(1))[0]




end = t.time()
print end-start