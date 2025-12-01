import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    
    if any(a[i] > a[i+1] for i in range(n-1)):
        print(0)
        continue

    
    if len(set(a)) < n:
        print(1)
        continue

    
    ans = 10**18
    for i in range(n-1):
        d = a[i+1] - a[i]   
        k = d//2 + 1
        ans = min(ans, k)

    print(ans)
