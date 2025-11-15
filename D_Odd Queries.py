import sys

input = sys.stdin.readline
out = []

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + a[i]
    total = pref[n]
    
    for __ in range(q):
        l, r, k = map(int, input().split())
        seg_sum = pref[r] - pref[l - 1]       
        length = r - l + 1
        new_total = total - seg_sum + k * length
        
        if new_total % 2 == 1:
            out.append("YES")
        else:
            out.append("NO")

print("\n".join(out))
