#################################################################################
#																				
#	re_m35.py 																		
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

import time

# Global variable
max_value = 1000	# Value to stop at 

# main
#	Function iterates from 
def main ():
	sum = 0

	# Iterate from 1 to the stopping point
	for x in range (1, max_value):
		# Only add the current value if it is a multiple of 3 or 5
		if (x % 3 == 0) or (x % 5 == 0):
			sum += x

	# Print the output
	print ("The sum of all multiples of 3 or 5 below " + str(max_value) + " is: " + str(sum))

time_start = time.time()
main()
print ("- %s seconds -" % (time.time() - time_start))


