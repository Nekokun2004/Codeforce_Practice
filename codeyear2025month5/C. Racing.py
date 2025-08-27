import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    d = list(map(int, input().split()))
    obs = [tuple(map(int, input().split())) for _ in range(n)]
    low = [0]*(n+1)
    high = [0]*(n+1)
    low[0] = high[0] = 0

    ok = True
    for i in range(1, n+1):
        l_i, r_i = obs[i-1]
        if d[i-1] == 0:
            lo, hi = low[i-1], high[i-1]
        elif d[i-1] == 1:
            lo, hi = low[i-1]+1, high[i-1]+1
        else:  # -1
            lo, hi = low[i-1], high[i-1]+1

        low[i]  = max(lo, l_i)
        high[i] = min(hi, r_i)
        if low[i] > high[i]:
            ok = False
            break

    if not ok:
        print(-1)
        continue

    h = [0]*(n+1)
    h[n] = low[n]  
    for i in range(n, 0, -1):
        if d[i-1] == -1:
            if low[i-1] <= h[i] <= high[i-1]:
                d[i-1] = 0
            else:
                d[i-1] = 1
        h[i-1] = h[i] - d[i-1]
        if not (low[i-1] <= h[i-1] <= high[i-1]):
            ok = False
            break

    print(*d if ok else [-1])


# t = int(input())
# for _ in range(t):
#     n = int(input())
#     d = list(map(int,input().split()))
#     drone = 0
#     for i in range(n):
#         l,r = map(int,input().split())
#         if d[i] == 0:
#           pass
#         elif d[i] == -1:
#            if l <= drone and drone <= r and l == r:
#               d[i] = 0
#            elif l <= drone and drone <= r and l < r:
#               d[i] = 1
#               drone += 1
#         elif d[i] == 1:
#            drone += 1
#     if d.count(-1) == 0:
#        print(d)
#     else:
#        print(-1)
              
              
    