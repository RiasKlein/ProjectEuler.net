#################################################################################
#
#	hd.py
#
#	Project Euler (projecteuler.net) Problem 12
#	Highly divisible triangular number
#
#	The sequence of triangle numbers is generated by adding the natural numbers.
#	The 7th number would be: 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
#	The number of factors that 28 has is 5.
#	What is the value of the first triangle number to have over five hundred divisors?
#	ANS: 76576500
#
#	Program by: Shunman Tse
#
#################################################################################

# countDivisors
#	Function returns the number of divisors that n has
def countDivisors ( n ):	
	div = 1
	count = 0
	
	while n % 2 == 0:
		count += 1
		n /= 2
	div = div * (count + 1)
	
	i = 3
	while n != 1:
		count = 0
		while n % i == 0:
			count += 1
			n /= i
		div = div * (count + 1)
		i += 2
	
	return div

def main():
	divisors = 1
	index = 2
	trig_num = 1

	# Keep getting more trig numbers and solving for the number of divisors
	# Stop when we have more than 500 divisors
	while (divisors < 500):
		trig_num += index
		index += 1
		divisors = countDivisors (trig_num)
		
	print (trig_num)
	
main()