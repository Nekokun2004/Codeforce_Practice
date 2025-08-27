a,b = map(int,input().split())
index = 0
while a <= b:
    a = a*3
    b = b*2
    index += 1
print(index)
