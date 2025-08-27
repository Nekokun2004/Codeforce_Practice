n = int(input())
for _ in range(n):
    x,y = [int(x) for x in input().split()]
    s = x*y
    p = x*(x+1)//2
    if s > p :
        print(s)
    else:
        print(p)
