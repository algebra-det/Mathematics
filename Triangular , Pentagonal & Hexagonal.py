from time import time
t = time()

triangle = []
for i in range(286,60000):
    j = (i*(i+1))//2
    triangle.append(j)

pentagonal = []
for k in range(165,40000):
    l = (k*(3*k-1))//2
    pentagonal.append(l)


hexagonal = []
for m in range(143,30000):
    n = (m*(2*m-1))
    hexagonal.append(n)

print(hexagonal)
for o in triangle:
    if o in pentagonal and o in hexagonal:
        print(o)
        print(time()-t)
        break
