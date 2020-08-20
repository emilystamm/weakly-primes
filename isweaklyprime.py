# isweaklyprime.py
from sympy import isprime


# isweakly(p,b)
# -------------------
# Input: p,b integers
# Ouput: True if p is a weakly prime base b
def isweakly(p,b):
    if not isprime(p): return False
    if b == 3 and p == 2: return True
    else:
        i = 0
        while(p>=b**i):
            # check all p+jb^i
            j = 1
            t = 0
            current = p + j*b**i
            while(p % b**i != current % b**(i+1)):
                if isprime(current): return False
                t = t + 1
                j = j + 1
                current = p + j*b**i
            # check all p-jb^i		
            for j in range(1,b-t):
                current = p - j*b**i
                if isprime(current): return False
            # increient the power	
            i = i + 1
        return True
