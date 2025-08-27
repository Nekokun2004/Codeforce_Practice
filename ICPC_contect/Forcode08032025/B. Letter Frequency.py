import sys
from collections import Counter

lst = {}
for line in sys.stdin:
    line = list(line)
    line = [ch for ch in line if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z')]
    line = [ch.upper() for ch in line]
    # print(line)
    for i in range(len(line)):
       if line[i] not in lst :
           lst[line[i]] = 1
       else:
           lst[line[i]] += 1
lst = (sorted(lst.items(), key=lambda x: (-x[1], x[0])))
# print(lst)
for i,x in lst:
    print(i,x)