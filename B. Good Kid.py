import math

t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    position = [i for i,x in enumerate(lst) if x == min(lst)]
    lst[position[0]] += 1
    answer = math.prod(lst)
    # print(lst)
    print(answer)