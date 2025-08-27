n = int(input())
count = 0
for i in range(n):
    a = input()
    if '++' in a :
        count += 1
    elif '--' in a :
        count -= 1
print(count)