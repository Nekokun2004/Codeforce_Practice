color1 = [int(x) for x in input().split()]
color2 = set(color1)
print(len(color1)-len(color2))