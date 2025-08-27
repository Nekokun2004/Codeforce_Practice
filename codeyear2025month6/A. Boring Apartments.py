t = int(input())
for _ in range(t):
    x = list(input())
    countx = len(x)
    setx = int(''.join(map(str,set(x))))
    count = (setx-1)*10
    for i in range(1,len(x)+1):
        count += i


    print(count)