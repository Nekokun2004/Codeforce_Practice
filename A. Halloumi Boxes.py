t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if k == 1:
        print("YES" if a == sorted(a) else "NO")
    else:
        print("YES")
