t = int(input())
for _ in range(t):
    n = int(input())
    halfn = n // 2
    if halfn % 2 == 1:
        print("NO")
    else:
        lst1 = [i for i in range(2,n+1,2)]
        lst2 = [i for i in range(1,n,2)]
        sumlst1 = sum(lst1)
        sumlst2 = sum(lst2)
        lst2[-1] += (sumlst1 - sumlst2)
        print("YES")
        lst1.extend(lst2)
        print(*lst1)
        
