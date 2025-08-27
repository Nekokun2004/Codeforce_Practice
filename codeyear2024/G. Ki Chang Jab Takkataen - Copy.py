N,M,H,Q = [int(x) for x in input().split()]
Mbox = []
Nbox = []
col = []
for i in range(N):
    x,y = [int(x) for x in input('ตำแหน่ง =').split()]
    Nbox.append((x,y))
while len(Mbox) < M:
    m =  [int(x) for x in input('ความยาวตาข่าย =').split()]
    Mbox.extend(m)
for _ in range(Q):
    q = [int(x) for x in input('quition =').split()]

Mbox.sort()
for i in range(len(Nbox)):
    x, y = Nbox[i]  # x, y coordinates of the box
    if i < len(Mbox):  # Ensure we're within bounds
        if H + Mbox[i] > y:
            print(f"Box at position {x} meets the condition")
        
 
    

