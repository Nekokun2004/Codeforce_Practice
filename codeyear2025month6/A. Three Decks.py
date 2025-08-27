t = int(input())
for _ in range(t):
    a,b,c = map(int,input().split())
    average = ( a+b+c ) // 3
    Remaining = c - average
    if a > average or b > average:
        print("NO")
    else:
        a_re = average - a
        b_re = average - b
        if Remaining == a_re+b_re:
            print("YES")
        else:
            print("NO")
    # print(average)