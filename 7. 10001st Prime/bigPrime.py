#################################################################################
#
#	bigPrime.py
#
#	Project Euler (projecteuler.net) Problem 7
#	10001st prime
#
#	By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
#	we can see that the 6th prime is 13.
#
#	What is the 10,001st prime number?
#	Ans: 104759
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
	
def main():
	value = 110000 
	prime_numbers = primes ( value )
	print ("The 10,001st prime number is: " + str(prime_numbers[10001]))
	
main()