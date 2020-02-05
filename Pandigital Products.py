import time
t = time.time()

per = []
for l in range(1,10):                  # per = list("123456789")
    per.append(str(l))
print(per)

whole = []

#
for i in range(1,100):
    for j in range(i,2000):
        current_digits = []
        k = i*j
        for q in str(i):                # a=list(str(a)+str(b)+str(a*b))
            current_digits.append(q)
        for r in str(j):
            current_digits.append(r)
        for s in str(k):
                current_digits.append(s)
        if len(current_digits)==9:
            if sorted(current_digits)==per:
                print(i," * ",j," = ",k)
                if k not in whole:
                    whole.append(k)

print(sum(whole))

print(time.time()-t)

"""QUICK METHOD
    
def pandigital(a,b):
    a=list(str(a)+str(b)+str(a*b))
    a.sort()
    if a==list("123456789"):
        return True
    return False

num=[]

for a in range(5000): #this value's are a guess
    for b in range(5000):
        if len(str(a))+len(str(b))+len(str(a*b))>9:
            break
        elif len(str(a))+len(str(b))+len(str(a*b))!=9:
            pass
        else:
            if pandigital(a,b)==True and a*b not in num:
                num.append(a*b)
print sum(num)

"""