import sys
import math
from sympy import isprime


def prime_number(n):
    lst = [1]
    for i in range(2,n+1):
        if isprime(i):
            lst.append(i)
    lst.sort()
    return lst


def generate_primes(n):
    prime_numbers = [1]
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
    return prime_numbers


for line in sys.stdin:
    line = int(line)
    # print(prime_number(line))
    print(generate_primes(line))