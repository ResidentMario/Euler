import time
start_time = time.time()

# PROBLEM STATEMENT:
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# SOLUTION:
# Loop
result = 0
i1 = 0
i2 = 1

while True:
	s = i1 + i2
	if s < 4000000:
		if s%2 == 0:
			result += s
		i1 = i2
		i2 = s
	else:
		break

print(result)

print("Execution time: ~%s seconds" %  format((time.time() - start_time), ".3f"))
