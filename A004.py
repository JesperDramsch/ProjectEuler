import numpy

def testPalindrome(n):
    len_n = len(str(n))
    n=str(n)
    n_mirror=""
    for x in range(-1,-len_n-1,-1):
        n_mirror+=n[x]
        
    if n_mirror==n:
        return True
    else:
        return False
pali_tmp=0
for y in range(999,100,-1):
    for z in range(999,100,-1):
        if testPalindrome(y*z):
            if y*z>pali_tmp:
                pali_tmp=y*z

print(pali_tmp)
            