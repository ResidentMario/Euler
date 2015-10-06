import time
import math
start_time = time.time()

# PROBLEM STATEMENT:
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# SOLUTION:
# We can create a least common multiple by considering the common multiple of all of the numbers given and eliminating any factors that are themselves factors of other
# factors under consideration. e.g. the presence of 20 removes 2, 4, 5, and 10 from the construction.

# Dirty, unoptimized prime factorization algorithm that is sufficient to get the job done here, since we do not factorize numbers greater than 20.
# A smart prime factorization algorithm would be a modification of the solution algorithm for p3.py.
def factorize(n):
	for i in range(2, math.floor(n/2)):
		if n%i == 0:
			return [i] + factorize(n/i)
	return [math.floor(n)]

# Merges two lists in a such a way that items present in multiples in both lists are added in the greatest number present in one.
# ex. merge([1,2,2],[2,3])=[1,2,2,3])
def merge(l1, l2):
	ret = []
	for f in (set(l1) | set(l2)):
		ret += [f for numtimes in range(0, max(l1.count(f), l2.count(f)))]
	return ret

solution_factorized = []
for f in range(20,1,-1):
	# print('Factors so far:', solution_factorized)
	# print('Next factor factorized:', factorize(f))
	solution_factorized = merge(solution_factorized, factorize(f))
solution = 1
for f in solution_factorized:
	solution *= f
	
print(solution)

print("Execution time: ~%s seconds" %  format((time.time() - start_time), ".3f"))
# Execution time is almost nothing.
