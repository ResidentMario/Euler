import time
start_time = time.time()

top = 2000000

# PROBLEM STATEMENT:
# Find the sum of all the primes below two million.

# SOLUTION:
# OK this time I'll write a proper sieve.
solution = 0

notprimeBooleans = [False] * top
p = 2
while True:
	for x in range(2*p, top, p):
		notprimeBooleans[x] = True
	p += 1
	if p >= top:
		break
	while p < top:
		if notprimeBooleans[p]:
			p += 1
		else:
			break

for i in range(2, top):
	# Note: Start at 2 to exclude 1.
	if notprimeBooleans[i] == False:
		solution += i

print(solution)

print("Execution time: ~%s seconds" %  format((time.time() - start_time), ".3f"))
# ~1.35 seconds execution time.
