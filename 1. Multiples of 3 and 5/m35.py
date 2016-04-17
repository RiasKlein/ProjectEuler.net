#################################################################################
#																				
#	m35.py 																		
#																				
#	Project Euler (projecteuler.net) Problem 1 									
#	Multiples of 3 and 5 														
# 																				
#	If we list all the natural numbers below 10 that are multiples of 3 or 		
#	5, we get 3, 5, 6, and 9. The sum of these multiples is 23. 				
#																				
#	Find the sum of all the multiples of 3 or 5 below 1000. 	
#	ANS: 233168				
#																				
#	Program written by: Shunman Tse 											
#																				
#################################################################################

# Global variable
max_value = 1000	# Value to stop at 

# Append Multiples
#	Function adds all multiples of 'number' up until 'max_value' into 'list'
#	If a value is already in the list it is not appended again
def append_multiples ( number, max_value, list ):
	cur_mult = 1 	# The current multiplier for number
	cur_val = number * cur_mult

	while (cur_val < max_value):
		if cur_val not in list:
			list.append (cur_val)

		cur_mult += 1
		cur_val = number * cur_mult

	return list

# sum_list
#	Function adds all the numbers in the list and returns the sum
def sum_list ( list ):
	sum = 0
	for num in list:
		sum += int (num)
	return sum

# main
#	Function appends multiples of 3 & 5 into list, stopping at max_value
#	Repeats are skipped. Then the sum is computed and the result is printed
def main ():
	list = []
	list = append_multiples (3, max_value, list)
	list = append_multiples (5, max_value, list)
	sum = sum_list (list)

	print ("The sum of all multiples of 3 or 5 below " + str(max_value) + " is: " + str(sum))

main()


