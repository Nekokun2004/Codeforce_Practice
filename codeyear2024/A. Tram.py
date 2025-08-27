tram = int(input())
Box = []
for i in range(tram):
    a , b = [int(x) for x in input().split()]
    if len(Box)==0:
        Box.append( a + b )
        
    elif len(Box) > 0:
        c = Box[-1] - a
        d = c + b
        Box.append(d)
    
print(max(Box))


