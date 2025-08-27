t = int(input())
for i in range(t):
    c = 0
    a,b = [int(x) for x in input().split()]
    c = c-a+b-c
    print(c)
