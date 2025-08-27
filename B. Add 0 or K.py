import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    lst = list(map(int,input().split()))
    for i in range(n):
        lst[i] += (lst[i] % (k+1)) * k
    print(*lst)