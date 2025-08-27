usekeyboard = [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']
]  
direction = input()
if direction == 'R':
    direction = -1
else:
    direction = 1
lst = list(input())
index = 0
Box = []
for ch in lst:
    found = False
    for row in usekeyboard:
        if ch in row:
            idx = row.index(ch)
            new_idx = idx + direction
            if 0 <= new_idx < len(row):
                Box.append(row[new_idx])
            found = True
            break
    if not found:
        Box.append(ch)  
print("".join(Box))
    
