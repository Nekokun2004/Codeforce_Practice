t = int(input())
for i in range(t):
    number1 = str(input())
    number2 = list(number1)
    Box = []
    num2 = len(number2)
    ba = num2-1
    count = 0
    for x in range(num2):
        if number2[x] != '0':
            ba = min(ba, count + num2 - x - 1)
            count += 1
    print(ba)
    
        

