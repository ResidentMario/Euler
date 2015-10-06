import time
import math
start_time = time.time()

# PROBLEM STATEMENT:
# What is the 10 001st prime number?

# SOLUTION:
# We wrote a well-optimized prime number checking algorithm as part of the legwork in problem 3, so we can use that here to our advantage.
# The isPrime(n) method below is a copy of the same method as I wrote it for problem 3 (you can't import p3.py because it's a script, not a library, and will execute when you do so).

# COPIED FOR PROBLEM 3
def candidateSmallPrimes(n):
	cap = math.floor(n**(1/2))
	return [2, 3, 5, 7, 11, 13, 17] + [x for x in range(19, cap, 2) if x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0 and x%11!=0 and x%13!=0 and x%17!=0]

def isPrime(n):
	cap = math.floor(n**(1/2))
	for smallPrime in candidateSmallPrimes(n):
		if isPrime(smallPrime):
			if n%smallPrime==0:
				return False
		else:
			continue
	return True
	print(s)

# END COPIED FROM PROBLEM 3
	
i = 1
n = 0
while(True):
	if n == 10001:
		print(i)
		break
	elif isPrime(i):
		print(i)
		n += 1
	i += 1

print("Execution time: ~%s seconds" %  format((time.time() - start_time), ".3f"))
