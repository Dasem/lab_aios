matrixA = [

    [0, 8, 3, 0],
    [8, 0, 4, 0],
    [3, 4, 0, 1],
    [0, 0, 1, 0]
]

# =================================================
# acycle functions

def delete_check(row):
    current_nodes = 0
    for i in range(len(row)):
        if row[i] != -1 and row[i] != 0:
            current_nodes = current_nodes + 1
    if current_nodes == 2:
        return -1
    return 1


def acycle(matrix):
    was_deleted = True
    while was_deleted:
        was_deleted = False
        for row_num in range(len(matrix)):
            if delete_check(matrix[row_num]) == -1:
                for i in range(len(matrix)):
                    matrix[row_num][i] = -1
                    matrix[i][row_num] = -1
                was_deleted = True


def is_cycle(matrix):
    acycle(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][i] != -1 and matrix[i][i] != 0:
                return True
    return False


# end of acycle functions
# ========================================
# kara...   functions

def true_copy(a):
    result = []
    for row in a:
        result.append(row.copy())
    return result


def find_max(matrix):
    max = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != -1 and matrix[i][j] != 0 and matrix[i][j] > max:
                max = matrix[i][j]
    return max


copy = true_copy(matrixA)
ostovnoe_derevo = true_copy(matrixA)
for i in range(len(ostovnoe_derevo)):
    for j in range(len(ostovnoe_derevo)):
        ostovnoe_derevo[i][j] = 0

max_value = find_max(copy)


def find_min(matrix):
    global ostovnoe_derevo
    min = max_value
    coord_i = -1
    coord_j = -1
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != -1 and matrix[i][j] != 0 and matrix[i][j] < min:
                min = matrix[i][j]
                coord_i = i
                coord_j = j
    if coord_i != -1:
        copy[coord_i][coord_j] = copy[coord_j][coord_i] = -1
        ostovnoe_derevo[coord_i][coord_j] = ostovnoe_derevo[coord_j][coord_i] = min
        print('Изменение остовного дерева')
        printishe(ostovnoe_derevo)
        return True
    else:
        return False


def karaksal(matrix):
    while find_min(matrix):
        print('********')
        printishe(ostovnoe_derevo)
        print('********')
        if is_cycle(true_copy(ostovnoe_derevo)):
            print('\n\n\n\nKARAMBA!')
            # ОТКАТ ПОСЛЕДНЕГО ДЕЙСТВИЯ
            return 0


def printishe(matrix):
    n = len(matrix)
    for i in range(n):
        print('[', end='')
        for j in range(n):
            if j != n - 1:
                print(str(matrix[i][j]) + ', ', end='')
            else:
                print(str(matrix[i][j]), end='')
        if i != n - 1:
            print('],')
        else:
            print(']')


# end of kar functions
# ===========================
#    main


karaksal(copy)

print('\n\n\nNOT PRINT BUT PRINT\n\n\n')
printishe(ostovnoe_derevo)
