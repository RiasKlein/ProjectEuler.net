#################################################################################
#
#	anum.py
#
#	Project Euler (projecteuler.net) Problem 21
#	Amicable numbers
#
#	Let d(n) be defined as the sum of proper divisors of n (numbers less than n
#	which divide evenly into n). If d(a) = b and d(b) = a and a =/= b, then
#	a and b are an amicable pair and each of a and b are called amicable numbers.
#	Evaluate the sum of all amicable numbers under 1000.
#
#	Program by: Shunman Tse
#
#################################################################################

# listDivisors
#	Function returns all divisors of n in a list
def listDivisors (n):
	list = []
	
	for x in range (1, n):
		if n % x == 0:
			list.append(x)
	
	#print (sorted(list))
	return list
	
# sumList
#	Function returns the sum of all elements of a list
def sumList (list):
	sum = 0
	for element in list:
		sum += element
	return sum
	
def main():	
	amicable_numbers = []
	
	# Iterating from 1 ~ 10000
	for x in range (1, 10000):
		# Only consider a number if we haven't confirmed that it's an amicable number
		if x not in amicable_numbers:
			# Solve for d(a) and d(b)
			d_x = sumList (listDivisors (x))
			d_y = sumList (listDivisors (d_x))
			
			# Make sure that d(a) does not equal d(b) before appending to list
			if d_y == x and d_y != d_x:
				amicable_numbers.append (x)
				amicable_numbers.append (d_x)
	
	#print (amicable_numbers)
	
	# Get the sum of the amicable numbers and print it out
	sum_amicable_numbers = sumList (amicable_numbers)
	print (sum_amicable_numbers)
	
main()


	






