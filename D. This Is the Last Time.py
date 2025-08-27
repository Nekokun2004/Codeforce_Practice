t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    casinos = []
    for i in range(n):
        l,r,get = map(int,input().split())
        casinos.append((l, r, get))
    casinos.sort(key=lambda x: x[0])
    # print(casinos)
    for l,r,get in casinos:
        if k >= l and k <= r and get >= k:
            k = get
            lost = False
        else:
            lost = True
            
    print(k)
