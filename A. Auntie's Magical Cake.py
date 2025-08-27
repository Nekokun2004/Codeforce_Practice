n = int(input())
sum = 0
if n < 3:
    print(0)
elif n > 2 :
    while n > 2:
        sum += (((n-2)+1)*(n-2))//2 + 1 
        n -= 2

    print(sum)