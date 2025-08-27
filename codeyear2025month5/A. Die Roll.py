y,w = map(int,input().split())
maxpoint = max(y,w)
dot = (6 - maxpoint) + 1 
point = 6
if point % dot == 0:
    point = point // dot
    dot = 1
elif point % 2 == 0 and dot % 2 == 0:
    dot //= 2
    point //= 2
elif point % 3 == 0 and dot % 3 == 0:
    dot //= 3
    point //= 3
print(f"{dot}/{point}")