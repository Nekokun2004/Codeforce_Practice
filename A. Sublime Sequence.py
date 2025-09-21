import sys

input = sys.stdin.readline

t = int(input())
out = []
for _ in range(t):
    x,n = map(int,input().split())
    if n % 2 == 0:
        out.append(0)
    else:
        out.append(x)
print("\n".join(map(str,out)))