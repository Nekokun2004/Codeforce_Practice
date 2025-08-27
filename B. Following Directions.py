import sys

input = sys.stdin.readline

t = int(input())
out = []
for _ in range(t):
    countx = 0
    county = 0
    answer = True
    n = int(input())
    lst = list(input())
    for i in range(n):
        if lst[i] == 'U':
            county += 1
        elif lst[i] == 'R':
            countx += 1
        elif lst[i] == 'D':
            county -= 1
        elif lst[i] == 'L':
            countx -= 1
        if county == 1 and countx == 1:
            answer = False
            break
    if answer :
        out.append("NO")
    else:
        out.append("YES")
print("\n".join(out))