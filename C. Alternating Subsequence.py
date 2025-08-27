# t = int(input())
# for _ in range(t):
#     n = int(input())
#     lst = list(map(int,input().split()))
#     Box = lst[0]
#     # print(Box)
#     index = 1
#     while index < n:
#         if (lst[index] > 0 and Box[-1] > 0) or (lst[index] < 0 and Box[-1] < 0):
#             maxvalues = max(lst[index],Box[-1])
#             Box[-1] = maxvalues
#             index += 1
#         else:
#             Box.append(lst[index])
#             index += 1
#         # print("index = ",index)
#         # print(Box)
#     print(sum(Box))


import sys
input = sys.stdin.readline

t = int(input())
out = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    total = 0
    curr = a[0]

    for i in range(1, n):
        if (a[i] > 0) == (curr > 0):
            curr = max(curr, a[i])
        else:
            total += curr
            curr = a[i]
    
    total += curr
    out.append(str(total))

print('\n'.join(out))


            
            
