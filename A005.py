import numpy

def teilbar(n):
    check = True
    for x in range(11,20):
        if not n%x==0:
            check = False
    return check

gefunden = False
k=0
while gefunden is False:
    k+=380
    if teilbar(k):
        print(k)
        gefunden = True
