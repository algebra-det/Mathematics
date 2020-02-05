
sum = 0
for i in range(1,1000000):
  j = str(i)
  if j == j[::-1]:
    k = bin(int(j)).split("b",2)
    l = str(k[1])
    if l[0]=="0":         #excluding all palindromic number which have 0 as leading value in base 2
      pass
    else:
      if l == l[::-1]:                # or check palindrome.py file for other way
        print(j , " With bin ",l)
        sum+=i

print("Sum of all palindromic in base 10 and 2 is ",sum)
