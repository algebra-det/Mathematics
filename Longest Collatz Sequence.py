from time import *
start_time = time()

e = lambda x :x//2
o = lambda x : (3*x)+1

z = 0
for x in range(1,1000000):
    a = x
    y = 1
    while x>1:
        if x%2==0:
            x = e(x)
            y+=1
        else:
            x = o(x)
            y+=1

    if y>z:
        z = y
        print("At %d, length of chain is %d"%(a,z))

print(time()-start_time)