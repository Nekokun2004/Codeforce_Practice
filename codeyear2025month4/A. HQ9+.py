word = list(input())
# print(word)

Core =  ['H','Q','9']

if any(char in Core for char in word):  
    print("YES")
else:
    print("NO")
