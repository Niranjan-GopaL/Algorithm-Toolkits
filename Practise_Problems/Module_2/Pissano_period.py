# Python3 program to calculate
# Fibonacci no. modulo m using
# Pisano Period

# Calculate and return Pisano Period
# The length of a Pisano Period for
# a given m ranges from 3 to m * m
def pisanoPeriod(m):
	prev, curr = 0, 1
	for i in range(0, m * m):
		prev, curr = curr, (prev + curr) % m
		
		# A Pisano Period starts with 01
		if (prev == 0 and curr == 1):
			return i + 1

# Calculate Fn mod m
def fibonacciModulo(n, m):
	
	# Getting the period
	pisano_period = pisanoPeriod(m)
	
	# Taking mod of N with
	# period length
	n = n % pisano_period
	
	prev, curr = 0, 1
	if n==0:
		return 0
	elif n==1:
		return 1
	for i in range(n-1):
		prev, curr = curr, prev + curr
		
	return (curr % m)



n , m = map(int, input().split())
print(fibonacciModulo(n, m))