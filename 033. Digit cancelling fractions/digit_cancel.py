################################################################################
#
#   digit_cancel.py
# 
#   Project Euler 33
#   Digit cancelling fractions
#
#   The fraction 49/98 is a curious fraction, as an inexperienced mathematician 
#   in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
#   which is correct, is obtained by canceling the 9s.
#
#   We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
#   There are exactly four non-trivial examples of this type of fraction, less 
#   than one in value, and containing two digits in the numerator and denominator.
#
#   If the product of these four fractions is given in its lowest common terms, 
#   find the value of the denominator.
#
#   Program by Shunman Tse 
#
################################################################################

import fractions 

# cancel_common_digit
#	Returns the numerator and denominator with the common digit removed
#	Assumption: numerator and denominator each has 2 digits and are strings
def cancel_common_digit ( numerator, denominator ):
	numerator = str(numerator)
	denominator = str(denominator)

	for index_n in range (0, len(numerator)):
		for index_d in range (0, len(denominator)):

			if (numerator[index_n] == denominator[index_d]):

				# Handle the numerator
				if index_n == 0:
					# The common digit is on the left, keep the digit on the right
					numerator = numerator[1:]
				else:
					numerator = numerator[:1]
					
				# Handle the denominator
				if index_d == 0:
					denominator = denominator[1:]
				else:
					denominator = denominator[:1]
				
				return int(numerator), int(denominator)
				
	return int(numerator), int(denominator)

def main():
	prod_num = 1
	prod_den = 1
	
	for num in range (10, 99):
		for den in range (num, 100):
			numerator, denominator = cancel_common_digit (num, den)
			
			# Let's start taking out the cases that do not count
			if numerator == 0 or denominator == 0 or numerator == denominator:
				pass
			elif len(str(numerator)) == 2 or len(str(denominator)) == 2:
				pass
			elif float(num) / float(den) != float (numerator) / float (denominator):
				pass
			elif '0' in str(num) or '0' in str(den):
				pass
			else:
				prod_num *= numerator
				prod_den *= denominator
				#print ("" + str(num) + "/" + str(den) + " = " + str(numerator) + "/" + str(denominator) )
	
	# Find the greatest common divisor 
	gcd = fractions.gcd (prod_num, prod_den)
	
	# Get the simplified denominator
	prod_den /= gcd
	print (prod_den)
	
main()