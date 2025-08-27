import sys
import math

input = sys.stdin.readline

t = int(input())
out = []
for _ in range(t):
    n = int(input())
    lst = map(int,input().split())
    sumlst = sum(lst)
    if math.sqrt(sumlst) == int(math.sqrt(sumlst)):
        out.append("YES")
    else:
        out.append("NO")
print("\n".join(out))
    