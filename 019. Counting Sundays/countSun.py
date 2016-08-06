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
	
def listDaysInYear ( year, leap_years ):
	# September, April, June and November has 30 days
	# All the rest has 31 except February which has 28 (except on leap years, 29)
	if year in leap_years:
		list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		return list
	else:
		list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		return list

def main ():
	start_year = 1901
	end_year = 2000
	
	# Make a list of all the leap years from start ~ end years inclusive
	leap_years = listLeapYear (start_year, end_year + 1)
	
	cur_day = 2				# Jan 1 1901 is a Tuesday
	sunday_the_first = 0 	# Counter of sundays that were also the first of month
	
	# Iterate through the years from starting year to ending year
	for year in range (start_year, end_year + 1):
		# Make a list of the days of the year of interest
		list_days = listDaysInYear (year, leap_years) 
		
		# Iterate through the months of the year one day at a time
		# If it's the first of a month and it's sunday, increment the counter
		for month in range (0, len(list_days)):
			day_in_month = 1
			while day_in_month <= list_days [month]:
				if (cur_day == 0 and day_in_month == 1):
					sunday_the_first += 1
				cur_day = ( cur_day + 1 ) % 7
				day_in_month += 1
	
	# Print out the number of sundays that coincided the first of a month
	print (sunday_the_first)	

main()