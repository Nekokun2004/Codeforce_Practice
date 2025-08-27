import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

maxvalues = lst[0]
count = 1
usecount = count

for i in lst[1:]:
    if i > maxvalues:
        maxvalues = i
        count += 1
    else:
        maxvalues = i
        count = 1   
    usecount = max(count, usecount)

print(usecount)



# import sys
# data = sys.stdin.read().split()
# n = int(data[0])
# lst = list(map(int, data[1:n+1]))
# maxvalues = lst[0]
# count = 1
# usecount = count
# for i in lst[1:]:
    
#     if i > maxvalues :
#         maxvalues = i
#         count += 1
#     else:
#         maxvalues = i
#         count = 1
#     usecount = max(count,usecount)
#     # print(count)
# print(usecount)