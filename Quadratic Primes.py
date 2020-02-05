
from Seive import seive
from time import time
t = time()

# Having a list of primes upto a certain number
lst = seive(10000)

# Function for checking and returning the prime numbers with number of primes for certain a &b
def for_primes(a,b):
    new_list = []               # new list for the primes of current a & b
    for i in range(0,1000):
        j = i*i +a*i + b
        if j in lst:
            new_list.append(j)
        else:
            print("%d with %d gives primes upto %d terms"%(a,b,len(new_list)))
            break
    return new_list

y = []  # for storing primes for highest yeilding a & b
z = 0   # for storing value of highest yeilding a
q = 0   # for storing value of highest yeilding b
for i in range(-1000,1000,1):   # i as a
    for j in range(1000):   # j as b
        k = for_primes(i,j)
        if len(k) >len(y):
            y = k
            print("As %d and %d "%(i,j))
            z = i
            q = j

print("As %d and %d we have total %d numbers of consecutive primes"%(z,q,len(y)))
print(y)
print(time()-t)