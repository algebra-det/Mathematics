x = 0
y = 0
for i in range(1,101):
    x += i*i
print(x)

for i in range(1,101):
    y+=i
z = y**2

print(z)

difference = z - x
print("Difference is :- ",difference)