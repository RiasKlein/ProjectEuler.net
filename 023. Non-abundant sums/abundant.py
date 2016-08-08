################################################################################
#
#	abundant.py
#	
#	Project Euler Problem 23
#	Non-abundant sums
#
#	A perfect number is a number for which the sum of its proper divisors is 
#	exactly equal to the number. For example, the sum of the proper divisors 
#	of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that:
#	28 is a perfect number.	
#
#	A number n is called deficient if the sum of its proper divisors is less 
#	than n and it is called abundant if this sum exceeds n.
#
#	Find the sum of all the positive integers which cannot be written as the 
#	sum of two abundant numbers.
#
#	Program by Shunman Tse
#
################################################################################

# The basic strategy to tackle this problem would be to:
#	1. Find all the abundant numbers up to 28123 (which is the upper bound)
#	2. Find the sum of all positive integers which cannot be made by the
#		sum of two abundant numbers

import math, itertools

abundant_numbers = []	# List to hold all the abundant numbers we find

def main():
	# Initialize the abundant_numbers array by getting all abundant numbers
	init_abundant_numbers ()

	print (abundant_numbers)

def init_abundant_numbers ():
	global abundant_numbers
	for num in range (12, 28124):
		if is_abundant (num):
			abundant_numbers.append (num)

# is_abundant
#	Tests whether num is an abundant number or not
def is_abundant ( num ):
	sum_of_proper_divisors = 0

	for x in range ( 2, int (math.sqrt(num)) + 1):
		if num % x == 0:
			temp = num
			sum_of_proper_divisors += x
			sum_of_proper_divisors += (temp / x)

	# Consider the factor of 1 which works for all values
	sum_of_proper_divisors += 1

	if sum_of_proper_divisors > num:
		return True
	return False
	

main()
