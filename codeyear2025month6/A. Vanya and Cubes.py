import math


n = int(input())
count = 0
x = 1
sumcubes = 0
# print(num)
while count < n:
    total = x * (x+1) // 2
    count += total
    # print("conut = ",count)
    x += 1
    if count > n:
        x -= 1
        count -= total
        break
if n >= count:
    x -= 1
    print(x)
