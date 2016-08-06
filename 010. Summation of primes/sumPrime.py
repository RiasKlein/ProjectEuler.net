#################################################################################
#
#	sumPrime.py
#
#	Project Euler (projecteuler.net) Problem 10
#	Summation of primes
#
#	The sum of primes below 10 is: 2 + 3 + 5 + 7 = 17.
#	Find the sum of all the primes below two million.
#	ANS: 142913828922
#
#	Program by: Shunman Tse
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
	
def main():
	# Generate list of primes under 2 million
	value = 2000000
	prime_numbers = primes (value)

	# Find the sum of those prime numbers
	sum = 0
	for num in prime_numbers:
		sum += num
	print (sum)
	
main()