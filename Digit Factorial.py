def fact(a):
  mul = 1
  for j in range(a,0,-1):
    mul*=j
  return mul

addit = 0
for i in range(10,100000):
  sum = 0
  k = i
  for l in str(i):
    sum+=fact(int(l))
  if sum == k:
    print(sum)
    addit+=sum

print("Total Sum of such numbers - ",addit)
