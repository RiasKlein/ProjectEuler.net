#################################################################################
#
#	spiral.py
#
#	Project Euler (projecteuler.net) Problem 28
#	Number spiral diagonals
#
#	Starting with the number 1 and moving to the right in a clockwise direction 
#	a 5 by 5 spiral is formed as follows:
#		21 22 23 24 25
#		20  7  8  9 10
#		19  6  1  2 11
#		18  5  4  3 12
#		17 16 15 14 13
#	It can be verified that the sum of the numbers on the diagonals is 101.
#	What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
#	formed in the same way?
#
#	Program by: Shunman Tse
#
#################################################################################

"""
For this problem, notice that the diagonal values are:
	1, (3, 5, 7, 9), (13, 17, 21, 25)
For the first tuple of (3, 5, 7, 9), each corner value is off by 2
In the second tuple (13, 17, 21, 25), each corner value is off by 4
This actually continues and in the third tuple, each corner is off by 6

Now that we can generate the tuples, great, but how many are we making?
The size of the diagonal increases by 2 for every tuple we generate.
Let's use this knowledge to help us finish this...
"""

# main
def main():
	STOP_corner = 1001
	
	sum = 1
	corner = 1
	counter = 1
	
	# Keep generating layers until we should stop
	while (corner < STOP_corner):
		# Add the 4 corner values into sum 
		for x in range (0, 4):
			counter += (corner + 1)
			sum += counter
		
		# Increment corner for the next layer
		corner += 2
	
	print (sum)
	
	
main()