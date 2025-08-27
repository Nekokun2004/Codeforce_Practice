def myfunc(n,arr):
    if(n<=1):
        return arr[0]+1
    else:
        arr1=[arr[i] for i in range(0,n,2)]
        arr2= [arr[j] for j in range(1,n,2)]
        return max(max(arr1)+len(arr1), max(arr2)+len(arr2))
    
tc = int(input())
 
for _ in range(tc):
    n=int(input())
    arr = [int(x) for x in input().split()]
    # print(n,arr)
    print(myfunc(n,arr))