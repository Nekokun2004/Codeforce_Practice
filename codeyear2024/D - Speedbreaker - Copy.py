def solve():
    n = int(input())
    a = list(map(int,input().split()))
    inv = [[] for _ in range(n+1)]
    for i in range(n):
        inv[a[i]].append(i)
    l,r = 0,0
    f = True
    res = [0,n-1]
    for i in range(1,n+1):
        if inv[i] != []:
            if f:
                l,r = min(inv[i]),max(inv[i])
                res = [max(r-i+1,res[0]),min(l+i-1,res[1])]
                f = False
                if r-l+1 > i:
                    print(0)
                    return 0
                continue
            l = min(l,min(inv[i]))
            r = max(r,max(inv[i]))
            res = [max(r-i+1,res[0]),min(l+i-1,res[1])]
            if r-l+1 > i:
                print(0)
                return 0
    print(res[1] - res[0] + 1)
for _ in range(int(input())):
    solve()
