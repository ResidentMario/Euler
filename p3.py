import time
import math
start_time = time.time()

# PROBLEM STATEMENT:
# What is the largest prime factor of the number 600851475143 ?

# EXAMINATION:
# A brute force solution would be to simply count down, but it would never finish running.
# A theorem that can be easily proven states that if a number n has a prime factor k > SQRT(N), then it necessarily has some other complimentary factor j
# such that j < SQRT(N). j is not itself necessarily prime.
# The implication of this theorem is that we can limit our search to numbers less than SQRT(N). Find all primes less than that number,
# then divide it through n to see if it is a valid divisor. If it is, check to see if the dividend is prime. If it is then assuming we go bottom-to-top we are done:
# the smallest prime multiple would be paired with the largest prime multiple. Otherwise we keep going. If we reach the last small prime divisor and get no hits then,
# then that largest small prime divisor is the largest prime divisor, period.
# Another optimization step I've done is construct a sieve. The sieve generates candidate small primes by removing multiples from a list of [k: k < SQRT(n)].
# After a certain point there are diminishing returns to sieving: removing all multiples of 3, say, is much more useful than removing all multiples of 17.
# We divide n through the candidate small primes in our sieve to get candidate large primes, store those values, and then check to see that those numbers are actually
# themselves prime, recursively.

# SOLUTION:

def candidateSmallPrimes(n):
	cap = math.floor(n**(1/2))
	return [2, 3, 5, 7, 11, 13, 17] + [x for x in range(19, cap, 2) if x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0 and x%11!=0 and x%13!=0 and x%17!=0]

def largestPrimeFactor(n):
	if n in [2, 3, 5, 7, 11, 13, 17]:
		return n
	for smallPrime in candidateSmallPrimes(n)[::-1]:
		if n%smallPrime == 0 and largestPrimeFactor(smallPrime) == smallPrime:
			if largestPrimeFactor(n/smallPrime) == n/smallPrime:
				return n/smallPrime
			else:
				return smallPrime
		else:
			continue
	return n
		
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

# print(candidateSmallPrimes(600851475143))
print(largestPrimeFactor(600851475143))

print("Execution time: ~%s seconds" %  format((time.time() - start_time), ".3f"))
# Execution time is <0.25 seconds!
