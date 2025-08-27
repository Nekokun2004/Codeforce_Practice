def solve():
    n, m, l, r = map(int, input().split())
    x = min(m, -l)  
    print(-x, m - x)  

t = int(input())
for _ in range(t):
    solve()
