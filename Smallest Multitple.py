x=0
for i in range(2500,1000000000,20):
    if x!=0:
        break
    else:
        for j in range(2,21):
            if i%j==0:
                if j>=20:
                    x = i
                    break
            else:
                break

print(x)
