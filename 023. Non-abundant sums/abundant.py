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

import math

max_value = 28123
abundant_numbers = []	# List to hold all the abundant numbers we find
numbers_markers = []	# List of markers for numbers to keep

def main():
	init()		# Initialize 

	# Find all the values that are sums of abundant numbers and mark them
	for i in range ( len (abundant_numbers)):
		for j in range (i, len(abundant_numbers)):
			sum_of_i_j = abundant_numbers[i] + abundant_numbers[j]
			if sum_of_i_j <= max_value:
				numbers_markers[sum_of_i_j] = False
			else:
				break
				
		if i > max_value / 2:
			break
	
	# Total up anything that isn't marked
	total = 0
	for i in range ( len (numbers_markers) ):
		if numbers_markers[i] == True:
			total += i
			
	# Output the result
	print (total)

# init
#	Runs setup functions to create necessary lists of numbers	
def init():
	init_abundant_numbers()
	init_numbers_markers()

# init_numbers_markers
#	Sets up a list of boolean markers for us to know which numbers to cross out / keep
def init_numbers_markers ():
	global numbers_markers
	numbers_markers = [True] * (max_value + 1)

# init_abundant_numbers
#	Creates list of abundant numbers up to max value
def init_abundant_numbers ():
	global abundant_numbers
	for num in range (12, max_value + 1):
		if is_abundant (num):
			abundant_numbers.append (num)

# is_abundant
#	Tests whether num is an abundant number or not
def is_abundant ( num ):
	sum_of_proper_divisors = 0

	for x in range ( 2, int (math.sqrt(num)) + 1):
		if num % x == 0:
			temp = num
			sum_of_proper_divisors += (temp / x)
			
			# If we have both divisors as the same value, don't overcount
			# Example: 16 = 4 * 4; we only want to count 4 once
			if (x != (temp/x)):
				sum_of_proper_divisors += x

	# Consider the factor of 1 which works for all values
	sum_of_proper_divisors += 1

	if sum_of_proper_divisors > num:
		return True
	return False
	
main()
