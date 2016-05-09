#################################################################################
#
#	fifths.py
#
#	Project Euler (projecteuler.net) Problem 34
#	Digit factorials
#
#	145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145
#	Find the sum of all numbers which are equal to the sum of the factorial 
#	of their digits.
#
#	Note: 1! = 1 and 2! = 2 but they are not sums and are not included.
#
#	Program by: Shunman Tse
#
#################################################################################

import math

"""
Single digit values will not count as sums and therefore we start with the
lower bound of 10. As for how high we are going, we can go to 1 million.
"""

# main
def main():
	sum = 0

	for x in range (10, 100000):
		sum_fact = 0
		num = x

		while (num > 0):
			digit = num % 10
			num /= 10
			num = int (num)

			sum_fact += math.factorial (digit)

		sum_fact = int (sum_fact)
		if sum_fact == x:
			sum += x

	print (sum)
	#print (math.factorial (4))
	
main()