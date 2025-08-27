t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    lst = list(map(int,input().split()))
    index = 0
    count = 0
    pre = [0] * (n+1)
    for i in range(n):
        pre[i+1] = pre[i] + lst[i]
    print(pre)
    while index + k <= n :
        if pre[index + k] - pre[index] == 0:
            index += k + 1
            count += 1
        else:
            index += 1
    print(count)
        