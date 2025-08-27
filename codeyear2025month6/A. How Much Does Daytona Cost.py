t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    if k in lst:
        print("YES")
    else:
        print("NO")
