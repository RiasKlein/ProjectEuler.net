#################################################################################
#
#	fib1000.py
#
#	Project Euler (projecteuler.net) Problem 25
#	1000-digit Fibonacci number
#
#	The 12th term of the fibonacci sequence is the first term to contain 3 digits
#	What is the index of the first term to contain 1000 digits?
#
#	Program by: Shunman Tse
#
#################################################################################

# fibDigits
#	Function continually generates fibonacci numbers until we get a fib number
#	with the specified number of digits
def fibDigits (n):
	fib = [1, 1]		# Numbers at index 1 & 2 in Fib sequence
	num_digits = 1		# Fib sequence starts with single digit numbers
	right_index = 2		# We start at 2 because default fib[1] contains index 2
	
	# Keep loop going until we have the specified number of digits
	while num_digits < n:
		# Generate the next fib number
		fib_next = fib[0] + fib[1]
		
		# Update the fibonacci number "window"
		fib[0] = fib[1]
		fib[1] = fib_next
		
		# Update the counter variables
		right_index += 1
		num_digits = len(str (fib_next))
		
	# Output the result
	print (right_index)

# main
#	Call fibDigits to complete the problem
def main():
	fibDigits (1000)
	
main()