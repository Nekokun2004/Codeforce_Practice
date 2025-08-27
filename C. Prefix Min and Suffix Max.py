t = int(input().strip())
results = []
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))
    
    min_prefix = [0] * n
    min_prefix[0] = a[0]
    for i in range(1, n):
        min_prefix[i] = min(min_prefix[i-1], a[i])
        
    max_suffix = [0] * n
    max_suffix[n-1] = a[n-1]
    for i in range(n-2, -1, -1):
        max_suffix[i] = max(max_suffix[i+1], a[i])
        
    res = []
    for i in range(n):
        if a[i] == min_prefix[i] or a[i] == max_suffix[i]:
            res.append('1')
        else:
            res.append('0')
            
    results.append(''.join(res))

for r in results:
    print(r)

# t = int(input())
# for _ in range(t):
#     n =int(input())
#     lst = list(map(int,input().split()))
#     answer = [0] * n
#     # print(answer)
#     position = [i for i,x in enumerate(lst) if x == min(lst) or x == max(lst)]
#     minposition = position[0]
#     maxposirion = position[-1]
    
#     # print(position)
#     for i in range(n):
#         if i == minposition:
#             answer[i] = 1
#         elif i == maxposirion:
#             answer[i] = 1
#     while minposition != 0 or maxposirion != n-1:
#         if minposition != 0:
#             minposition -= 1
#             answer[minposition] = 1
#         if maxposirion != n-1:
#             maxposirion += 1
#             answer[maxposirion] = 1
#     answer = int(''.join(map(str,answer)))
#     print(answer)
     