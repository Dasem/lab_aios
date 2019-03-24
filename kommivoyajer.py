# matrixA = [
#     [0, 8, 3, 0],   # 0
#     [8, 0, 4, 0],   # 1
#     [3, 4, 0, 1],   # 2
#     [0, 0, 1, 0]    # 3
# ]


matrixA = [
    [0, 3, 8, 2, 0, 7],
    [3, 0, 0, 0, 0, 0],
    [8, 0, 0, 1, 4, 0],
    [2, 0, 1, 0, 2, 1],
    [0, 0, 4, 2, 0, 5],
    [7, 0, 0, 1, 5, 0],
]


# =================================================
# acycle functions

# Удалять её из графа в том случае, если из неё исходит меньше двух рёбер
def is_delete_needed(row):
    if 0 not in row:  # Если мы уже удалили вершину, то у неё стоит -1 на пути самой к себе
        return

    edges_count = 0
    for i in range(len(row)):
        if row[i] != -1 and row[i] != 0:
            edges_count = edges_count + 1
    if edges_count < 2:
        return True
    return False


def convert_to_cycle_or_empty_matrix(matrix):
    was_deleted = True
    while was_deleted:
        was_deleted = False
        for row_num in range(len(matrix)):
            if is_delete_needed(matrix[row_num]):
                delete_node(matrix, row_num)
                was_deleted = True


def delete_node(matrix, row_num):
    for i in range(len(matrix)):
        matrix[row_num][i] = -1
        matrix[i][row_num] = -1


def is_cycle(matrix):
    convert_to_cycle_or_empty_matrix(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != -1 and matrix[i][j] != 0:
                return True
    return False


# end of acycle functionsdelete_check
# ========================================
# kara...   functions

def true_copy(a):
    return [row.copy() for row in a]


def find_max(matrix):
    max = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != -1 and matrix[i][j] != 0 and matrix[i][j] > max:
                max = matrix[i][j]
    return max


current_min_edge = [-1, -1]
spanning_tree = [0] * len(matrixA)
for i in range(len(matrixA)):
    spanning_tree[i] = [0] * len(matrixA)

max_value = find_max(matrixA)


def find_min(matrix):
    global current_min_edge
    global spanning_tree
    min = max_value
    coord_i = -1
    coord_j = -1
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != -1 and matrix[i][j] != 0 and matrix[i][j] <= min:
                min = matrix[i][j]
                coord_i = i
                coord_j = j
                current_min_edge = [coord_i, coord_j]
    if coord_i != -1:
        matrix[coord_i][coord_j] = matrix[coord_j][coord_i] = -1
        spanning_tree[coord_i][coord_j] = spanning_tree[coord_j][coord_i] = min
        print('Изменение остовного дерева')
        printishe(spanning_tree)
        return True
    else:
        return False


def karaksal(matrix):  # Если получился цикл, отменяем последнее добавление
    while find_min(matrix):
        if is_cycle(true_copy(spanning_tree)):
            rollback()
            print("Алярм, цикл!!1! Откачено до этого состояния:")
            printishe(spanning_tree)
    print("Минимальные вершины закончились")


def rollback():
    spanning_tree[current_min_edge[0]][current_min_edge[1]] = 0
    spanning_tree[current_min_edge[1]][current_min_edge[0]] = 0


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


def contains_all(list, collection):
    for element in list:
        if element not in collection:
            return False
    return True


def eilerov_cycle_starter(matrix):
    return eilerov_cycle(matrix, 0, [0], [], 0)


def eilerov_cycle(matrix, current_node, pasted_nodes, edges_history, start_node):  # [[вес, откуда, куда],...]
    if contains_all(get_list_nodes(matrix), pasted_nodes) and current_node == start_node:
        return pasted_nodes
    else:
        is_there_path = False
        for node in range(len(matrix)):
            if matrix[current_node][node] <= 0:
                continue
            next_edge = [matrix[current_node][node], current_node, node]
            if matrix[current_node][node] > 0 and next_edge not in edges_history:
                is_there_path = True
                edges_history.append(next_edge)
                pasted_nodes.append(node)
                result = eilerov_cycle(matrix, node, pasted_nodes, edges_history, start_node)
                if result is not None:
                    return result
        if not is_there_path and not contains_all(get_list_nodes(matrix), pasted_nodes):
            rollback_eilerov_cycle(pasted_nodes, edges_history)


def get_list_nodes(matrix):
    return list(range(len(matrix)))


def rollback_eilerov_cycle(pasted_nodes, edges_history):
    pasted_nodes.pop()
    edges_history.pop()


# end of kar functions
# ===========================
#    main


karaksal(true_copy(matrixA))


print('\n\n\nNOT PRINT BUT PRINT\n\n\n')
printishe(spanning_tree)

print('Эйлеров цикл по остовному дереву, начиная с 0 вершины: ', eilerov_cycle_starter(spanning_tree))
