def check_sum(A,B):
    a = 1
    b = 2
    keep = []
    for Anum in range(A):
       keep.append(a)
    for Bnum in range(B):
       keep.append(b)
    for i in range(2**len(keep)):
        sum = 0
        for j in range(len(keep)):
            if (i >> j) & 1:
                sum += keep[j]
            else:
                sum -= keep[j]
        if sum == 0:
            return 'Yes'
    return 'No'


t = int(input())
for i in range(t):
    A, B = [int(x) for x in input().split()]
    result = check_sum(A, B)
    print(result)
    
