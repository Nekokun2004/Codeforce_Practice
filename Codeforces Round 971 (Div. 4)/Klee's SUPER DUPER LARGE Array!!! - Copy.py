t = int(input())
for i in range(t):
    n,k = int(input().split())
    a = n - k
    if a < 0:
        a = -a
    x = a