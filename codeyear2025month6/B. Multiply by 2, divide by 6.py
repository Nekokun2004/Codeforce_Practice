
t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    count1 = 0
    if n > 1:
        while n > 6 or n == 3:
            # print("n1 = ",n)
            if n % 6 == 0:
                n = n // 6
                count += 1
            elif n % 3 == 0:
                n = n * 2
                count += 1
            else:
                count = -1
                break
            # print("n2 = ",n,'\n')
        if n > 6:
            count = count
        else:
            count += 1
    else:
        count = -1
    count += (count1 // 2)
    if n == 1:
        count = 0
    elif n < 6 and n != 3 :
        count = -1
    else:
        count = count

    # print("count = ",count)
    # print("count 1 = ",count1)
    print(count)
