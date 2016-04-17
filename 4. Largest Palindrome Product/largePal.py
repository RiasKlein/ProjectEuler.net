#################################################################################
#
#	largePal.py
#
#	Project Euler (projecteuler.net) Problem 4
#	Largest Palindrome Product
#
#	A palindromic number reads the same both ways. The largest palindrome 
#	made from the product of two 2-digit numbers is 9009 = 91 * 99.
#	Find the largest palindrome made from the product of two 3-digit numbers.
#	ANS: 906609	
#
#	Program by: Shunman Tse
#
#################################################################################

# detectPalindrome
#	Detects a palindrome by reversing a value and comparing with the original value
def detectPalindrome ( value ):
	# A palindrome reads the same both ways
	
	# Convert value to a string, reverse it, and convert back to int
	value_rev = int(str(value)[::-1])	
	
	# Now compare the two values to see if we have a palindrome
	if value == value_rev:
		return True
	else:
		return False
	
def main():
	# Keep track of the largest palindrome that we found
	largest_palindrome = 0
	
	# Since we want the largest palindrome, let's start with 900, 900 as base values
	# We will increment the two variables from 900 ~ 999 and create products
	# If we find a palindrome, we will record that in largest_palindrome
	for i in range (0, 100):
		for j in range (0, 100):
			x = 900 + i
			y = 900 + j
			if detectPalindrome( x * y ) and ( x * y ) > largest_palindrome:
				largest_palindrome = (x * y)
				
	print (largest_palindrome)
	
main()
