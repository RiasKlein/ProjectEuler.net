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

def reverse ( num ):
	return int (str (num) [::-1] )

def main():
	found = 0
	
	for x in range (1, 1000000000, 2):
		if x % 10 == 0:
			pass
		else:
			sum = x + reverse (x)
			sum = str(sum)
			if '2' in sum or '4' in sum or '6' in sum or '8' in sum or '0' in sum:
				pass
			else:
				found += 1
				
	print (found * 2)		
		
main()
