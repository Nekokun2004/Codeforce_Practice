t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    count1 = 0
    count2 = 0
    if n > 1:
        for i in range(n):
            if i % 2 == 0 and lst[i] % 2 == 0:
                continue
            elif i % 2 == 0 and lst[i] % 2 != 0: 
                count1 -= 1
            elif i % 2 != 0 and lst[i] % 2 != 0:
                continue
            elif i % 2 != 0 and lst[i] % 2 == 0: 
                count2 += 1
        if abs(count1) == count2:
            count = count2
        else:
            count = -1
    else:
        if lst[0] % 2 == 0:
            count = 0
        else:
            count = -1
    print(count)
