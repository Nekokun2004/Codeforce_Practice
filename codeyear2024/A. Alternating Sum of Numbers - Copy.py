t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    count = 0
    for j in range(len(a)) :
        if j % 2 == 0:
            count += a[j]
        else:
            count -= a[j]
    print(count)
