# Even Fibonacci Numbers

## Approach Analysis

In evenFib.py, the approach for solving the problem is:
* 1. Generate a list of Fibonacci numbers up to 4 million
* 2. Add up all of the even Fibonacci numbers in the list

## Possible Improvement

If we want to improve the speed of the solution, first let's consider where we are doing 
"wasteful" work in the current solution. In the current solution, we generate a complete list of Fibonacci
numbers up to 4 million and then iterate through the list in order to sum up all of the even values.

How about only incorporating the sum calculation with the generation of the Fibonacci numbers?
That is, as we generate each Fibonacci value (up to 4 million), if the new value is even, add it to a running total.
When we reach the stopping point of 4 million, we can just output the running total value.

## Future Plans

I plan to code the alternate solution and do a timing comparison between the two approaches (the current vs. the alternative)
to test whether the proposed improvement will make a faster program. 
