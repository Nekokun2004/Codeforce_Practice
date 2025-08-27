import sys


input = sys.stdin.readline

n,m = map(int,input().split())
if n >= m:
    for i in range(-(-n//2),n+1):
        if i % m == 0:
            print(i)
            break
else:
    print(-1)