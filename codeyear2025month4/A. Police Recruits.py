n = int(input())
casen = map(int,input().split())
numberpoliceC = 0
untreated = 0
# count = 1
for i in casen:
#   print(f"[{count}]")
#   count += 1
#   print("i =",i)
  if i > 0 :
    numberpoliceC += i
  elif i == -1:
    if numberpoliceC == 0:
      untreated += abs(i)
    elif numberpoliceC > 0:
      numberpoliceC += i
#   print("numberpolice = ",numberpoliceC)
#   print("untreated = ",untreated)
#   print("------------------")
  
print(untreated)