#################################################################################
#
#	smallMult.py
#
#	Project Euler (projecteuler.net) Problem 5
#	Smallest Multiple
#
#	2520 is the smallest number that can be divided by each of the numbers 
#	from 1 to 10 without any remainder.
#
#	What is the smallest positive number that is evenly divisible by all of 
#	the numbers from 1 to 20?
#	ANS: 232792560
#
#	Program by: Shunman Tse
#
#################################################################################

max_value = 20

# primeFactors
#	Returns prime factors of n in a list
def primeFactors ( n ):
    factors = []
    num = 2
    while n > 1:
        while n % num == 0:
            factors.append ( num )
            n /= num
        num = num + 1
    return factors
	
# listMultiply
#	Returns the product of all elements in list
def listMultiply ( list ):
	product = 1
	for num in list:
		product *= num
	return product

def main():	
	# Make list to hold factors for our smallest multiple
	smallest_list = []

	# Get the least number of each factor that we need into smallest_list
	for x in range (2, max_value + 1):
		factorx = primeFactors (x)
		for factor in factorx:
			num = factorx.count(factor)
			while smallest_list.count(factor) < num:
				smallest_list.append(factor)
	
	# Print out the smallest multiple 
	print (listMultiply(smallest_list))
	
main()


	






