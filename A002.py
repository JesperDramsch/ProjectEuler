import numpy

fibo=1
naci=1
count=0
while fibo<4*10**6:
    fibonaci = fibo+naci
    
    print(fibonaci)
    if fibonaci%2==0:
        count = count+fibonaci
    naci = fibo    
    fibo = fibonaci

print(count)