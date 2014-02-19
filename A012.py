import numpy
import operator as op
import time as t
start = t.time()

"""
.
"""

def tri(n):
    for k in xrange(1,n):
        yield (k**2+k)*.5
def faktoren(n):
    return sum(2 for k in xrange(1,int(n**.5+1)) if not n%k)

k=100000000
for l in tri(k):
    if faktoren(l)>500:
        print("Es wurde die Zahl ",int(l)," mit ",faktoren(l)," Faktoren gefunden")
        break


end=t.time()
print(end-start)