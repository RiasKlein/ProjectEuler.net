#################################################################################
#
#	cycle.py
#	Project Euler Problem 26
#	Reciprocal cycles
#
#	A unit fraction contains 1 in its numerator. The decimal representation of 
#	the unit fractions with denominators 2 to 10 are given:
#		1/2 = 0.5
#		1/3 = 0.(3)
#		1/4 = 0.25
#		1/5 = 0.2
#		1/6 = 0.1(6)
#		1/7 = 0.(142857)
#		1/8 = 0.125
#		1/9 = 0.(1)
#		1/10 = 0.1
#	where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
#	be seen that 1/7 has a 6-digit recurring cycle.
#
#	Find the value of d < 1000 for which 1/d contains the longest recurring
#	cycle in its decimal fraction part.
#
#	Program by Shunman Tse
#
#################################################################################

# Terminology: The repeating digit sequence of a number is called: repetend
# A helpful fact to know before we start is that a number 1/d has a repetend 
# 	with a length of at most d - 1. 
#	So 1/7 has a max repetend length of 7 - 1 = 6; which happens to be the case
#	That is, 1/7 has a repetend of 142857 which has a length of 6
# Now let's think about this in terms of long division

# Say we want to find the repetend of the number 1/d
#	First, we get the remainder of 1/d
#	Then, we multiply the remainder of 10 and divide that by d
#	We repeat this until we get a remainder that we've already seen
#	Once we get a repeated remainder, we look at the number of remainders we have
#	The number of remainders is the length of the repetend

def remainder_length ( number ):
	remainder_list = []
	remainder = 1
	while remainder not in remainder_list:

		# Max repetend length of a number is value of number - 1
		if len (remainder_list) == number - 1:
			break

		remainder_list.append(remainder)
		remainder *= 10
		remainder = remainder % number
	return len(remainder_list)

def main():
	longest_number = 2
	longest_repetend = 0

	for number in range (2, 1000):
		length = remainder_length (number)
		if length > longest_repetend:
			longest_repetend = length
			longest_number = number

	print ("Longest Repetend: " + str(longest_number))

main()
