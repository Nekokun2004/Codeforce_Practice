import math


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    Triangular = (n * (n + 1)) // 2
    
    if n <= 0 or m < n or m > Triangular:
        print(-1)
        continue
    elif m == Triangular:
        lst = [x for x in range(n,0,-1)]
        print(lst[0])
        countindex = 0
        while countindex < n-1:
            print(lst[countindex],lst[countindex+1])
            countindex += 1
    elif n == m :
        lst = [x for x in range(1,n+1)]
        print(lst[0])
        countindex = 0
        while countindex < n-1:
            print(lst[countindex],lst[countindex+1])
            countindex += 1
    elif m > n and m < n*2:
        use = m - n + 1
        lst = [use]
        lst1 = [x for x in range(1,n+1) if x != use]
        lst.extend(lst1)
        countindex = 0
        print(lst[0])
        while countindex < n-1:
            print(lst[countindex],lst[countindex+1])
            countindex += 1
    elif m > n and m >= n*2:
        lst = []
        copyn = n
        while m >= copyn*2 :
            if m - copyn >= copyn - 1 and m > 0 and copyn > 0:
                lst.append(copyn)
                m -= copyn
                copyn -= 1
            else:
                break
        use = m - copyn + 1
        lst.append(use)
        lst1 = [x for x in range(1,n+1) if x not in lst]
        lst.extend(lst1)
        countindex = 0
        print(lst[0])
        while countindex < n-1:
            print(lst[countindex],lst[countindex+1])
            countindex += 1
