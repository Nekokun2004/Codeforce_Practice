import math

def count_divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 1 
            if i != n // i:
                count += 1  
    return count

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def is_t_prime(x):
    root = math.sqrt(x)
    if not root.is_integer():
        return False
    return is_prime(int(root))


def answer(n):
    total = count_divisors(n)
    # print("is_t_prime = ",is_t_prime)
    # print("numbersqrt = ",math.sqrt(n))
    # print("sqrt = ",is_prime(math.sqrt(n)))
    # print("total = ",is_prime(total))
    if is_t_prime(n) and is_prime(total):
        return "YES"
    else:
        return "NO"

t = int(input())
n = list(map(int,input().split()))
for i in range(len(n)):
   print(answer(n[i]))


# import math

# def is_prime(x):
#     if x < 2:
#         return False
#     for i in range(2, int(math.sqrt(x)) + 1):
#         if x % i == 0:
#             return False
#     return True

# def is_t_prime(x):
#     root = math.sqrt(x)
#     if not root.is_integer():
#         return False
#     return is_prime(int(root))

# def answer(n):
#     return "YES" if is_t_prime(n) else "NO"

# t = int(input().strip())
# nums = list(map(int, input().split()))
# for n in nums:
#     print(answer(n))
