t = int(input())
for _ in range(t):
    x,y,n = map(int,input().split())
    num = n % x
    non = (y-num)
    if non > 0:
        print(n + non - x)
    else:
        print(n + non)