import math

def is_t_prime(num):
    root = math.isqrt(num)
    return root * root == num and checkprime(root)

def checkprime(p):
   if p <= 1:
      return False
   for i in range(2, int(math.sqrt(p)) + 1):
      if p % i == 0:
         return False
   return True

t = int(input())
n = list(map(int, input().split()))

for num in n:
   if is_t_prime(num):
      print("YES")
   else:
      print("NO")
