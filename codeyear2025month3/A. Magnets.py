n = int(input())
count = 0
Box = []

for i in range(n):
    meg = input()
    if i == 0 :
        Box.append(meg)
        count += 1
    else:
        if meg in Box:
            pass
        else:
            Box.clear()
            Box.append(meg)
            count += 1
print(count)