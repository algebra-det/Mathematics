# Sum of Even Fibonacci Numberes upto 4 million

x=0
y=1
z=0
sum=0

while z<4000000:
    z=x+y
    print(z)
    if z%2==0:
        sum+=z
    x=y
    y=z

print("Sum of Even Fibonacci series upto 4 million is: ",sum)
print("Bye")



