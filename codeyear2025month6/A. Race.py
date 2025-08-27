t = int(input())
for _ in range(t):
    a,x,y = map(int,input().split())
    Bob = (x + y) // 2
    count = abs(Bob - x) + abs(Bob - y)
    count1 = abs(a - x) + abs(a - y)
    # print("count = ",count)
    # print("count1 = ",count1)

    if count < count1 :
        print("YES")
    else:
        print("NO")
