import sys, heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    m = 2 * n

    ans = [0] * (m + 1)
    buckets = [[] for _ in range(m + 2)]
    unused = [-x for x in range(1, n + 1)]
    heapq.heapify(unused)

    for i in range(1, m + 1):
        if buckets[i]:
            x = max(buckets[i])
            ans[i] = x
            for y in buckets[i]:
                if y == x:
                    continue
                j = i + y
                buckets[j].append(y)
            buckets[i].clear()
        else:
            x = -heapq.heappop(unused)
            ans[i] = x
            buckets[i + x].append(x)

    print(*ans[1:])
