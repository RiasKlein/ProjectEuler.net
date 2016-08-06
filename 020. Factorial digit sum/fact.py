#################################################################################
#
#	fact.py
#
#	Project Euler (projecteuler.net) Problem 20
#	Factorial digit sum
#
#	n! means n(n-1) * ... * 3 * 2 * 1
#	For example, 10! = 10 * 9 * 8 * ... * 3 * 2 * 1 = 3628800
#	The sum of its digits is: 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27
#	Find the sum of the digits in the number 100!
#	ANS:
#
#	Program by: Shunman Tse
#
#################################################################################

# addDigits
#	Function adds all the digits in the number n by adding the results of 
#	n % 10 and dividing 10 as long as it is larger than 0
def addDigits ( n ):
	sum = 0
	while ( n > 0 ):
		sum += n % 10
		n /= 10
	return sum

# main
#	Function prints out the sum of the digits in n factorial 
def main():
	n = 100
	result = 1
	for x in range (1, n+1):
		result *= x
	print (addDigits (result))
	
main()