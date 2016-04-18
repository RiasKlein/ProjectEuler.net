#################################################################################
#
#	sumSquareDiff.py
#
#	Project Euler (projecteuler.net) Problem 6
#	Sum Square Difference
#
#	The sum of the squares of the first 10 natural numbers is:
#		1^2 + 2^2 + ... + 10^2 = 385
#	The square of the sum of the first 10 natural numbers is:
#		(1 + 2 + ... + 10)^2 = 55^2 = 3025
#	The difference is: 3025 - 385 = 2640
#
#	Find the difference between the sum of the squares of the first 100 
#	natural numbers and the square of the sum.
#	ANS: 25164150
#
#	Program by: Shunman Tse
#
#################################################################################

# sumOfSquares
# 	Function returns the sum of the squares of the first n natural numbers
def sumOfSquares (n):
	sum = 0 
	for num in range (1, n+1):
		sum += (num * num)
	return sum
	
# squareOfSum
# 	Function returns the square of the sum of the first n natural numbers
def squareOfSum (n):
	sum = 0
	for num in range (1, n+1):
		sum += num
	return sum * sum
	
def main():
	square_of_sum = squareOfSum (100)
	sum_of_square = sumOfSquares (100)
	print ("The difference is: " + str (square_of_sum - sum_of_square)) 
	
main()
	
