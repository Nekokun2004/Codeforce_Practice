num1 = list(input())
num2 = list(input())
Box = []
for i in range(len(num1)):
    if num1[i] == num2[i]:
        Box.append('0')
    else:
        Box.append('1')
print(''.join(Box))