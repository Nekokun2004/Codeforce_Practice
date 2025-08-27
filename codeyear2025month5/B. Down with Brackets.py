import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    bal = 0
    can_break = False
    for ch in s[:-1]:
        if ch == '(':
            bal += 1
        else:
            bal -= 1
        if bal == 0:
            can_break = True
            break

    print("YES" if can_break else "NO")
