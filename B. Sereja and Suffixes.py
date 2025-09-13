import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

distinct_count = [0] * (n + 2)

seen = set()
count = 0

for i in range(n - 1, -1, -1):
    if a[i] not in seen:
        seen.add(a[i])
        count += 1
    distinct_count[i + 1] = count   

out = []
for _ in range(m):
    l = int(input())
    out.append(str(distinct_count[l]))

print("\n".join(out))
