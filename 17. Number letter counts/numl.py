#################################################################################
#
#	numl.py
#
#	Project Euler (projecteuler.net) Problem 17
#	Number letter counts
#
#	If the numbers 1 to 5 are written out in words:
#		one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
#	letters used in total.
#	If all the numbers from 1 to 1000 (inclusive) were written out in words,
#	how many letters would be used?
#
#	Program by: Shunman Tse
#
#################################################################################

# countTenOne
# 	Function takes in a number n and returns the number of letters that are 
#	in the word form of the tens and ones places of the number
def countTenOne ( n ):
	list_ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	list_teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
	list_tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
	ten_one = n % 100	# contains the tens and ones place of n

	if ten_one == 0:	# If we have 00 then we should count 0
		return 0
	if ten_one < 10:
		#print (list_ones [ten_one-1])
		return len ( str (list_ones [ten_one-1]) )
	if ten_one < 20:
		ones_place = ten_one % 10
		#print (list_teens [ones_place])
		return len ( str (list_teens [ones_place]) )
	if ten_one >= 20:
		sum = 0
		tens_place = ten_one / 10	# Consider the tens place
		#print (list_tens [tens_place-1])
		sum += len (str ( (list_tens [tens_place-1]) ) )
		ones_place = ten_one % 10	# Consider the ones place
		if ones_place > 0: 
			#print (list_ones [ones_place-1])
			sum += len (str (list_ones [ones_place-1]) )
		return sum

# countHundredThousand
#	Function takes in a number n and returns the num of letters that are 
#	in the word form of the hundreds place or return one thousand
#	So n is either in the hundreds or one thousand
def countHundredThousand ( n ):
	list_ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	str_hundred = 'hundred'
	str_thousand = 'onethousand'
	thousand_hundred = n / 100		# Contains the thousands and hundreds place of n
	
	if thousand_hundred == 0:
		return 0
	if thousand_hundred < 10:
		#print (list_ones [thousand_hundred-1])
		#print (str_hundred)
		sum = 0
		sum += len ( str (list_ones [thousand_hundred-1]) )
		sum += len (str_hundred)
		return sum
	else:
		return len (str_thousand)
		
# main
"""
Counting the hundreds and ones places can be done in a straight forward
manner, however, things get weird when we're dealing with the tens place.
Consider how 15 is called fifteen rather than say ten-five. So my approach
is to count in two groups [ thousand, hundreds ] and [ tens, ones ]
"""
def main():
	total_len = 0
	
	# We will consider all numbers n from 1 to 1000
	for n in range (1, 1001):
		# First we count the hundreds (or thousands) place of n
		total_len += countHundredThousand (n)
		
		# Consider the 'and' that shows up for numbers greater than 100
		if n > 100 and n != 1000:
			if n % 100 != 0:
				total_len += 3
		
		# Count the ones place of n
		total_len += countTenOne (n)
	
	# Output the total 
	print (total_len)
	
main()