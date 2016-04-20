#################################################################################
#
#	maxp.py
#
#	Project Euler (projecteuler.net) Problem 18
#	Maximum path sum I
#
#	By starting at the top of the triangle below and moving to adjacent numbers
#	on the row below, the maximum total from top to bottom is 23.
#	   3
#     7 4
#	 2 4 6
#	8 5 9 3
#	That is, 3 + 7 + 4 + 9 = 23.	
#	Find the maximum total from top to bottom of the triangle below...
#
#	Program by: Shunman Tse
#
#################################################################################

"""
While brute force and testing every single path can work with a problem of the 
provided scale in problem 18, it will not work nicely for somethinng on an 
even greater scale...

So, let's consider the example triangle on a smaller scale...
 3
7 4
Let's say that we just have the following triangle, what would the solution be?
Well, we can start from the lowest level and see that [3, 7] is the best choice.
The alternative would have been [3, 4] which would be smaller.

Now, let's build up another level...
  3
 7 4
2 4 6
Once again starting from the lowest level, we can see that we have the paths:
2, 7 -> 9
4, 7 -> 11
If we're at 7 we have a choice between 2 and 4 which would give us a total of 9 
or 11. Since 11 > 9, the desired path is [7, 4]
4, 4 -> 8
6, 4 -> 10
If we're at 4, we have a choice between 4 and 6 which gives us a total of 8 or 10.
Since 10 > 8, the desired path is [4, 6]

Note that we are not trying to find the path with the max number, but rather the 
maximum number itself. We can just remove the last row and just consider from the 
second row and up with the new path values. So we have:
  3
11 10 
From this point it is easy enough to see that the best choice is [3, 11]
We get that the max path in the triangle is 14 and the path is [3, 7, 4]

Even if the number of rows were to increase, the same idea will work.
"""

# To use different triangles, just copy them into the string space in triangle
triangle = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
""".split ('\n')

# Remove the empty entries in the front and the back of the grid
triangle.remove ('')
triangle.remove ('')

# mergeRow 
#	Function merges the row at the provided index with the following row
def mergeRow ( list_triangle, row_index ):
	row_to_mod = list_triangle [ row_index ]
	row_following = list_triangle [ row_index + 1 ]
	
	# We want to change the elements in row_to_mod such that each index
	# will combine with the maximum of the number at index or index +1 in row_following
	# That is, if we have the following lists:
	#	row_to_mod = [7, 4]
	#	row_following = [2, 4, 6]
	# 7 can interact with [2, 4] and should be changed to 7 + 4 = 11
	# 4 can interact with [4, 6] and should be changed to 4 + 6 = 10
	
	# Iterate through the entirety of row_to_mod
	for index in range (0, len(row_to_mod)):
		t1 = row_to_mod [ index ] + row_following [ index ]
		t2 = row_to_mod [ index ] + row_following [ index + 1 ]
		row_to_mod [ index ] = max (t1, t2)
	
	#print (row_to_mod)
		
def main():
	# list_triangle is a list that contains a list of numbers for each row in the original triangle
	list_triangle = []
	for line in triangle:
		str_list = ( line.split(' ') )
		str_list = [int(i) for i in str_list]
		list_triangle.append (str_list)
	
	size_of_triangle = len (list_triangle)
	
	# We will iterate backwards from the size_of_triangle - 2, until 0
	for x in range (size_of_triangle - 2, -1, -1):
		mergeRow ( list_triangle, x)
	
	# Now we just need to read the value at the root of the triangle for the desired max total
	print ( list_triangle [0][0] )
	
main()