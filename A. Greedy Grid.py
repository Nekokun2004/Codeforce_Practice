t = int(input())
for i in range(t):
    m,n = map(int,input().split())
    if n == 1 or m == 1:
        print("NO")
    elif n == 2 and m == 2:
        print("NO")
    else:
        print("YES")