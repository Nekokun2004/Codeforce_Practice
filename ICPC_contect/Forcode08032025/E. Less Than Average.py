import sys

data = sys.stdin.readlines()
# print(data)
all_numbers = [int(x) for line in data for x in line.strip().split()]
first_value = all_numbers[0]
rest_values = all_numbers[1:]
if len(rest_values) > first_value:
    rest_values = rest_values[:first_value+1]
average = sum(rest_values) // len(rest_values)
# print(average)
x = [x for x in rest_values if x < average]
print(len(x))