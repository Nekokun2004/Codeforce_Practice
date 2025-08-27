MAX_A = 100005

n = int(input())

freq = [0] * MAX_A
for x in map(int, input().split()):
    freq[x] += 1

dp = [-1] * (MAX_A + 1)

dp[MAX_A] = 0
dp[MAX_A - 1] = freq[MAX_A - 1] * (MAX_A - 1)

for x in range(MAX_A - 2, 0, -1):
    skip = dp[x + 1]
    choose = x * freq[x] + dp[x + 2]
    dp[x] = max(skip, choose)

print(dp[1])