Sto = input()
n = 0
for i in Sto:
    if '4' in i:
        n += 1
    elif '7' in i:
        n += 1
    elif 'A' in i:
        n += 1
    elif 'b' in i:
        n += 1
    elif 'C' in i:
        n += 2
    elif 'd' in i:
        n += 1
    elif 'F' in i:
        n += 2
print(n)