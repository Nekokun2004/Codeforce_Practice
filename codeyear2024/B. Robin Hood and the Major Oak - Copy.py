def leaves_output(n,k):
    start_year = max(1, n - k + 1)
    print('start_year = ',start_year)
    leaves = (n * (n + 1)) // 2 - (start_year * (start_year - 1)) // 2
    print('leaves ตัวต้น = ',(n * (n + 1)) // 2)
    print('leaves ตัวลบ = ',(start_year * (start_year - 1)) // 2)
    print('leaves = ',leaves)
    if leaves % 2 == 0:
        return "Yes"
    else:
        return "No"

testcase = int(input())
for i in range(testcase):
    n,k = map(int,input().split())
    print(leaves_output(n,k))
    
    

