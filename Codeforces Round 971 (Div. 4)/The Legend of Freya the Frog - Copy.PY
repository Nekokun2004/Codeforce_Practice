t = int(input())
for i in range(t):
    x,y,k = [int(x) for x in input().split()]
    if x == 0 and y == 0 :
       print(0)
    elif x < k and y < k :
       print(2)
       
    else:
        if x % k == 0 :
          a = x / k
        else:
          a = x//k+1
        if y % k == 0 :
          b = y / k
        else:
          b = y//k+1
        if a >= b:
          x = a * 2 -1
          print(int(x))
        else:
          x = b * 2 
          print(int(x))