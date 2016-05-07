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

"""
For this problem, we can extract each digit of the number that we are considering
by using modulo and then dividing by 10. For example if we have 1634:
	Do: 	1634 % 10 --> 4
	Then:	1634 / 10 --> 163
By repeating this procedure, we can extract all the digits of the number.
Then we can apply the fifth power to each of the extracted digits.
If the sum of the fifth powers equal the original number, we got a hit!
"""

# main
def main():
	
	
	
main()