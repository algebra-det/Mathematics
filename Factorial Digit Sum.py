
x = int(input("Enter the number: "))
fact = 1
for i in range(1,x+1):
    fact *= i

print("Factorial of %d is "%x,fact)

sum = 0
for j in str(fact):
    sum +=int(j)

print("Their Sum is ",sum)
