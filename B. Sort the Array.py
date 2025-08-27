import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
# lst = lst[:1] + lst[len(lst)-1:0:-1] + lst[len(lst)-1:]
sortedlst = sorted(lst)
position = [x for x in range(len(lst)) if lst[x] != sortedlst[x]]
# print(position)
if len(position) == 0:
   print("yes")
   print(1,1)
elif len(position) == len(lst):
   lst.reverse()
   if lst == sortedlst  :
      print("yes")
      print(position[0]+1,position[-1]+1)
   else:
      print("no")
elif len(position) > 0:
   if position[0] == 0:
      lst[position[0]:position[-1]+1] = lst[position[-1]::-1]
   elif position[0] > 0:
      lst[position[0]:position[-1]+1] = lst[position[-1]:position[0]-1:-1]
   # print(lst)
   if lst == sortedlst :
      print("yes")
      print(position[0]+1,position[-1]+1)
   else:
      print("no")
