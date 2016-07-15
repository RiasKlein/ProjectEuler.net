#################################################################################
#
#	primeperm.py
#	
#	Project Euler Problem 49
#	Prime permutations
#
#	The arithmetic sequence, 1487, 4817, 8147, in which each of the terms 
#	increases by 3330, is unusual in two ways: 
#	(i) each of the three terms are prime, and, 
#	(ii) each of the 4-digit numbers are permutations of one another.
#
#	There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
#	exhibiting this property, but there is one other 4-digit increasing sequence.
#
#	What 12-digit number do you form by concatenating the three terms in this sequence?
#
#	Shunman Tse
#
#################################################################################

import itertools

# primes
# 	Function returns a list of prime numbers < n
#	Source: http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
def primes ( n ):
    sieve = [True] * n
    for i in xrange(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) / (2 * i) + 1)
    return [2] + [i for i in xrange(3, n, 2) if sieve[i]]

def delNon4DigitPrimes ( list ):
	new_list = []
	for x in list:
		if len(str(x)) == 4:
			new_list.append(x)
	return new_list

def getPermutationPrimes ( list_of_primes, prime ):
	digits_of_prime = []
	for x in str(prime):
		digits_of_prime.append (x)
	digits_of_prime.sort()

	permutations = []
	permutations.append (prime)

	for num in list_of_primes:
		if num == prime:
			break
		digits_of_num = []
		for x in str(num):
			digits_of_num.append (x)
		digits_of_num.sort()
		if digits_of_num == digits_of_prime:
			permutations.append (num)

	if len (permutations) >= 3:
		permutations.sort()
		return permutations
	else:
		return

def main():
	# Generate all primes up to 10,000 (includes all 4-digit values)
	list_of_primes = primes (10000)	

	# Remove all non 4-digit primes from the list
	list_of_primes = delNon4DigitPrimes ( list_of_primes )

	for x in range (0, len(list_of_primes)):
		multiples = getPermutationPrimes (list_of_primes, list_of_primes[x])
		if multiples is not None:
			# Generate all the permutations of lists of multiples
			permutations = list (itertools.permutations (multiples, 3))

			# Each element of permutations is a list
			for list_of_multiples in permutations:
				if list_of_multiples[1] - list_of_multiples[0] == list_of_multiples[2] - list_of_multiples[1]:
					if list_of_multiples[0] < list_of_multiples[1] < list_of_multiples[2] and list_of_multiples[0] != 1487:
						print (list_of_multiples)

main()