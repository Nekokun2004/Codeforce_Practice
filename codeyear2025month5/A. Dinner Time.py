t = int(input())
for _ in range(t):
    n, m, p, q = map(int, input().split())
    if n > 0 and p == 1 and m == 1 and q == 1 or p % 2 == 0:
        print("YES")
    elif p > n // 2:
        print("NO")
    else:
        print("NO")
        
