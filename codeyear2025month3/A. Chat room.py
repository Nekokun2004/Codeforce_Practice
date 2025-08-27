word = list(input())
hello = ['h','e','l','l','o',]
Box = []
index = 0
for i in range(len(word)):
      if word[i] == hello[index] :
            Box.append(word[i])
            index += 1
            if index == 5:
                  break
w_hello = "".join(Box)
if w_hello == "hello":
      print("YES")
else:
      print("NO")