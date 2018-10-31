import math

def get_next_prime_after(num):
	"""Return the next prime after the number
	
	This prime search is backed by Bertrand's postulate.
	It also uses the (6k +- 1) optimization.
	See:
		"https://en.wikipedia.org/wiki/Bertrand%27s_postulate"
		"https://en.wikipedia.org/wiki/Primality_test"
	
	Parameters:
		num -- reference number for the search of the next prime
	"""

	if num < 2:
		return 2
	elif num == 2:
		return 3
	
	# If the number is in the form (6k - 1) or (6k + 0),
	# check primality of (6k + 1) with the same k.
	# Note that (num % 6 = 5) is the same as (num % 6 = -1)
	start = 0
	if (num % 6 == 5) and is_prime(num + 2):
		return num + 2
	elif (num % 6 == 0) and is_prime(num + 1):
		return num + 1
	
	# Otherwise, get the next integer in the form (6k - 1)
	# after this number
	start = 0
	if (num % 6 == 5):
		start = num + 6
	else:
		start = num + (5 - (num % 6))

	# By Bertrand's postulate, there exists at least one prime p
	# such that n < p < 2n for all n > 1.
	# 
	# The following search uses the (6k +- 1) optimization.
	# Note that 2 divides (6i + 0), (6i + 2), (6i + 4) and
	# 3 divides (6i + 3). So, skip them.
	#
	# Note that the lower bound is modified to have the form (6k - 1)
	# after the number.
	# Every number i less that (2 * num) in the form (6k +- 1)
	# is checked for its primality.
	# Note that the step size is 6 to retain i in the form (6k - 1).
	for i in range(start, 2 * num, 6):
		if is_prime(i):
			return i
		elif is_prime(i + 2):
			return i + 2
	
	# This condition is unexpected, otherwise Bertrand's postulate is falsified.
	return -1

def is_prime(num):
	"""Return True if the number is prime, False otherwise
	
	This primality test uses the 6k +- 1 optimization.
	See:
		"https://en.wikipedia.org/wiki/Primality_test"
	
	Parameters:
		num -- testing number
	"""
	
	# Every integer can be represented as 6i + j,
	# where j = -1, 1, 2, 3, or 4.
	# Note that 2 divides (6i + 0), (6i + 2), (6i + 4) and
	# 3 divides (6i + 3).
	# So, if the number is not a prime if it is divisible by 2 or 3.
	if num < 2:
		return False
	elif num < 4:  # num = 2 or 3
		return True
	elif num % 2 == 0 or num % 3 == 0:
		return False
		
	# Check through all divisors of form (6i - 1) and (6i + 1).
	# Note that (5 + 6j) = (6i - 1), where j >= 0.
	# So, the step size is 6.
	#
	# Also note that it is only necessary to test divisors less than
	# or equal to the square root of the number.
	for i in range(5, int(math.sqrt(num)) + 1, 6):
	
		# Check with (6i - 1) and (6i + 1)
		if num % i == 0 or num % (i + 2) == 0:
			return False
	return True