T = int(input())
 
for _ in range(T) :
    n = int(input())
    x, y, z, w = 0, 0, 0, 0
    deg = [0] * (n + 1)
    for __ in range(n - 1) :
        u, v = map(int, input().split())
        deg[u] += 1
        deg[v] += 1
    s = " " + input()
    for i in range(2, n + 1) :
        if deg[i] == 1 :
            if s[i] == '?' :
                z += 1
            elif s[i] == '0' :
                x += 1
            else :
                y += 1
        elif s[i] == '?' :
            w += 1
    if s[1] == '0' :
        print(y + (z + 1) // 2)
    elif s[1] == '1' :
        print(x + (z + 1) // 2)
    else :
        print(max(x, y) + (z + (w % 2 if x == y else 0)) // 2)