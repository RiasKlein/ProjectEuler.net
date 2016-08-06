#################################################################################
#
#	self..py
#
#	Project Euler (projecteuler.net) Problem 48
#	Self powers
#
#	The series: 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317
#	Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
#
#	Program by: Shunman Tse
#
#################################################################################

trim_mod = 10000000000		# This will trim for the last 10 digits

# getSelfPower
# Function gets the last 10 digits of the self power of num
def getSelfPower ( num ):
	product = 1
	
	# Run this loop num times
	for x in range (0, num):
		# Multiply the current product by num
		# We don't want the entire product and so we use modulo to trim it
		product *= num
		product = product % trim_mod
		
	# Return the last 10 digits of the self power of num
	return product

# main
def main():
	sum = 0
	
	# This will run from 1 ~ 1000
	for x in range (1, 1001):
		sum += (getSelfPower (x) % trim_mod)
	
	# Trim sum to display 10 digits
	print (sum % trim_mod)
	
main()