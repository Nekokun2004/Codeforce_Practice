def solve():
    N, M, H, Q = map(int, input().split())
    grasshoppers = []
    for _ in range(N):
        x, y = map(int, input().split())
        grasshoppers.append((x, y))
    nets = sorted(list(map(int, input().split())))
    queries = [int(input()) for _ in range(Q)]
    grasshoppers.sort(key=lambda g: g[1])
    for q in queries:
        if q > len(nets):
            print(-1)
            continue
        
        count = 0 
        distance = 0  
        last_x = 0  

        for i in range(q):  
            x, y = grasshoppers[i]
    
            if H - nets[i] <= y <= H + nets[i]:
                distance += abs(x - last_x)  
                last_x = x 
                count += 1
            else:
                break
        
        if count == q:
            print(distance)
        else:
            print(-1)

solve()
