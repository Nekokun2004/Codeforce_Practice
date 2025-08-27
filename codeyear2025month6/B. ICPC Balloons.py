t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(input())
    Box = {}
    count = 0
    for i in lst:
        if i not in Box:
            Box[i] = 1
        else:
            Box[i] += 1
    for k,v in Box.items():
        if v == 1:
            count += 2
        else:
            count += v+1
    print(Box)
    print(count)
