from itertools import groupby
import sys

input = sys.stdin.readline

t = int(input())
out = []
for _ in range(t):
    count = 0
    n = int(input())
    lstx = [''.join(g) for _,g in groupby(input().strip())]
    # print(lstx)
    found = any("..." in s for s in lstx)
    if found:
        # print(2)
        out.append(2)
    else:
        dot_count = sum(s.count('.') for s in lstx)
        out.append(dot_count)
        # print(dot_count)
print("\n".join(map(str,out)))