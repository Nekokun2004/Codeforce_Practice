import sys

n = int(sys.stdin.readline())
if n % 2:
    print(-1)
else:
    ans = [0] * n
    ans[0::2] = range(2, n + 1, 2)   
    ans[1::2] = range(1, n, 2)       
    print(*ans)


# import sys

# def func1(n):
#     lst = []
#     num = 1
#     for i in range(n // 2):
#        lst.append(num+1)
#        lst.append(num)
#        num += 2
#     return lst

# input = sys.stdin.readline

# n = int(input())

# if n % 2 == 0:
#     answer = func1(n)
#     print(*answer)
# else:
#     print(-1)