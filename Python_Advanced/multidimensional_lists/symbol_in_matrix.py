n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(input()))

searched_elements = input()
is_found = False

for row_index in range(n):
    if is_found:
        break
    for col_index in range(len(matrix[row_index])):
        if matrix[row_index][col_index] == searched_elements:
            print(f'({row_index}, {col_index})')
            is_found = True
            break

if not is_found:
    print(f"{searched_elements} does not occur in the matrix")