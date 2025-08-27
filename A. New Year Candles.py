a, b = map(int, input().split())

hours = 0     
burnt = 0      

while a > 0:
    hours += a         
    burnt += a         
    a = burnt // b    
    burnt = burnt % b  

print(hours)
