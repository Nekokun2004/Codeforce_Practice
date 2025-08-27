import sys

def fiboncci(n):
    lst = [0,1]
    index = 1
    while index < n:
        lst.append(lst[index-1]+lst[index])
        index += 1
    return lst

for line in sys.stdin:
    line = int(line)
    answer = fiboncci(line)
    print(sum(answer))

    
        

