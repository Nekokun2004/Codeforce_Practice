n = int(input())
XTotal = 0
for i in range(n):
    x = int(input())
    XTotal += x
print(XTotal)
Xafter = (XTotal // ((10**9)+7) ) + 1
print(Xafter*((10**9)+7)-XTotal)