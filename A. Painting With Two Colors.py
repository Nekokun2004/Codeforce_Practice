import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,a,b = map(int,input().split())
    if (b % 2) != (n %2):
        print("NO")
    elif (a % 2) != (n % 2) and a > b:
        print("NO")
    else:
        print("YES")