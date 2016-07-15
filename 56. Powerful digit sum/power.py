#################################################################################
#
#	power.py
#
#	Project Euler Problem 56
#	Powerful digit sum
#
#	A googol (10 ^ 100) is a massive number: one followed by one-hundred 
#	zeroes; 100^100 is almost unimaginably large: one followed by two-hundred 
#	zeroes. Despite their size, the sum of the digits in each number is
#	only 1.
#
#	Considering natural numbers of the form, a^b, where a, b < 100
#	what is the maximum digital sum?
#	
#################################################################################

# digitalSum
#	Iterates through a number one digit at a time and returns the sum of digits
def digitalSum (num):
	num = str(num)
	total = 0
	for x in num:
		total += int(x)
	return total

def main():
	greatest_sum = 0					# Variable to hold the greatest sum

	# Use for-loops to get all a^b expressions with a, b < 100
	for i in range (1, 100):
		for j in range (1, 100):
			num = i ** j				# Get the a^b value
			total = digitalSum (num)	# Get the sum of digits

			if total > greatest_sum:	# Save the sum if it's larger than the previous largest
				greatest_sum = total

	print ( greatest_sum )

main()