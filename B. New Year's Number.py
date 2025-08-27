t = int(input())
for _ in range(t):
    n = int(input())
    num = n // 2020
    modu = n % 2020
    if modu > num :
        print("NO")
    else:
        print("YES")