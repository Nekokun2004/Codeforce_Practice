word = input()
vowels = "AOYEUIaoyeui"
Box = []
for i in word :
    i = i.lower()
    Box.append(i)
    if i in vowels:
        Box.remove(i)
newword = '.'+'.'.join(Box)
print(newword)