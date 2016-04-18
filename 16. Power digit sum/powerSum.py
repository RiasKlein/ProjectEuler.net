#################################################################################
#
#	powerSum.py
#
#	Project Euler (projecteuler.net) Problem 16
#	Power digit sum
#
#	2^15 = 32768 and the sum of its digits is: 3 + 2 + 7 + 6 + 8 = 26
#	What is the sum of the digits of the number: 2^1000?
#	ANS:
#
#	Program by: Shunman Tse
#
#################################################################################

val = 2
exp = 1000

# Store 2^1000 in the variable 'val'
for x in range (exp-1):
	val *= 2

# Now we want to get the sum of all the digits	
sum = 0

while val > 0:
	r = val % 10		# This is the current right most digit
	sum += r			# Add that into the sum
	val /= 10			# Then we truncate the right most digit for a new one
	val = int(val)
	
print (sum)