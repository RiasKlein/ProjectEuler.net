# Multiples of 3 and 5: Analysis

The original attempt is m35.py and the second attempt is re_m35.py.
This document contains an analysis of the different approaches used in each of the files and the timing results for each.

## Approach Analysis

### First attempt (m35.py)
* A function appends all the multiples of a number from 1 up to a stopping value into a list. 
  - If the list already contains the multiple that is being considered, it will not append the same value again.
* In the main function, that function is called twice to first append all the multiples of 3 and then all the multiples of 5.
* Then another function is used to get the sum of all the elements in the list.
* Finally, the sum is printed out.

### Second attempt (re_m35.py)
* The program iterates from 1 up to the stopping value and adds up any value that is a multiple of 3 or 5.
* Then, the sum is printed out.

## Timing Analysis

File | Time (seconds)
--- | ---
m35.py | 0.0017 
re_m35.py | 0.00017

The second attempt (re_m35.py) is about a factor of 10 faster than the original attempt, coming in at 0.00017 seconds. 

The first attempt (m35.py):
* is a 2-pass solution for getting all the multiples of 3 or 5 into a list.
* requires another pass through the final list to get the sum of all the multiples of 3 or 5.

while the second attempt (re_m35.py):
* is a single-pass solution that acquires the final sum by counting from 1 to the stopping point once.
