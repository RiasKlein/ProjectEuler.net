#################################################################################
#
#	const.py
#
#	Project Euler Problem 40
#	Champernowne's constant
#
#	An irrational decimal fraction is created by concatenating the positive 
#	integers:
#		0.123456789101112131415161718192021...
#	It can be see that the 12th digit of the fractional part is 1.
#	If d_n represents the nth digit of the fractional part,
#	find the value of the following expression:
#		d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000
#
#	Program by Shunman Tse
#
#################################################################################

# genConstant
#	Creates a string with the integers concatenated up to parameter stop_value
#	To get d_n, access the nth index of the returned string
def genConstant ( stop_value ):
	constant = ''
	for x in range (stop_value + 1):
		constant += str(x)
	return constant

def main():
	# First we generate the constant
	d = genConstant (1000000)

	# Solve for the desired value with the provided indices
	value = int (d[1])
	value *= int (d[10])
	value *= int (d[100])
	value *= int (d[1000])
	value *= int (d[10000])
	value *= int (d[100000])
	value *= int (d[1000000])

	# Output the value 
	print (value)

main()

