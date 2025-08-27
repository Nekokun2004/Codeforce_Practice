import sys

input = sys.stdin.readline

t = int(input())
out = []
for _ in range(t):
    n = int(input())
    lst = list(input())
    positionB = [x for x in range(n) if lst[x] == 'B']
    out.append(positionB[-1] - positionB[0] + 1)
print("\n".join(map(str,out)))