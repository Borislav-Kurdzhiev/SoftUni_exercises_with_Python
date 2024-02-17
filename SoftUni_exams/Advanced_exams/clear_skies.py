def initialize_matrix(size):
    matrix = [['' for _ in range(size)] for _ in range(size)]
    pos_row, pos_col = -1, -1
    enemies, repair_points = 0, 0

    for row in range(size):
        matrix_info = input()
        for col in range(size):
            matrix[row][col] = matrix_info[col]
            if matrix[row][col] == 'J':
                pos_row, pos_col = row, col
                matrix[row][col] = '-'
            if matrix[row][col] == 'E':
                enemies += 1
            if matrix[row][col] == 'R':
                repair_points += 1

    return matrix, pos_row, pos_col, enemies, repair_points


def move_jetfighter(matrix, pos_row, pos_col, jetfighter_armor, enemies):
    killed_enemies = 0

    while True:
        command = input()

        if command == "up":
            pos_row -= 1
        elif command == "down":
            pos_row += 1
        elif command == "left":
            pos_col -= 1
        elif command == "right":
            pos_col += 1

        if matrix[pos_row][pos_col] == '-':
            continue
        elif matrix[pos_row][pos_col] == 'R':
            jetfighter_armor = 300
            matrix[pos_row][pos_col] = '-'
        elif matrix[pos_row][pos_col] == 'E':
            killed_enemies += 1
            enemies -= 1
            matrix[pos_row][pos_col] = '-'
            if enemies > 0:
                jetfighter_armor -= 100
                if jetfighter_armor == 0:
                    matrix[pos_row][pos_col] = 'J'
                    return jetfighter_armor, killed_enemies, pos_row, pos_col, True
            elif enemies == 0:
                matrix[pos_row][pos_col] = 'J'
                return jetfighter_armor, killed_enemies, pos_row, pos_col, False


size = int(input())
matrix, pos_row, pos_col, enemies, repair_points = initialize_matrix(size)
jetfighter_armor, killed_enemies, pos_row, pos_col, mission_accomplished = move_jetfighter(
    matrix, pos_row, pos_col, 300, enemies)

if mission_accomplished:
    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{pos_row}, {pos_col}]!")
else:
    print("Mission accomplished, you neutralized the aerial threat!")

for row in matrix:
    print(''.join(row))
