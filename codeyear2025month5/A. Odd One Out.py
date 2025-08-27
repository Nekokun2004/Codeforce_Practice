t = int(input())
for _ in range(t):
    lst = list(map(int,input().split()))
    x = [x for x in lst if lst.count(x) == 1]
    x = int("".join(map(str,x)))
    print(x)