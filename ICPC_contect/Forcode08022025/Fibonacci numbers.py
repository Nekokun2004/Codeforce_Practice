import sys

def fiboncci(n):
    lst = [0,1]
    index = 1
    while True:
        if lst[index-1]+lst[index] <= n:
            lst.append(lst[index-1]+lst[index])
        else:
            break
        index += 1
    return lst

for line in sys.stdin:
    line = int(line)
    answer = fiboncci(line)
    print("lst of fiboncci = ",answer) #for list
    print(sum(answer))
    # sumfibonacci = sum(fiboncci(line))
    # print(sumfibonacci)
    
        

