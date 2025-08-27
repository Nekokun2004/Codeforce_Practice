for _ in range(int(input())):
    n,c = map(int,input().split())
    lst = list(map(int,input().split()))
    count = 0
    index = 0
    lst.sort(reverse=True)
    while len(lst) > 0:
        # print(lst)
        while lst[index] > c:
            lst.remove(lst[index])
            count += 1
            if len(lst) == 0:
                break
            elif lst[index] <= c:
                index = 0
                break
        if len(lst) > 0:
            lst.remove(lst[index])
            for j in range(index, len(lst)):
                lst[j] *= 2
        else:
            break
        # print(lst)
    print(count)