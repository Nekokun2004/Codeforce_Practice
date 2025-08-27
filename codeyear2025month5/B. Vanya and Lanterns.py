n, l = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

max_gap = 0
if n > 1:
    for i in range(n - 1):
        gap = a[i + 1] - a[i]
        if gap > max_gap:
            max_gap = gap
    d = max(a[0] - 0, l - a[-1], max_gap / 2)
else:
    d = max(a[0] - 0, l - a[0])

print(f"{d:.10f}")
