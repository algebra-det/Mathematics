from itertools import permutations

a = list(permutations("0123456789"))
b = ''
b = b.join(a[999999])
print(a[999999])
print(len(a))
print(b)

