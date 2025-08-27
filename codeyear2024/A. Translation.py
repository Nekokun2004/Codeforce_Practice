stringori = input()
word = input() 
Box = []
for i in stringori[::-1]:
    Box.append(i)
Boxnew = ''.join(Box)
if Boxnew == word :
    print("YES")
else:
    print("NO")
