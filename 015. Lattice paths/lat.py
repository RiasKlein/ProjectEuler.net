#################################################################################
#
#	lat.py
#
#	Project Euler (projecteuler.net) Problem 15
#	Lattice paths
#
#	Starting from the top left corner of a 2x2 grid, and only being able to move 
#	to the right and down, there are exactly 6 routes to the bottom right corner.
#	How many such routes are there through a 20 x 20 grid?
#	ANS: 137846528820
#
#	Program by: Shunman Tse
#
#################################################################################

# countRoutes
#	Function calculates the number of routes to get from the top left
#	to the bottom right of a square grid of size 'size'
def countRoutes ( size ):
	m = [1] * size
	
	for i in range (0, size):
		for j in range (0, i):
			m[j] = m[j] + m[j - 1]
		m[i] = 2 * m[i - 1]
	
	len = m[size - 1]
	return len
	
print ( countRoutes (20) )