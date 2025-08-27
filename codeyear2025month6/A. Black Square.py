a,b,c,d = map(int,input().split())
number = list(map(int,input()))
# print(number)
count = 0
countone = number.count(1)
counttwo = number.count(2)
countthree = number.count(3)
countfour = number.count(4)
count += countone*a
count += counttwo*b
count += countthree*c
count += countfour*d
print(count)