
t = int(input())  
for _ in range(t):
    l, r = map(int, input().split())  
    n = r - l + 1  
    e = (r // 2) - ((l - 1) // 2)  
    o = n - e  
    ans = min(e, o // 2)  
    print(ans)

