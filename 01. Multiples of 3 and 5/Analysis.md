# Multiples of 3 and 5: Analysis

The original attempt is m35.py and the second attempt is re_m35.py.
This document contains an analysis of the different approaches used in each of the files and the timing results for each.

## Approach Analysis

### First attempt (m35.py)
* A function was written to append all the multiples of a number from 1 up to a stopping value. 
* If the list already contains the multiple that is being considered, it will not append the same value again.
* In the main function, the function was called twice to first append all the multiples of 3 and then all the multiples of 5.
* Then another function is used to get the sum of all the elements in the list.

## Timing Analysis

File | Time (seconds)
--- | ---
m35.py | 0.0017 
re_m35.py | 0.00017

The second attempt (re_m35.py) is about a factor of 10 faster than the original attempt, coming in at 0.00017 seconds. 
