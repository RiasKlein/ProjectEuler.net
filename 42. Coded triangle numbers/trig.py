#################################################################################
#
#	trig.py
#
#	Project Euler (projecteuler.net) Problem 42
#	Coded triangle numbers
#
#	
#
#################################################################################

word_filename = 'p042_words.txt'

def getWordValue ( word ):
	value = 0
	word = word.lower()
	
	for letter in word:
		value += (ord (letter) - 96)

	return value

def genTrigNum ( amount ):
	list = []

	for n in range ( amount ):
		t = n * (n + 1) / 2
		list.append (t)

	return list

def main():
	trig_list = genTrigNum ( 10000 )
	count_of_trig_num = 0

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

	rfile.close()

main()

