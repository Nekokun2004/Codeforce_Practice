n = int(input())
a = [int(x) for x in input().split()]
result = [x for x in a if x % 2 == 1]
if len(result) == 1:
    number = int(result[0])
    position = [i for i in range(len(a)) if a[i] == number]
    number = int(position[0]) + 1
    print(number)
else:
    result = [x for x in a if x % 2 == 0]
    number = int(result[0])
    position = [i for i in range(len(a)) if a[i] == number]
    number = int(position[0]) + 1
    print(number)