# -*- coding: utf-8 -*-
import numpy as np

def fak(x):
    if x > 1:
        return x * fak(x - 1)
    else:
        return 1
        
def binomial(n,k):
    return fak(n)/(fak(k)*fak(n-k))
    
[n,k] = input('Bitte Gitterformat eingeben [a,b]: ')

print 'Die Anzahl der Pfade durch das {}x{} Gitter beträgt {}.'.format(n,k,binomial(n+k,k))
