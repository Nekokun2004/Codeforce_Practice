t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    x1 = [x for x in lst if x % 2 == 1]
    x2 = [x for x in lst if x % 2 == 0]
    if len(x1) % 2 == 1:
        print("NO")
        # elif len(x2) % 2 == 1:
        #     print("NO")
    else:
        print("YES")
