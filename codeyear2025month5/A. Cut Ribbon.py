n, a, b, c = map(int, input().split())
dp = [-float('inf')] * (n + 1)
dp[0] = 0  
for i in range(1, n + 1):
    print("dp zero = ",dp)
    if i >= a:
        dp[i] = max(dp[i], dp[i - a] + 1)
    if i >= b:
        dp[i] = max(dp[i], dp[i - b] + 1)
    if i >= c:
        dp[i] = max(dp[i], dp[i - c] + 1)
    print("dp = ",dp[i])

print(dp[n])


# lst = list(map(int,input().split()))
# lengths = lst[0]
# # print(lst)
# lst[1:] = sorted(lst[1:])
# # minlst = min(lst[1:])
# # print(lengths//minlst)
# count = 0
# index = 0
# if sum(lst[1:]) >= lengths:
#     for i in lst[1:]:
#             count += i
#             index += 1
#             if count > lengths :
#                 index -= 1
#     print(index)
# else:
#     print(lengths)
