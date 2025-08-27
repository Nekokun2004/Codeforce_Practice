import math
import sympy

def get_primes(limit):
    primes = [1]
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

n,m = map(int,input().split())
lst = get_primes(m)
if n == lst[-2] and m == lst[-1]:
    print("YES")
else:
    print("NO")
# lst = list(sympy.primerange(n,m+2))
