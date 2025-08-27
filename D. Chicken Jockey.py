import sys
input = sys.stdin.readline

t = int(input())
out = []
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    dp = [0] * (n + 1)
    dp[1] = lst[0]
    for i in range(2, n + 1):
        # print("before",dp)
        dp[i] = min(dp[i - 1] + lst[i - 1] - 1, lst[i - 2] + dp[i - 2] + max(0, lst[i - 1] - (i - 1)))
        # print("after",dp)
 
    out.append(dp[-1])

print("\n".join(map(str,out)))
