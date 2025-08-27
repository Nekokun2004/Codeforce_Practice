n,m = map(int,input().split())
count = n
while n >= m:
    num = n // m
    count += num
    num1 = n % m
    num1 += num
    n = num1


print(count)