t = int(input())
for i in range(t):
    n = int(input())
    Box = list(map(int, str(n)))
    num = len(Box)
    num1 = [x for x in Box if x != 0]
    print(len(num1))
    for o in Box:
        zeroadd = '0'
        if o != 0:
            answer = o * (10**(num-1))
            print(answer,end=" ")
        num -= 1

    