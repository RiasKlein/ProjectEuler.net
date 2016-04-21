#################################################################################
#
#	countSun.py
#
#	Project Euler (projecteuler.net) Problem 19
#	Counting Sundays
#
#	You are given the following information, but you may prefer to do some research for yourself.
#	1 Jan 1900 was a Monday.
#	Thirty days has September, April, June and November.
#	All the rest have thirty-one,
#	Saving February alone, which has twenty-eight, rain or shine. And on leap years, twenty-nine.
#	
#	A leap year occurs on any year evenly divisible by 4, but not on a century 
#	unless it is divisible by 400.
#	
#	How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#
#	Program by: Shunman Tse
#
#################################################################################

# isLeapYear
#	Function returns whether the provided year is a leap year or not
def isLeapYear ( year ):
	leap_year = False

	# If the year is evenly divisible by 4, it is a leap year
	if year % 4 == 0:
		leap_year = True
	# Unless it is a century, only centuries that are divisble by 400 are leap years
	if year % 100 == 0 and year % 400 != 0:
		leap_year = False

	return leap_year

# listLeapYear
#	Function returns a list of the leap years between the start and end parameters (inclusive)
def listLeapYear ( start, end ):
	leap_years = []
	for year in range (start, end + 1):
		if isLeapYear (year):
			leap_years.append (year)
	return leap_years

def main ():
	leap_years = listLeapYear (1901, 2001)
	print (leap_years)

main()