#################################################################################
#
#	double.py
#
#	Project Euler (projecteuler.net) Problem 36
#	Double-base palindromes
#
#	The decimal number, 585 = 1001001001 (binary) is palindromic in both bases
#	Find the sum of all numbers, less than 1 million, 
#	which are palindromic in base 10 and base 2.
#
#	Program by: Shunman Tse
#
#################################################################################

import math

# test_bpalindrome
#	Function tests whether the provided number is palindromic in base 2
def test_bpalindrome ( num ):
	# First let's get the binary form of the number
	binary_num = str (bin (num)) [2:]

	# Now let's check for palindrome!
	if binary_num == binary_num [::-1]:
		return True
	else:
		return False

# test_dpalindrome
#	Function tests whether the provided number is palindromic in base 10
def test_dpalindrome (num):
	# Check for a palindrome!
	if str(num) == str(num) [::-1]:
		return True
	else:
		return False

# main
def main():
	sum = 0

	for x in range (1, 1000000):
		if test_dpalindrome(x) and test_bpalindrome (x):
			sum += x

	print (sum)
	


	
main()