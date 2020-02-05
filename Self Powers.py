
j = 0
for i in range(1,1001):
    j += i**i

k = str(j)
print(k)
print("Last Ten Digits :- " ,k[-10::1])