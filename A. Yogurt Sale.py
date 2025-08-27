import sys 


input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,a,b = map(int,input().split())
    nb = n // 2
    numb = n % 2
    minva = min((n*a),(nb*b+(numb*a)))
    print(minva)