#################################################################################
#
#	minpath_greedy.py
#
#	Project Euler (projecteuler.net) Problem 81
#	Path sum: two ways
#
#	In the 5x5 matrix below, the minimal path sum from the top left to the 
#	bottom right, by only moving to the right and down, is indicated in bold 
#	red and is equal to 2427.
#
#	[131]   673     234     103     18
#	[201]   [96]    [342]   965     150
#	630     803     [746]   [422]   111
#	537     699     497     [121]   956
#	805     732     524     [37]    [331]
#
#	Find the minimal path sum, in matrix.txt attached, from the 
#	top left to the bottom right by only moving right and down.
#
#	This program uses the greedy search method in order to get a local minimum.
#	It would appear that the local minimum is not the value we need...
#
#	Program by: Shunman Tse
#
#################################################################################

filename = 'p081_matrix.txt'
#filename = 'p081_example.txt'

def readMatrix (filename):
	matrix = []

	rfile = open (filename, 'r')

	while True:
		line = rfile.readline()
		if not line: 
			rfile.close()
			break

		line = line.strip('\n').split(',')

		for x in range (len(line)):
			line[x] = int(line[x])

		matrix.append(line)

	return matrix

def main():
	# Read the text file for the matrix
	matrix = readMatrix (filename)
	
	# Get the size of the matrix
	matrix_size = len(matrix)

	current_row = matrix_size - 1
	current_col = matrix_size - 1

	current_cost = 0
	
	while current_col != 0 or current_row != 0:
		print (matrix[current_row][current_col])
		current_cost += matrix[current_row][current_col]

		# From any given position, there are two directions to travel in
		# We can go up or move to the left

		up_value = -1
		left_value = -1

		# Consider moving up
		if current_col > 0:
			up_value = matrix[current_row][current_col - 1]

		# Consider moving to the left
		if current_row > 0:
			left_value = matrix[current_row-1][current_col]

		if up_value == -1:
			# Go left
			current_row -= 1
		elif left_value == -1:
			current_col -= 1
		else:
			if up_value < left_value:
				# Go up
				current_col -= 1
			else:
				current_row -= 1

	print (matrix[0][0])
	current_cost += matrix[0][0]
	print ('Total Cost: ' + str(current_cost))

main()