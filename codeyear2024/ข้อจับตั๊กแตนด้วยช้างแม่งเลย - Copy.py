def solve():
    from bisect import bisect_left
    
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
        available_nets = nets[:]
        distance = 0
        last_x = 0
        net_used = [False] * len(available_nets)
        
        for i in range(q):
            x, y = grasshoppers[i]
            caught = False
            
            for j in range(len(available_nets)):
                net_length = available_nets[j]
                if H - net_length <= y <= H + net_length:
                    distance += abs(x - last_x)
                    last_x = x
                    net_used[j] = True
                    caught = True
                    break
            
            if not caught:
                distance = -1
                break
        
        if distance != -1:
            print(distance)
        else:
            print(-1)

solve()
