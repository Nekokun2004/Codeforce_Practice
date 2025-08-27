n = int(input())

for i in range(n):
    t = int(input())
    lst = list(input())
    lst.sort(reverse=True)
    print(ord(lst[0])-ord('a')+1)