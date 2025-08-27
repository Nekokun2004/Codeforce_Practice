import sys

n = int(sys.stdin.readline())
maxva = -float('inf')  
minva = float('inf')   

for _ in range(n):
    num = int(sys.stdin.readline())
    if num > maxva:
        maxva = num
    if num < minva:
        minva = num

print(maxva)
print(minva)
