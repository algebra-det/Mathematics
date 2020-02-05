# this is a problem of nCr i.e. combination formula
# or we can say binomial theorem
# Learn more about binomial theorem to understand the concept more vigrously

import math

def ncr(n,r):   # making a function for nCr formula/ Binomial theorem
    return math.factorial(n) // (math.factorial(n-r) * math.factorial(r))

print(ncr(4,2))
print(ncr(40,20))