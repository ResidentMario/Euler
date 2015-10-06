import time
start_time = time.time()

# PROBLEM STATEMENT:
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

# SOLUTION:
# Through substitution we know that a + b + SQRT(a**2 + b**2) = 1000.
# We can find our answer by taking only values of a and b for which the latter value, SQRT(a**2 + b**2), is a whole number, and then flinging them against 1000.
# Since triples can occur in all sorts of crazy combinations.
# BUT there is a general property that all c = 4n + 1 for some n. So we can generate c with which to test a and b.
# It can be shown algebraically that, using the fact that the minimum value that any of the variables can take on is 1, the largest values they can take on are capped:
# c_max = 998, implying that n_max = 249.
# b_max given some n_max is demonstrably 998-4n.
# We iterate through this constrained range to create our a, then test it against the Pythagorean relationship. The first a that proves sufficient is our answer.
# (note that the answering print statement is a*b*c. This is because Project Euler only ever accepts one number as answer, but of course it's the numbers that are interesting,
#  not their product...)

for n in range(1,250):
	for b in range(1, 998 - 4*n):
		c = 4*n + 1
		a = 1000 - b - c
		if a**2 + b**2 == c**2:
			print(a*b*c)
			break

print("Execution time: ~%s seconds" %  format((time.time() - start_time), ".3f"))
# Execution in <0.2 seconds time.
