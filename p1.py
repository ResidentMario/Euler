import time
start_time = time.time()

# PROBLEM STATEMENT:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# SOLUTION:
# This problem can be treated by summing up multiples of 5, then summing up multiples of 3, and then removing from this set their intersection: multiples of 15.
result = 0
for n in range (3, 1000, 3):
	result += n
for n in range (5, 1000, 5):
	if n%15 != 0:
		result += n
print(result)

print("Execution time: ~%s seconds" %  format((time.time() - start_time), ".3f"))
