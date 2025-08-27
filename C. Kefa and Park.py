import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
lsta = list(map(int, input().split()))

graph = {}
for _ in range(n-1):
    x, y = map(int, input().split())
    graph.setdefault(x, []).append(y)
    graph.setdefault(y, []).append(x)

ans = 0
q = deque()
q.append((1, -1, 0))

while q:
    node, parent, consecutive = q.popleft()

    if lsta[node-1] == 1:
        consecutive += 1
    else:
        consecutive = 0
    
    if consecutive > m:
        continue

    is_leaf = True
    for nei in graph[node]:
        if nei != parent:
            is_leaf = False
            q.append((nei, node, consecutive))
    
    if is_leaf:
        ans += 1

print(ans)
