n,m = [int(x) for x in input().split()]
string = '#'
dot = '.'
count = 1
for i in range(1,n+1):
    if i % 2 == 1:
        print(string*m)
    else:
        if count % 2 == 1:
            print(f"{dot*(m-1)}{string}")
            count += 1
        else:
            print(f"{string}{dot*(m-1)}")
            count += 1
        