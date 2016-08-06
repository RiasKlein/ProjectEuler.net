#################################################################################
#
#	longCol.py
#
#	Project Euler (projecteuler.net) Problem 14
#	Longest Collatz sequence
#
#	The following iterative sequence is defined for the set of positive ints:
#		n -> n / 2 (n is even)
#		n -> 3n + 1 (n is odd)
#	Using the rule above and starting with 13, we generate the following sequence:
#		13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#	It can be seen that this sequence (starting at 13 and finishing at 1) contains
#	10 terms. Although it has not been proved yet (Collatz Problem), it is 
#	thought that all starting numbers finish at 1.
#	
#	Which starting number, under one million, produces the longest chain?
#	ANS: 837799
#
#	Program by: Shunman Tse
#
#################################################################################

# Let's take a dynamic programming approach
dict = {}
dict [13] = 10

# getNextTerm
#	Gets the next term in the Collatz Sequence
def getNextTerm ( n ):
	if n % 2 == 0:
		# if n is even
		return n / 2
	else:
		# n is odd
		return (3 * n + 1)

# getChainLen
#	Function returns the length of the chain starting with n
def getChainLen ( n ):
	len = 2
	
	next_term = 1
	if n == 1:
		return 1
	else:
		next_term = getNextTerm ( n )
		
	if (dict.has_key(next_term)):
		return (len + dict.get(next_term) - 1)
	
	while (next_term != 1):
		len += 1
		next_term = getNextTerm (next_term)
		
	return len

# Populate our dictionary with chain lengths for 1 ~ 1 million	
for x in range (1, 1000000):

	# First, we get the chain length of the current value
	chain_len = getChainLen (x)
	
	# Now we add the new chain length into our dictionary
	dict [x] = chain_len

# Get the largest chain value from the dictionary	
val = list (dict.values())
key = list (dict.keys())
print ( key [val.index(max(val))])