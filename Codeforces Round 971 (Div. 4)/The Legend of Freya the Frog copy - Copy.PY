t = int(input())
for i in range(t):
    x, y, k = map(int, input().split())
    
    # Calculate the minimum moves needed for x and y
    a = (x + k - 1) // k  # Equivalent to math.ceil(x / k)
    b = (y + k - 1) // k  # Equivalent to math.ceil(y / k)
    
    # Determine the total moves
    if a >= b:
        result = 2 * a - 1
    else:
        result = 2 * b
    
    # Print the result for the current test case
    print(result)
