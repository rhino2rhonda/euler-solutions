# Problem 5 - Smallest multiple
# 520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# The following solution is based on factorising each number and collecting the max count of factors in a map

def get_smul(N):
    
    factors = {}

    for n in range(2, N+1):
        factors[n] = 0
        for f in range(2, n+1):
            count = 0
            while True:
                if n % f == 0:
                    count += 1
                    n /= f
                else:
                    break
            if count > 0:
                factors[f] = max(factors[f], count)

    mul = 1
    for f in factors:
        mul *= pow(f, factors[f])

    return mul

print get_smul(20)
 

