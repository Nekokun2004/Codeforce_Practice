import sys

def func1(n):
    n = n * 2
    return n 

def func2(n):
    n = (n-1)//3
    return n 

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k,x = map(int,input().split())
    print(x * (2**k))