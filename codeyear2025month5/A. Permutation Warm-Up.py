t = int(input())
for i in range(t):
    n = int(input())
    maxn = n
    total = 0
    for x in range(1,n + 1):
    #    print("abs(maxn - x) = ",abs(maxn - x))
    #    print("maxn = ",maxn)
    #    print("x = ",x)
    #    print("-------------")
       total += abs(maxn - x)
       maxn -= 1
    answer = ( total // 2 ) + 1
    print(answer) 

# from itertools import permutations
# t = int(input())
# for i in range(t):
#     n = int(input())
#     count = 0 
#     Box = []
#     nowcount = {}
#     for p in permutations(range(1, n + 1)):
#         f_p = sum(abs(p[i] - (i + 1)) for i in range(n))
#         print(f"p = {p}, f(p) = {f_p}")
#         if f_p not in Box :
#             count += 1
#             Box.append(f_p)
#         if f_p not in nowcount:
#             nowcount[f_p] = 1
#         else:
#             nowcount[f_p] += 1
#     print("nowcount = ",nowcount)
#     print(count)