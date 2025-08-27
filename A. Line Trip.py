for _ in range(int(input())):
    n, x = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    maxdistance = max(lst[0], (x - lst[-1]) * 2)
    for i in range(n - 1):
        gap = lst[i+1] - lst[i]
        if gap > maxdistance:
            maxdistance = gap
    
    print(maxdistance)
