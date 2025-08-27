import sys
from collections import Counter

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    lstS = [min(x%k,abs((x%k)-k)) for x in S]
    lstT = [min(x%k,abs((x%k)-k)) for x in T]
    lstS.sort()
    lstT.sort()
    if lstT == lstS:
        print("YES")
    else:
        print("NO")

