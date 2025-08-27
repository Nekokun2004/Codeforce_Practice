import sys

input = sys.stdin.readline

t = int(input())
out = []
for i in range(t):
    n = int(input())
    lsta = list(input().strip())
    m = int(input())
    lstb = list(input().strip())
    mode = list(input().strip())

    # print(mode)
    index = 0
    for char in mode:

        if char == 'D':
            lsta.append(lstb[index])
        elif char == 'V':
            lsta.insert(0,lstb[index])
        index += 1 

    # print(lsta)
    out.append(''.join(lsta))
print("\n".join(out))