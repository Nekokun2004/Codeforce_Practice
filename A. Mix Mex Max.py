t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = {x for x in a if x != -1}
    if len(s) >= 2:
        print("NO")
    elif len(s) == 0:
        print("YES")
    else:
        v = s.pop()
        print("YES" if v != 0 else "NO")
