t = int(input())
for _ in range(t):
    h,m = map(int,input().split())
    num = 23 - h
    num = num * 60
    num1 = 60 - m
    print(num+num1)