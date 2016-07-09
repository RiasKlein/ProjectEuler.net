#################################################################################
#
#	pan.py
#	Project Euler Problem 32
#	Pandigital Products
#
#	We shall say that an n-digit number is pandigital if it makes use of all the 
#	digits 1 to n exactly once; 
#		for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
#	The product 7254 is unusual, as the identity, 39 * 186 = 7254, 
#	containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
#	Find the sum of all products whose multiplicand/multiplier/product identity 
#	can be written as a 1 through 9 pandigital.
#
#	Program by Shunman Tse
#
#################################################################################

import math

len_pandigital = 9

def digit_in_list ( digit, number_list ):
	digit_found = False

	for x in number_list:
		if str(digit) in str(x):
			return True

	return False

def digit_count ( number_list ):
	digit_count = 0
	for x in number_list:
		digit_count += len (str(x))

	return digit_count

def pandigital_test ( start, end, number_list ):

	for x in range (start, end + 1):
		if (digit_in_list (x, number_list) == False):
			return False

	return True

# Find the stopping point
max_value = '9' * len_pandigital
max_value = int (math.sqrt (float(max_value)))

product_list = []
product_sum = 0

for multiplicand in range (1, max_value + 1):
	for multiplier in range (1, max_value + 1):
		
		product = multiplicand * multiplier
		number_list = []
		number_list.append (product)
		number_list.append (multiplier)
		number_list.append (multiplicand)

		if digit_count (number_list) > len_pandigital:
			break

		if (pandigital_test ( 1, len_pandigital, number_list)):
			if (product not in product_list):
				product_list.append (product)
				product_sum += product
				print ("Found: " + str(multiplier) + ' * ' + str(multiplicand) + ' = ' + str(product))

print (product_sum)



