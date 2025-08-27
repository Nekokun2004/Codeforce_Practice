import sys

input = sys.stdin.readline

t = int(input())
out = []
for _ in range(t):
    word = list(input())
    word[-3::] = 'i'
    out.append(''.join(word))
print("\n".join(out))