x = 2**1000
print(x)
y = 0
z = []
while x>0:
	a = x%10
	z.append(a)
	x = x//10
print(z)

for i in z:
	y +=i
print(y)

#OR

sum=0
for n in str(2**1000):
    sum+=int(n)
print(sum)
