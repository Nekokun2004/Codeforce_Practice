t = int(input())

for _ in range(t):
    n, m, q = map(int, input().split())
    t1, t2 = map(int, input().split())
    david_position = int(input())
    if t1 > t2:
        t1, t2 = t2, t1
    if t1 < david_position < t2:
        steps = min(abs(david_position-t1),abs(t2-david_position))
        if ((t1+t2) //2) >  david_position:
            steps += 1
        print(steps)
    elif david_position < t1:
        steps = t1 - 1 
        print(steps)
    elif t1 - david_position == 2:
        print(2)
    elif david_position > t2:  
        steps = n - t2 
        print(steps)

# t = int(input())

# for _ in range(t):
#     n, m, q = map(int, input().split())
#     t1, t2 = map(int, input().split())
#     david_position = int(input())
#     if david_position < min(t1,t2):
#         steps = min(t1,t2) - 1 
#         print(steps)
#     else:
#         if david_position > max(t1,t2):  
#             steps = n - max(t1,t2)
#             print(steps)
#         else:
#             steps = abs(t2-t1)//2
#             print(steps)

        

