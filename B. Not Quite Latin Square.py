import sys

input = sys.stdin.readline

t = int(input())
out = []
for i in range(t):
    Box = []
    for i in range(3):
        word = list(input().strip())
        Box += word
    # print(Box)
    if Box.count('A') == 2:
        out.append('A')
    elif Box.count('B') == 2:
        out.append('B')
    elif Box.count('C') == 2:
        out.append('C')
print("\n".join(out))
