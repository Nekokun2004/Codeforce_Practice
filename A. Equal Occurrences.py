import sys
from collections import Counter

input = sys.stdin.readline

t = int(input())
out = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    freq = list(Counter(arr).values())
    ans = 0
    maxf = max(freq)
    for k in range(1, maxf + 1):
        cnt = sum(1 for f in freq if f >= k)   
        ans = max(ans, cnt * k)

    out.append(ans)
print("\n".join(map(str,out)))
