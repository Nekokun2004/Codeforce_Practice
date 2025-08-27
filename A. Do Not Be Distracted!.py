t = int(input())
for _ in range(t):
    n = int(input())
    word = list(input())
    answer = True
    Box = []
    for i in range(n-1) :
      if word[i] not in Box:
         Box.append(word[i])
      if word[i] != word[i+1] and word[i+1] in Box:
         answer = False
         break
    if answer :
       print("YES")
    else:
       print("NO")
    