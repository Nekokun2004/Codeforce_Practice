import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    s = input().strip()

    i = x
    while i > 0 and s[i - 1] != '#':
        i -= 1
    l = min(i + 1, n + 1 - x)

    i = x
    while i <= n and s[i - 1] != '#':
        i += 1
    r = min(n + 2 - i, x)

    ans = max(l, r)
    print(ans)


# t = int(input())
# for _ in range(t):
#     n, x = map(int, input().split())
#     lst = list(input())
#     count = 0
#     x -= 1
#     lst[x] = "person"
 
#     while 0 < x < n - 1:
#         notwall = [i for i, v in enumerate(lst) if v != '#' and i != x]
#         if not notwall:
#             break
 
#         mindist = min(abs(x - y) for y in notwall)
#         closest_candidates = [y for y in notwall if abs(x - y) == mindist]
 
#         if len(closest_candidates) == 1:
#             closest = closest_candidates[0]
#         else:
#             def distance_to_edge(idx):
#                 return min(idx, n - 1 - idx)
#             closest = min(closest_candidates, key=distance_to_edge)
 
#         lst[closest] = '#'
 
#         left_walls = [i for i in range(x) if lst[i] == '#']
#         right_walls = [i for i in range(x + 1, n) if lst[i] == '#']
 
#         if not left_walls or not right_walls:
#             break
 
#         if len(left_walls) < len(right_walls):
#             target = left_walls[-1]
#         elif len(right_walls) < len(left_walls):
#             target = right_walls[0]
#         elif len(right_walls) == len(left_walls):
#             left_nowalls = [i for i in range(x) if lst[i] != '#']
#             right_nowalls = [i for i in range(x + 1, n) if lst[i] != '#']
#             minva = min(len(left_nowalls),len(right_nowalls))
#             if minva == len(left_nowalls):
#                 target = left_walls[-1]
#             elif minva == len(right_nowalls):
#                 target = right_walls[0]
#         else:
#             target = left_walls[-1]
 
#         lst[x] = '.'
#         lst[target] = 'person'
#         x = target
#         count += 1
 
#     count += 1
#     print(count)

