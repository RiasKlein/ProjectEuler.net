#################################################################################
#
#	spec.py
#
#	Project Euler (projecteuler.net) Problem 9
#	Special Pythagorean triplet
#
#	A Pythagorean triplet is a set of three natural numbers, a < b < c, for which
#		a^2 + b^2 = c^2
#	There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#	Find the product abc.
#	ANS: 31875000
#
#	Program by: Shunman Tse
#
#################################################################################

# genTriplet
#	Function finds a pythagorean triplet such that a + b + c = sum
#	The triplet is returned as a list
def genTriplet ( sum ):
	triplet = []
	
	# Using two positive integers such that m < n:
	#	Our triples are: 	a = n^2 - m^2
	#						b = 2 * n * m 
	#						c = n^2 + m^2
	for m in range (0, sum):
		for n in range (0, sum):
			if m < n:
				a = (n * n) - (m * m)
				b = 2 * n * m 
				c = (n * n) + (m * m)
				if (a + b + c == sum):
					triplet.append(a)
					triplet.append(b)
					triplet.append(c)
					break
	
	return triplet
	
def main():
	# Find the triplets that sum to 1000
	list = genTriplet (1000)
	
	# Find the product of the triplets
	product = 1
	for num in list:
		product *= num
	
	print (product)
	
main()