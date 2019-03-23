matrix = [[0, 4, 4, 2, 2],
          [4, 0, 5, 5, 3],
          [4, 5, 0, 3, 2],
          [2, 5, 3, 0, 2],
          [2, 3, 2, 2, 0]]

result = -1


def komm(sum_nodes, pasted, current_node):
    global result
    if len(pasted) == len(matrix):
        # print(sum_nodes)
        if result == -1 or result > sum_nodes:
            result = sum_nodes
        return
    for next_node in range(len(matrix)):
        if next_node not in pasted:
            new_pasted = pasted.copy()
            new_pasted.append(next_node)
            # print(new_pasted)
            komm(sum_nodes + matrix[current_node][next_node],
                 new_pasted,
                 next_node)


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
    was_deleted = 1
    while was_deleted == 1:
        was_deleted = 0
        for row_num in range(len(matrix)):
            if delete_check(matrix[row_num]) == -1:
                for i in range(len(matrix)):
                    matrix[row_num][i] = -1
                    matrix[i][row_num] = -1
                was_deleted = 1


# end of acycle functions
# ========================================
# kara...   functions

def find_max(matrix):
    max = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][i] != -1 and matrix[i][i] != 0 and matrix[i][i] > max:
                max = matrix[i][i]
    return max


min_edge = []
max_value = find_max(matrix)


def find_min(matrix):
    global min_edge
    min = max_value
    coord_i = -1
    coord_j = -1
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][i] != -1 and matrix[i][i] != 0 and matrix[i][i] < min:
                min = matrix[i][i]
                coord_i = i
                coord_j = j
    if coord_i!=-1:
        min_edge.append([min,coord_i,coord_j])
        matrix[coord_i][coord_j]= -1
        return 1
    else:
        return -1

def is_a_cycle(edge_list):



def kar(matrix):
    not_cycle = 1
    while(find_min(matrix)==1 and  )



# end of kar functions
# ===========================
#    main

komm(0, [0], 0)
print(result)

acycle(matrix)

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
