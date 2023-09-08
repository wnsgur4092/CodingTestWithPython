input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

print(row, column)

steps = [(-2, -1), (-2, 1), (2,-1), (2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2)]

result = 0

for step in steps:
    next_row = row + step[0]
    print("next_row is:", next_row)

    next_column = column + step[1]
    print("next_column is:", next_column)

    if next_row >= 1 and next_row <=8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)