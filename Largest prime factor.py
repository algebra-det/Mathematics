x=int(input("Enter the number :- "))

from array import *

a = array('i',[])

for z in range(1,x+1):
    if x%z==0:
        print("Factor",z)
        for y in range(2,z):
            if z%y==0:
                break
        else:
            print(z," is prime")
            a.append(z)

print("The prime factors are:- ")
for b in a:
    print(b,end=",")
