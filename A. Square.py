import sys
from collections import deque
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    graph = {}
    for _ in range(4):
        x,y = map(int,input().split())
        graph.setdefault(x, []).append(y)
    # print(graph)
    x = sorted(graph.keys(),reverse=True)
    x = x[0] - x[1]
    
    for i in graph:
        y = graph[i]
        y.sort(reverse=True)
        y = y[0] - y[1]
        break
    # y = 
    print(x*y)

    