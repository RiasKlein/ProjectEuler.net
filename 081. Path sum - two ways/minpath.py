#################################################################################
#
#	minpath.py
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
	# Read the text file for the data matrix
	data_matrix = readMatrix (filename)
	
	# Get the size of the data matrix
	data_matrix_size = len(data_matrix)

	# Cost matrix
	cost_matrix = [[[] for i in range(data_matrix_size)] for i in range (data_matrix_size)]
	
	for row in range (data_matrix_size):
		for col in range (data_matrix_size):
			if row == 0 and col == 0: 	# This is the top-left most tile, the cost is just itself
				cost_matrix[row][col] = data_matrix[row][col]
			elif row == 0 and col > 0:
				# This is the top row in which we just move to the right
				cost_matrix[row][col] = data_matrix[row][col] + cost_matrix[row][col-1]
			elif row > 0 and col == 0:
				# This is the left-most column in which we just move down
				cost_matrix[row][col] = data_matrix[row][col] + cost_matrix[row-1][col]
			else:
				# These are the inner tiles
				cost_matrix[row][col] = min ( (data_matrix[row][col] + cost_matrix[row][col-1]), (data_matrix[row][col] + cost_matrix[row-1][col]) )
					
	print (cost_matrix[ data_matrix_size-1 ][ data_matrix_size-1 ])

main()