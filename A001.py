
def find_start(upperlimit,multipleof):
    return int((upperlimit-1)/multipleof)
    
def sumall(n):
    return (n*(n+1))/2
    
ul = 1000
a = 3
b = 5
c = a*b
a_iter = find_start(ul,a)
b_iter = find_start(ul,b)
c_iter = find_start(ul,c)
endsumme = sumall(a_iter)*a+sumall(b_iter)*b-sumall(c_iter)*c
print(endsumme)