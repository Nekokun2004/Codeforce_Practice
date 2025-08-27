t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    maxvalues = 0
    count = 0
    for i in range(n):
        # print("lst[i] = ",lst[i])
        if lst[i] == 0:
            count += 1
            maxvalues = max(maxvalues,count)
        else:

            count = 0
        # print("count = ",count)
    print(maxvalues)
        