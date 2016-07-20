#################################################################################
#
#	comb.py
#
#	Project Euler Problem 53
#	Combinatoric selections
#
#	There are exactly 10 ways of selecting three from five, 12345:
#		123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#	In combinatorics, we use the notation: 5C3 = 10
#
#	In general:
#		nCr = n! / (r! * (n-r)!), where r <= n
#	It is not until n = 23, that a value exceeds one-million:
#		23C10 = 1144066
#
#	How many, not necessarily distinct, values of nCr, for 1 <= n <= 100,
#	are greater than one-million?
#	
#################################################################################

import operator as op

# ncr
#	Returns the result of nCr (combinations)
#	Source: http://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

def main():
	# Counter for solutions greater than 1 million
	greater_than_one_million = 0

	# Check all n and r values from 1 ~ 101
	for n in range (1, 101):
		for r in range (1, n+1):
			value = ncr (n, r)

			# If combinations value is greater than one million, increase the counter
			if value > 1000000:
				greater_than_one_million += 1

	print (greater_than_one_million)

main()