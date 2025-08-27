import sys

n = int(input())
for i in range(n):
    x = []
    for _ in range(8):
        word = str(input())
        word = word.replace('.','')
        word = word.strip()
        x.append(word)
    print(''.join(x))