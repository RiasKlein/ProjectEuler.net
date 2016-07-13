#################################################################################
#
#	trig.py
#
#	Project Euler (projecteuler.net) Problem 42
#	Coded triangle numbers
#
#	The nth term of the sequence of triangle numbers is given by:
#		t_n = 1/2 * n * (n+1)
#	so the first ten triangle numbers are:
#		1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
#	By converting each letter in a word to a number corresponding to its 
#	alphabetical position and adding these values we form a word value. 
#	For example, the word value for SKY is:
#		19 + 11 + 25 = 55 = t_10
#	If the word value is a triangle number then we shall call the word a 
#	triangle word.
#
#	How many words in the accompanying file are triangle words?
#
#	Program by Shunman Tse	
#
#################################################################################

word_filename = 'p042_words.txt'

# getWordValue
#	Calculates the word value for a parameter string (word)
def getWordValue ( word ):
	value = 0
	word = word.lower()
	
	for letter in word:
		value += (ord (letter) - 96)

	return value

# genTrigNum
#	Returns list with parameter amount triangle numbers
def genTrigNum ( amount ):
	list = []

	for n in range ( amount ):
		t = n * (n + 1) / 2
		list.append (t)

	return list

def main():
	# Initialization of necessary variables
	trig_list = genTrigNum ( 10000 )
	count_of_trig_num = 0

	# Retrieve the word list
	rfile = open (word_filename, 'r')
	line = rfile.readline()

	# Create an array of words out of the word list
	words = line.split(',')
	for word in words:
		# Strip the starting and ending quotation marks
		word = word[1:-1]
			
		# Get the value of the word
		value = getWordValue (word)

		# Check if the value of the word is a triangle number
		if value in trig_list:
			count_of_trig_num += 1

	# Output the number of triangle numbers we found
	print (count_of_trig_num)

	# Cleanup
	rfile.close()

main()

