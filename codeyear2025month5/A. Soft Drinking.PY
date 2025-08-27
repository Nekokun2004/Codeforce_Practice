n, k, l, c, d, p, nl, np = map(int,input().split())
enough  = (k * l) // nl
limes = c * d
toats = p // np
print(min(enough,limes,toats)//n)