t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if len(a) % 2 ==1:
        newa = (a[len(a)//2])
    else:
        new = (a[len(a)//2 - 1] + a[len(a)//2]) / 2
        newa = (min(a, key=lambda x: abs(x - new)))
        

    if newa <= k:
        print("YES")
    else:
        print("NO")