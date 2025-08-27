t = int(input())
for i in range(t):
    n = int(input())
    positions = []
    for i in range(n):
        arr = []
        word = [str(x) for x in input()]
        arr.extend(word)
        for a in range(4):
          if arr[a] == '#':
              positions.append(a+1)
    for pos in reversed(positions):
        print(pos, end=" ")  
      
    