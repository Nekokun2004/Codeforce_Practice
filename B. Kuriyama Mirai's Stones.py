import sys

input = sys.stdin.readline

n = int(input())
costrock = list(map(int, input().split()))
orig_pref = [0] * (n + 1)
for i in range(1, n + 1):
    orig_pref[i] = orig_pref[i-1] + costrock[i-1]

sortedcost = sorted(costrock)
sorted_pref = [0] * (n + 1)
for i in range(1, n + 1):
    sorted_pref[i] = sorted_pref[i-1] + sortedcost[i-1]

q = int(input())
out = []
for _ in range(q):
    mode, l, r = map(int, input().split())
    if mode == 1:
        out.append(orig_pref[r] - orig_pref[l-1])
    else:
        out.append(sorted_pref[r] - sorted_pref[l-1])

print("\n".join(map(str, out)))
