# Range 10,000 - 998,001 for product of two 3 digit

def firstDigit(n):
    while n>10:                         #OR n = n/100000
        n = n/10
    return int(n)

def secondDigit(n):
    n = (n/10000)%10                    #OR n = (n%100000)/10000
    return int(n)

def thirdDigit(n):
    x = (n/1000)%10                     #OR n = (n%10000)/1000
    return int(x)

def thirdlastDigit(n):
    x = (n/100)%10                    #OR n = (n%1000)/100
    return int(x)

def secondLastDigit(n):
    n = (n/10)%10                      # OR n = (n%100)/10
    return int(n)

def lastDigit(n):
    n = n%10
    return n

for n in range(900000,998002):
    if firstDigit(n)==lastDigit(n):
        if secondDigit(n)==secondLastDigit(n):
            if thirdDigit(n)==thirdlastDigit(n):
                for i in range(100,1000):
                    for j in range(i,1000):
                        if i*j==n:
                            print(n,"with multiples %d*%d"%(i,j))


print()
print("first digit ",firstDigit(226498))
print("second digit ", secondDigit(226498))
print("third digit ", thirdDigit(226498))
print("thirdlast digit ", thirdlastDigit(226498))
print("secondlast digit ",secondLastDigit(226498))
print("last digit ", lastDigit(226498))