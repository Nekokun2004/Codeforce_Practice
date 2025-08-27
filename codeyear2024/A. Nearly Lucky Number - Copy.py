num_input = list(input())
numberunluck = ['0','1','2','3','5','6','8','9']
Box = []
too = [item for item in numberunluck if item in num_input]
print("too = ",too)
if len(num_input) < 2:
   print("NO")
else:
   if too :
      Box.extend(too)
      print(len(Box))
      if len(Box) - len(num_input) == 4 or len(Box) - len(num_input) == 7:
          print("YES")
      else:
          print("NO")

