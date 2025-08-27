n = int(input())
lst = list(map(int,input().split()))
usesum = sum(lst)
if usesum < n:
    print(-1)
elif usesum == n:
    print(*lst)
elif usesum > n:
    diff = usesum - n
    indices = [i for i, v in enumerate(lst) if v == diff]
    if not indices:
        print(-1)
    else:
        idx = indices[0]
        lst[idx] = 0
        print(*lst)