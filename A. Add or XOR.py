t = int(input())
for _ in range(t):
    a,b,x,y = map(int,input().split())
    usea = bin(a)[2:]
    useb = bin(b)[2:]
    if a > b :
        if len(usea) != len(useb):
            print(-1)
        else:
            print(y)
    elif a == b:
        print(0)
    elif a < b:
        reslut = b - a
        answer2 = 0
        countx = 0
        county = 0
        if reslut % 2 == 1:
            countx += (-(-reslut//2))* x
        

        else:
            countx += (reslut // 2) * x
        county += (reslut // 2) * y
        answer1 = countx + county
        answer = min(reslut*x,answer1)
        print(answer)