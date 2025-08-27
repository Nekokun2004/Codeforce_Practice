t = int(input())
for i in range(t):
    a,b = [int(x) for x in input().split()]
    x = -(-a // b)
    # print("x = ",x)
    if (x*b) == a:
        print(0)
    else:
        o = a-(x*b)
        print(abs(o))
    