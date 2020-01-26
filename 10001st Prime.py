# Starting with 2
x = []
for j in range(2,1000000):
    if x.__len__()>=10001:
        break
    else:
        for k in range(2,j):
            if j%k==0:
                break
        else:
            print(j)
            x.append(j)

print("The 10001'st prime number is %d"%x[x.__len__()-1])