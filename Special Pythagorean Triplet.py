import math
b = 0
for i in range(1,400):
	if b!=0:
		break
	else:
		for j in range(i,400):
			c = i*i + j*j
			a = math.sqrt(c)
			if i + j + a == 1000:
				print("%d + %d = %d "%(i,j,a))
				b = i*j*a
				print("Their product is ",b)
				break