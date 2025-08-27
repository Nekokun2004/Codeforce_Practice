n,t = map(int,input().split())
lst = list(map(int,input().split()))
count = 1
index = 0
while count < t:
    count += lst[index]
    index += lst[index]
    # print(count)
if count == t:
    print("YES") 
else:
    print("NO")