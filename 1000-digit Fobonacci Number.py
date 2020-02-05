
x = 0
y = 1
print("1  at  1")
for i in range(2,10000):
        z = x + y
        x = y
        y = z
        print(z," at ",i)
        a = str(z)
        if len(a)==1000:
            print("So 10 Digits is at ",i)
            break