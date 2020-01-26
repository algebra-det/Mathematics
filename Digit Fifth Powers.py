from time import time
t = time()

def individual():
    sum = 0
    for i in range(1000,200000):
        c = 0
        for k in str(i):
            c += int(k)**5
        if  c == i:
            sum +=c
            print(c)
    print("Sum of these numbers - ", sum)

individual()
print(time()-t)



