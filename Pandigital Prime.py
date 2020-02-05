from math import *

def prime(y):
    for z in range(2 ,ceil(sqrt(y))):
        if y% z == 0:
            break
    else:
        print(y, " is prime")

for i in range(7000001,8000000,2):
    stri = str(i)
    for j in range(1,8):
        k = str(j)
        if k not in stri:
            break
    else:
        print(i)
        prime(i)




