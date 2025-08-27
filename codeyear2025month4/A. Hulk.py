number = int(input())
count = 1
while number > 0:
    if count % 2 == 1:
        print("I hate ",end = '')
    else:
        print("that I love ",end = '')
        if number != 1:
            print("that ",end = '')
    if number == 1:
        print("it ")
    count += 1
    number -= 1