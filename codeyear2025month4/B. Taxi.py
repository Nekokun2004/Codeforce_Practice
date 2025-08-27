from collections import Counter
import math

n = int(input())
groups = list(map(int, input().split()))
count = Counter(groups)
taxis = 0
taxis += count[4]
pair_3_1 = min(count[3], count[1])
taxis += count[3]
count[1] -= pair_3_1
taxis += count[2] // 2
count[2] = count[2] % 2  
if count[2]:
    taxis += 1  
    count[1] -= min(2, count[1])
if count[1] > 0:
    taxis += math.ceil(count[1] / 4)

print(taxis)
