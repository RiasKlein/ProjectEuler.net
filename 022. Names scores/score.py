#################################################################################
#
#	score.py
#
#	Project Euler (projecteuler.net) Problem 22
#	Names scores
#
#	Sort the provided list of names into alphabetical order. Then work out the
#	alphabetical value of each name, multiply this value by its alphabetical 
#	position in the list to obtain a name score.
#	
#	For example, when the list is sorted, COLIN is worth:
#		3 + 15 + 12 + 9 + 14 = 53
#	It's position is 938 and so the score is: 938 * 53
#
#	What is the total of all the name scores in the file?
#
#	Program by: Shunman Tse
#
#################################################################################

# readNames
#	Function will read the contents of the provided names file and 
#	Return a list of all the names 
def readNames( filename ):
	rfile = open ( filename, 'r')
	
	line = rfile.readline()		# Read a line from the names file
		
	line = line.split(',')		# Use , as the delimiter and split the line
		
	# Iterate through the list and get rid of all the quotation marks
	for x in range (0, len(line)):
		element = line[x]
		element = element.strip ('"')
		element = element.strip ('"')
		line[x] = element
		
	# Now we sort the list
	line = sorted (line)
	
	rfile.close() 	# Close the file now that we are done
	
	# Return the list
	return (line)

# getAlphaValue
#	Function calculates and returns the alphabetical value of a name
#	Note: A has a value of 1, B = 2, C = 3, etc.	
def getAlphaValue ( name ):
	sum = 0
	
	# Note: 'a' has an ord of 97, 'b' has 98, and etc.
	# This applies for the lowercase version of the letter, that is why 
	#	we must turn the letter to lowercase before getting the value
	for letter in name:
		sum += (ord(letter.lower()) - 96)
	
	# return the alphabetical value of the name
	return sum

def main():
	names_list = readNames ('p022_names.txt')
	
	# By this point we have a sorted list of the names
	# We can now calculate the score of the list
	
	total_score = 0
	
	for x in range (0, len(names_list)):
		current_name = names_list[x]			# get the current name
		score = getAlphaValue (current_name)	# get the alphabetical value
		score *= (x+1)							# get the name score
		total_score += score					# update the total score
		
	# The reason score is multiplied by 'x+1' is because the 
	# alphabetical position of the name is equal to the index + 1
	# Consider the first name and have it has an index of 0

	print (total_score)
	
main()