import sys

input = sys.stdin.readline

t = int(input())
out = []
for _ in range(t):
    n = int(input())
    lsta = list(map(int,input().split()))
    x = [x for x in lsta if lsta.count(x)>1]
    if len(x) > 0:
        out.append("YES")
    else:
        out.append("NO")
print("\n".join(out))