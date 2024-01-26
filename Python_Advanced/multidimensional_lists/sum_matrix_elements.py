row, col = [int(el) for el in input().split(',')]

matrix = []
total = 0

for i in range(row):
    row_data = [int(el) for el in input().split(',')]
    total += sum(row_data)
    matrix.append(row_data)
print(total)
print(matrix)