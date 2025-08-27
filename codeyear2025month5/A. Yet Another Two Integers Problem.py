t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    count = 0
    if a == b:
        count = 0
    elif a > b :
        c = a - b
        # print("c = ",c)
        count += c // 10
        # print("count = ",count)
        if c % 10 != 0:
            count += 1
    elif a < b:
        c = b - a
        # print("c = ",c)
        count += c // 10
        # print("count = ",count)
        if c % 10 != 0:
            count += 1
    print(count)
