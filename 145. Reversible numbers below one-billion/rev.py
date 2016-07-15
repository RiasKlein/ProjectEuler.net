#################################################################################
#
#	rev.py
#
#	Project Euler Problem 145
#	How many reversible numbers are there below one-billion?
#
#	Some positive integers n have the property that the sum [ n + reverse(n) ] 
#	consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 
#	409 + 904 = 1313. We will call such numbers reversible; 
#	so 36, 63, 409, and 904 are reversible. 
#	Leading zeroes are not allowed in either n or reverse(n).
#
#	There are 120 reversible numbers below one-thousand.
#
#	How many reversible numbers are there below one-billion?
#
#	Shunman Tse
#
#################################################################################

def no_evens ( num ):
	num = str(num)
	for digit in num:
		if digit == '0' or digit == '2' or digit == '4' or digit == '6' or digit == '8':
			return False
	return True

def reverse ( num ):
	return int( str (num) [::-1] )

def no_leading_zero ( num ):
	num = str (num)
	if num[0] == '0':
		return False
	return True

def main():
	reversible_numbers = 0
	for x in range (1000):
		
