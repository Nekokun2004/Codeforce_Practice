n,k = map(int,input().split())
timestart = 20
count = 0
index = 5
hour = k // 60
minute = k % 60
# print("minute = ",minute)
timestart += hour
# print(f"{timestart}.{minute}")
if timestart > 24 :
    print(0)
else:
    while timestart < 24 and count < n:
        minute += index
        index += 5
        count += 1
        if minute >= 60 :
            minute -= 60
            timestart += 1
            if timestart >= 24 and minute > 0:
                count -= 1
                minute -= index
                break
        # print(f"{timestart}.{minute}")
    print(count)
        