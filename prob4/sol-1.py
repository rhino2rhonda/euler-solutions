# Problem 4 - Largest palindrome product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# This solution is based on brute force, stating from the largest 3 digit numbers to the smallest

def is_pal(x):
    x_mod = x
    rev = 0
    while x_mod > 0:
        rev *= 10
        rev += x_mod%10
        x_mod /= 10
    return x == rev

max_pal = -1
for x in xrange(999,99,-1):
    for y in xrange(999,99,-1):
        if is_pal(x*y):
            max_pal = max(max_pal, x*y)

print max_pal
