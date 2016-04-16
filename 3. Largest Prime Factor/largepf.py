#################################################################################
#
#	largepf.py
#
#	Project Euler (projecteuler.net) Problem 3
#	Largest Prime Factor
#
#	The prime factors of 13195 are 5, 7, 13 and 29.
#	What is the largest prime factor of the number 600851475143 ?
#
#	Program by: Shunman Tse
#
#################################################################################

import math

# primes
# 	Function returns a list of prime numbers < n
#	Source: http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
def primes ( n ):
    sieve = [True] * n
    for i in xrange(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) / (2 * i) + 1)
    return [2] + [i for i in xrange(3, n, 2) if sieve[i]]
	
# getLargestPrimeFactor
#	Function returns the largest prime factor of the provided value
#	primes is a list of prime numbers up to the sqrt (value)
def getLargestPrimeFactor (value, primes):
	factors = []
	for number in primes:
		if value % number == 0:
			factors.append(number)
	return factors[-1]
	
def main():
	value = 600851475143 
	prime_numbers = primes ( int(math.sqrt(value)) )
	largestFactor = getLargestPrimeFactor (value, prime_numbers)
	print ("Largest Prime Factor of " + str(value) + " is: " + str(largestFactor))
	
main()