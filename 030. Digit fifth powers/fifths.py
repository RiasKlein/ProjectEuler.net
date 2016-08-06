#################################################################################
#
#	fifths.py
#
#	Project Euler (projecteuler.net) Problem 30
#	Digit fifth powers
#
#	Surprisingly there are only three numbers that can be written as the sum 
#	of fourth powers of their digits:
#		1634 = 1^4 + 6^4 + 3^4 + 4^4
#		8208 = 8^4 + 2^4 + 0^4 + 8^4
#		9474 = 9^4 + 4^4 + 7^4 + 4^4
#	As 1 = 1^4 is not a sum, it is not included
#	The sum of those numbers is: 1634 + 8208 + 9474 = 19316
#	
#	Find the sum of all the numbers that can be written as the sum of fifth 
#	powers of their digits.
#
#	Program by: Shunman Tse
#
#################################################################################

import math

"""
For this problem, we can extract each digit of the number that we are considering
by using modulo and then dividing by 10. For example if we have 1634:
	Do: 	1634 % 10 --> 4
	Then:	1634 / 10 --> 163
By repeating this procedure, we can extract all the digits of the number.
Then we can apply the fifth power to each of the extracted digits.
If the sum of the fifth powers equal the original number, we got a hit!

Now what is the upperbound?
The upperbound is less than 9^5 * 5 = 295245
So using 300K for the upperbound is more than enough
"""

# main
def main():
	sum = 0
	
	for x in range (2, 300000):
		sum_of_fifths = 0		# Sum of fifths for the current case
		num = x					# num is used to help extract digits of x
		
		while (num > 0):
			digit = num % 10	# get a digit from num
			num /= 10			# divide num by 10
			num = int(num)		# keep num as an int (truncates floats)
			
			sum_of_fifths += math.pow (digit, 5)
			sum_of_fifths = int (sum_of_fifths)
			
		if (sum_of_fifths == x):
			sum += sum_of_fifths
			print (sum_of_fifths)
			
	print ("Sum: " + str(sum))
	
main()