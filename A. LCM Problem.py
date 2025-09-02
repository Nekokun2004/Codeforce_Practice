import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    l,r = map(int,input().split())
    if l * 2 > r:
        print(-1,-1)
        continue
    print(l,l*2)