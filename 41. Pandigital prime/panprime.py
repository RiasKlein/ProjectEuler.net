#################################################################################
#
#	panprime.py
#	
#	Project Euler Problem 41
#	Pandigital prime
#
#	We shall say that an n-digit number is pandigital if it makes use of all
#	of its digits 1 to n exactly once. For example, 2143 is a 4-digit
#	pandigital and is also prime.
#
#	What is the larget n-digit pandigital prime that exists?
#
#	Shunman Tse
#
#################################################################################

# primes
# 	Function returns a list of prime numbers < n
#	Source: http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
def primes ( n ):
    sieve = [True] * n
    for i in xrange(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) / (2 * i) + 1)
    return [2] + [i for i in xrange(3, n, 2) if sieve[i]]

# isPandigital
#	Verifies whether the parameter (value) is a pandigital value
#	Returns True if value is pandigital, False otherwise
def isPandigital ( value ):
	digits = []
	value = str(value)
	for digit in value:
		if digit not in digits:
			digits.append (digit)

	for x in range (1, len(value) + 1):
		if str(x) not in digits:
			return False

	return True

def main():
	list = primes (100000000)
	largest_prime = 0

	# Check each prime in list to see which are pandigital
	for prime in list:
		if isPandigital (prime):
			if prime > largest_prime: 
				largest_prime = prime
				print (largest_prime)

main()