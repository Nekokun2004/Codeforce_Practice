def has_odd_divisor(n):
    return n & (n - 1) != 0

t = int(input())
for _ in range(t):
    n = int(input())
    print("YES" if has_odd_divisor(n) else "NO")


# import math
# def integer(x):
#     lst = []
#     for i in range(1,int(math.sqrt(x))+1):
#         if x % i == 0:
#            lst.append(i)
#            if i != x // i:
#                lst.append(x // i)
#     lst.sort()
#     return lst


# t = int(input())
# for _ in range(t):
#     n = int(input())
#     answer = integer(n)
#     answer = [x for x in answer if x % 2 == 1]
#     if len(answer)>1:
#         print("YES")
#     else:
#         print("NO")

    