import time
import math
start_time = time.time()

# PROBLEM STATEMENT:
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# SOLUTION:
# Trivial?
sumofsquares = squareofsum = 0
for n in range(1, 101):
	sumofsquares += n**2
	squareofsum += n
squareofsum = squareofsum**2

print(squareofsum - sumofsquares)

print("Execution time: ~%s seconds" %  format((time.time() - start_time), ".3f"))
