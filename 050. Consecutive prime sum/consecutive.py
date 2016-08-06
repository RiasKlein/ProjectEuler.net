#################################################################################
#
#	consecutive.py
#	
#	Project Euler Problem 50
#	Consecutive prime sum
#
#	The prime 41, can be written as the sum of six consecutive primes:
#		41 = 2 + 3 + 5 + 7 + 11 + 13
#	This is the longest sum of consecutive primes that adds to a prime below 
#	one-hundred.
#
#	The longest sum of consecutive primes below one-thousand that adds to a 
#	prime, contains 21 terms, and is equal to 953.
#
#	Which prime, below one-million, can be written as the sum of the most 
#	consecutive primes?
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

def getLongestChain ( num, primes_list ):
	longestChain = 1

	for starting_index in range ( len (primes_list)):
		index = starting_index
		sum_of_chain = primes_list[index]
		current_chain = 1

		if sum_of_chain >= num:
			return longestChain
		
		while sum_of_chain < num:
			index += 1
			current_chain += 1
			sum_of_chain += primes_list[index] 

		if sum_of_chain == num:
			if current_chain > longestChain:
				longestChain = current_chain
				
	return (longestChain)

def main():
	primes_list = primes (1000000)

	longestChain = 0
	longestNum = 0
	for x in primes_list:
		if x > 200000:
			chain_length = getLongestChain (x, primes_list)
			if chain_length > longestChain:
				longestChain = chain_length
				longestNum = x
				print (str (longestNum) + ' with chain of: ' + str (longestChain))

	print (longestNum)

main()