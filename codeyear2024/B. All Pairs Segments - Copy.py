for _ in range(int(input())):
  n,q=[int(i) for i in input().split()]
  arr=[int(i) for i in input().split()]
  Q=[int(i) for i in input().split()]
  from collections import *
  has=Counter()
  C=Counter()
  for i in range(n):
    C[(n-1+(i*(n-i-1)))]+=1
    if i>0:
      cnt=arr[i]-arr[i-1]-1
      val=i*(n-i)
      C[val]+=cnt
  for i in Q:
    print(C[i],end=" ")
  print(" ")