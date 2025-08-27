import sys



for line in sys.stdin:
    print(line)
    a,b,c = map(int,line.split())
    lst = list(map(int,line.split()))
    print(lst)
    if a+b <= c or a+c <= b or b+c <= a:
        print("Yes")
    else:
        print("No")