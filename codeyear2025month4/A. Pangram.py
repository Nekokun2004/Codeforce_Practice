n = int(input()) 
s = input()    
s = s.lower()     
alphabet = set(s)

if len(alphabet) >= 26:
    print("YES")
else:
    print("NO")
