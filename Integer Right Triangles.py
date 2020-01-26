from time import *
t = time()

max_count = 0
max_number = 0
for m in range(1,1001):
    count = 0
    for i in range(1,500):
        for j in range(i,500):
            k = (i**2 + j**2)**0.5
            l = i+j+k
            if l<=1000:
                count+=1
    if count>max_count:
        print("For %d we have total count %d" % (m, count))
        max_count= count
        max_number = m

print("We have %d counts for %d perimeter"%(max_count,max_number))
print(time()-t)