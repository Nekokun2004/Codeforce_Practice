from itertools import groupby
from collections import Counter

phone = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

word = str(input())
groups = [''.join(g) for _, g in groupby(word)]  
# print(groups)
lst = []
answer = []
for i in groups:
    lenlst = len(i)
    # print(lenlst)
    while lenlst // len(phone[i[0]]) >= 1:
        lst.append(phone[i[0]][len(phone[i[0]])-1])
        lenlst -= len(phone[i[0]])
    if lenlst % len(phone[i[0]]) != 0:
        use = lenlst % len(phone[i[0]]) 
        lst.insert(0,phone[i[0]][use-1])
    answer.extend(lst)
    # print(lst)
    lst = []
print(''.join(answer))
    
    
