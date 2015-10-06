import time
import math
start_time = time.time()

# PROBLEM STATEMENT:
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# EXAMINATION:
# Palindromes are easy to generate algorithmically, so it makes sense to generate the palindromes first and check whether or not they are prime second.
# The product of two 3-digit numbers ranges between 10000 (100**2) and 998001 (999**2).

# SOLUTION:

# Finding the palindromes could be optimized to run an order of magnitude faster by generating digits instead of checking them off form a list.
# For the purposes of this problem, this is fast enough, though: ~0.230 execution time for the chosen snippet.
def listPalindromesBetween(j,k):
	return [x for x in range(j,k) if isPalindrome(x)]

def isPalindrome(n):
	for i in range(0, math.floor(len(str(n))/2)):
		if str(n)[i] != str(n)[len(str(n)) - i - 1]:
			return False
	return True

# Is brute force "good enough" for checking the factorization of the palindrome list? Otherwise to find three-digit multiples we'd first need to write
# an efficient prime factorization algorithm...possible but a lot of work on my part. See p3.py.
# Also possible, a smarter stepping-down function.

palindromes = listPalindromesBetween(100000, 998001)
found_satisfiable_palindromes = []
for j in range(100, 1000):
	for k in range(100, 1000):
		if j*k in palindromes and j*k not in found_satisfiable_palindromes:
			found_satisfiable_palindromes.append(j*k)
print(max(found_satisfiable_palindromes))

print("Execution time: ~%s seconds" %  format((time.time() - start_time), ".3f"))
# Execution time is ~14 seconds. Could definitely be cut down to ~<1 second with two optimizations:
# 1. Generating palindromic numbers instead of, as now, checking which amongst an iteration of all integers satisfy the conditions for being palindromic.
# 2. Writing a smart two-integer stepping down function so that at any step the j,k chosen are such that j*k is the largest multiple in that range smaller than any already tried.
