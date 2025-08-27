import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if a[-1] != b[-1]:
        print("NO")
        continue

    ok = True
    for i in range(n-2, -1, -1):
        if b[i] == a[i] or (a[i] ^ a[i+1]) == b[i] or (a[i] ^ b[i+1]) == b[i]:
            continue
        ok = False
        break

    print("YES" if ok else "NO")
