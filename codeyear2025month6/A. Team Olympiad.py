# def position(n,lst):
#     answer = lst.index(n)
#     return answer+1



n = int(input())
lst = list(map(int,input().split()))
countone = lst.count(1)
counttwo = lst.count(2)
countthree = lst.count(3)
answerfirst = min(countone,counttwo,countthree)
print(answerfirst)
positionone = [x for x in range(n) if lst[x] == 1]
positiontwo = [x for x in range(n) if lst[x] == 2]
positionthree = [x for x in range(n) if lst[x] == 3]
# print("one = ",positionone)
# print("two =",positiontwo)
# print("three = ",positionthree)
for i in range(answerfirst):
    Box = []
    Box.append(positionone[i]+1)
    Box.append(positiontwo[i]+1)
    Box.append(positionthree[i]+1)
    print(*Box)
