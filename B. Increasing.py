t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    x = [x for x in lst if lst.count(x) > 1]
    if len(x) == 0:
        print("YES")
    else:
        print("NO")