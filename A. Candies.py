for _ in range(int(input())):
    n = int(input())
    num = 3

    if n % num == 0:
        print(n // num)
    else:
        while n % num != 0 :
            num = (num * 2) + 1
            if n % num == 0:
                print(n // num)
    # elif n % 7 == 0:
    #     print(n // 7)
    # elif n % 15 == 0:
    #     print(n // 15) 