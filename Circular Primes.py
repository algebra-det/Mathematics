# Seive
import itertools, time
from Seive import seive



x = int(input("Enter Upto "))
t = time.time()

new_list = seive(x)
str_list = list(map(str,new_list))
print(new_list)
print(len(new_list))

circular = []

for i in new_list:
    j = str(i)
    permi = list(itertools.permutations(j))
    for k in permi:
        k = ''.join(k)
        if k not in str_list:
            break
    else:
        circular.append(i)

print(circular)
print(len(circular))
print(time.time()-t)

# Above Code will take around 3 -4 hours to execute
# Below one will get you the result in a couple of seconds

"""
    def sieve(n):
	is_prime = [True]*n
	is_prime[0] = False
	is_prime[1] = False
	is_prime[2] = True
	#even numbers except 2 have been eliminated
	for i in range(3,int(n**0.5+1),2):
		index = i*2
		while index < n:
			is_prime[index] = False
			index = index+i
	prime = [2]
	for i in range(3,n,2):
		if is_prime[i]:
			prime.append(i)
	return prime

#sieving prime numbers upto 1 million
primes = sieve(1000000)

#counter to count the instances
counter = 0

#looping through prime numbers
for i in primes:
	#assuming that there is no 2,4,6,8,5,0 in digits
	flag = True
	#start with tens digit
	number = i/10
	#looping through digits
	while number:
		if (number%10) % 2 == 0 or (number%10)%5 == 0:
			flag = False
			break
		number //= 10
	#check if flag is true or false
	if flag:
		length = len(str(i))
		number = i
		#assume that the circular permutations are prime
		counter += 1
		#loop to create circular permutations
		for j in range(length):
			number = (number%10)*10**(length-1)+number//10
			#if any permutation is not prime
			if number not in primes:
				#subtract one from counter
				counter -= 1
				break

#print the number of instances
print(counter)

"""