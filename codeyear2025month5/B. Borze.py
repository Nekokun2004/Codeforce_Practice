Borze = list(input())
lst = []
# print(Borze)
index = 0
while index < len(Borze):
    if Borze[index] == '.':
      lst.append(0)
      index += 1
    elif Borze[index] == '-':
        index += 1
        if Borze[index] == ".":
            lst.append(1)
            index += 1
        elif Borze[index] == "-":
            lst.append(2)
            index += 1
print("".join(map(str, lst)))
    