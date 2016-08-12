################################################################################
#
#   quadratic.py
# 
#   Project Euler 27
#   Quadratic Primes
#
#   Considering quadratics of the form:
#       n^2 + an + b, where |a| < 1000 and |b| <= 1000
#   where |n| is the absolute value of n.
#
#   Find the product of the coefficients, a and b, for the quadratic expression 
#   that produces the maximum number of primes for consecutive values of n,
#   starting with n = 0.
#
#   Program made via pair programming by Shunman Tse & David Tan
#
################################################################################

def main():
    longest_chain = 0                   # Longest chain discovered so far
    product_lc = 0                      # Product of (a, b) from longest chain
    
    markers = prime_markers (1000000)   # Generate our prime markers

    # Test (a, b) pairs for the longest chain of n
    for a in range (-999, 1000):        # a goes from [-999, 1000)
        for b in range (2, 1001):       # b goes from [2, 1000] , optimization: b >= 2 for n = 0 case
            current_chain = 0           # chain length for the current (a, b) pair
            n = 0                       # Initialize n to 0
            
            # For the n^2 + an + b with n = 0 case, we see that b must be prime
            if markers[b] == True:
                # Find the chain length of primes for the current (a, b) pair
                while True:
                    val = n**2 + a * n + b
                    if val > 0 and markers[val]:
                        current_chain += 1
                        n += 1
                    else:
                        break
                        
                # If our current chain is longer than the longest chain, update it
                if current_chain > longest_chain:
                    longest_chain = current_chain
                    product_lc = a * b
    
    print (product_lc)

# prime_markers
#   Returns a list of boolean markers for whether a number is prime or not
# Assuming the returned list is named markers:
#   If you want to test whether 3 is prime, check whether markers[3] == True
def prime_markers ( n ):
    markers = [False] * n       # Boolean list of markers to be returned
    sieve = [True] * n
    for i in xrange(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) / (2 * i) + 1)
    
    # 2 is always a prime number, mark it as such
    markers[2] = True
    
    # Use the sieve to complete our prime markers
    for i in xrange (3, n, 2):
        if sieve[i]:
            markers[i] = True
    return markers
    
main()