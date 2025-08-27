testcase = int(input())
BoxX = []
BoxY = []
BoxZ = []
for _ in range(testcase):
    x,y,z = map(int,input().split())
    BoxX.append(x)
    BoxY.append(y)
    BoxZ.append(z)
if sum(BoxX) == 0 and sum(BoxY) == 0 and sum(BoxZ) == 0 :
    print("YES")
else:
    print("NO")