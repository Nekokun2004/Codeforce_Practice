t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    if k % (n-1) == 0:
        count = n - 1
    else:
        count = k % (n-1)
    num = -(-k//(n-1))-1    
    # print("num =",num)
    print(n*num + count)