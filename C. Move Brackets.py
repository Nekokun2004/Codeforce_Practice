t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(input())
    # print(lst)
    count = 0
    maxcount = 0
    for i in lst:
        if i == ')':
            count += 1
            maxcount = max(count,maxcount)
        else:
            count -= 1
            maxcount = max(count,maxcount)
        # print(count)
        # print("maxcount = ",maxcount)
    print(maxcount)