import sys

input = sys.stdin.readline

t = int(input())
out = []
for _ in range(t):
    x,y = map(int,input().split())
    if x == 0 or y == 0:
        out.append(1)
    elif x < y :
        out.append(2)
    elif x > y and (x-1) > y and y > 1:
        out.append(3)
    else:
        out.append(-1)
print("\n".join(map(str,out)))
