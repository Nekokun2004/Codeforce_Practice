import sys

input = sys.stdin.readline

t = int(input())
out = []
for _ in range(t):
    word = list(input().strip())
    
    word = word[::-1]
    
    for i in range(len(word)):
        if word[i] == 'p':
            word[i] = 'q'
        elif word[i] == 'q':
            word[i] = 'p'
    out.append("".join(word))
print("\n".join(out))
        