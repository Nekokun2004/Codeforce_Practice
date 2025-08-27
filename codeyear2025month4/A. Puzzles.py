n, m = map(int, input().split())
f = list(map(int, input().split()))
f.sort()
index = 1
min_diff = float('inf')
for i in range(m - n + 1):
    print("i = ",i)
    print("index =",index)
    index += 1
    diff = f[i + n - 1] - f[i]
    print(f"diff = {diff}")
    min_diff = min(min_diff, diff)
    print("min = ",min_diff)

print(min_diff)
