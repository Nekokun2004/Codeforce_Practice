t = int(input())
for _ in range(t):
    n = int(input())
    ans = []
    while n>=3:
        ans.append(-1)
        ans.append(3)
        n -= 2
    ans.append(-1)
    if n == 2:
        ans.append(2)
    print(*ans)
        
        # ans = []
        # for i in range(1, n + 1):
        #     if i % 2 == 1:  
        #         ans.append(-1)
        #     else:           
        #         ans.append(2 if (n % 2 == 0 and i == n) else 3)
        # print(*ans)
