import sys


input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input().strip())
    length = len(str(n))          
    first_digit = int(str(n)[0])  
    count = (length - 1) * 9
    candidate = int(str(first_digit) * length)
    if candidate <= n:
        count += first_digit
    else:
        count += first_digit - 1

    print(count)