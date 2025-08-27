t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    best = n  

    for l in range(n):
        print("\nl = ",l)
        for r in range(l, n):
            print("r = ",r)
            if (a[l] + a[r]) % 2 == 0:
                cost = l + (n - 1 - r)
                print("cost = ",cost)
                if cost < best:
                    best = cost
                    print("best = ",best)

    print(best)
