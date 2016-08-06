#################################################################################
#
#	perm.py
#	
#	Project Euler Problem 52
#	Permuted Multiples
#
#	It can be seen that the number, 125874, and its double, 251748, contain 
#	exactly the same digits, but in a different order.
#
#	Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
#	contain the same digits.
#
#	Program by Shunman Tse
#
#################################################################################

def checkMultiples (num):
	# First we store all the desired multiples of x (in string form)
	x2 = str (num * 2)
	x3 = str (num * 3)
	x4 = str (num * 4)
	x5 = str (num * 5)
	x6 = str (num * 6)

	# Verify that each of the strings for the multiples have equal length
	# If the lengths are not the same, then we do not have the number we seek
	if len (x2) == len (x3) and len (x3) == len (x4) and len (x4) == len (x5) and len (x5) == len (x6):
		# Get the digits of x2
		x2_digits = []
		for digit in x2:
			x2_digits.append (digit)

		# Compare the digits of x2 with each of the other multiples
		for digit in x3:
			if digit not in x2_digits:
				return False

		for digit in x4:
			if digit not in x2_digits:
				return False

		for digit in x5:
			if digit not in x2_digits:
				return False

		for digit in x6:
			if digit not in x2_digits:
				return False		

		# If we found a number that works, output it 
		print (num)
		return True

	else:
		return False

def main ():
	# Testing for the desired number in the range 1 ~ 1 million
	for x in range (1, 1000000):
		checkMultiples (x)
		
main()
