from math import ceil
 
t = int(input())
 
for _ in range(t):
    n = int(input())
    money_P = [int(x) for x in input().split()]
 
    if n <= 2:
        print(-1)
        continue
 
    money_P.sort()
    a = money_P[n//2]
    x = 2*a*n - sum(money_P)
    if x%1 == 0:
        x = int(x+1)
    else:
        x = ceil(x)
 
    if x>=0: print(x)
    else: print(0)