n,k = map(int,input().split())
index = 0
while index < k:
    if n % 10 == 0:
        n = n // 10
    else:
       n -= 1
    index += 1
print(n)