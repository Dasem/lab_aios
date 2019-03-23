matrix = [[0, 4, 4, 2, 2],
          [4, 0, 5, 5, 3],
          [4, 5, 0, 3, 2],
          [2, 5, 3, 0, 2],
          [2, 3, 2, 2, 0]]

result = -1


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
                return False
    return True


# end of acycle functions
# ========================================
# kara...   functions

def find_max(matrix):
    max = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != -1 and matrix[i][j] != 0 and matrix[i][j] > max:
                max = matrix[i][j]
    return max


min_edge = matrixA.copy()
max_value = find_max(matrixA)


def find_min(matrix):
    global min_edge
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
        min_edge[coord_i][coord_j] = -1
        return True
    else:
        return False


def kar(matrix):
    while find_min(matrix):
        if is_cycle(matrix):
            print('KARAMBA!')


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


#komm(0, [0], 0)
print(result)

kar(min_edge)

printishe(matrixA)

print('\n\n\nNOT PRINT BUT PRINT\n\n\n')
printishe(min_edge)

