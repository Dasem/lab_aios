import time


def parse():
    file = open('input.txt', 'r')
    rows = file.readlines()
    result_matrix = []
    for row in rows:
        new_row = row.split('\t')
        new_row[-1] = new_row[-1].strip()
        result_matrix.append(new_row)
    for i in range(len(result_matrix)):
        for j in range(len(result_matrix)):
            result_matrix[j][i] = result_matrix[i][j] = int(result_matrix[j][i])
    return result_matrix


matrixA = parse()

debug = False

start_time = time.time()


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
        if debug:
            print('Изменение остовного дерева')
            printishe(spanning_tree)
        return True
    else:
        return False


def karaksal(matrix):  # Если получился цикл, отменяем последнее добавление
    while find_min(matrix):
        if is_cycle(true_copy(spanning_tree)):
            rollback()
            if debug:
                print("Алярм, цикл!!1! Откачено до этого состояния:")
                printishe(spanning_tree)
    if debug:
        print("Минимальные вершины закончились")


def rollback():
    spanning_tree[current_min_edge[0]][current_min_edge[1]] = 0
    spanning_tree[current_min_edge[1]][current_min_edge[0]] = 0


def printishe(matrix):
    n = len(matrix)
    for i in range(n):
        print(str(i) + ', ', end='')
    print()
    for i in range(n):
        print(i, end='')
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


# Возвращает результат в список pasted_nodes
def eilerov_cycle_starter(matrix):
    return eilerov_cycle(matrix, 0, [], 0)


def eilerov_cycle(matrix, current_node, edges_history, start_node):  # [[вес, откуда, куда],...]
    global pasted_nodes
    if contains_all(get_list_nodes(matrix), pasted_nodes) and current_node == start_node:
        return
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
                eilerov_cycle(matrix, node, edges_history, start_node)
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

# функция редуцирования эйлерова цикла
def find_kommivoyajer_path(cycle):
    meeted_nodes = []
    for node in cycle:
        if node not in meeted_nodes:
            meeted_nodes.append(node)
    meeted_nodes.append(meeted_nodes[0])
    return meeted_nodes


def length_kommivoyajer_path(matrix, path):
    len_path = len(path)
    summ = 0
    for i in range(len_path - 1):
        summ += matrix[path[i]][path[i + 1]]
    return summ


# MAIN

karaksal(true_copy(matrixA))
if debug:
    print('\n\n\nNOT PRINT BUT PRINT\n\n\n')
    printishe(spanning_tree)

pasted_nodes = [0]
eilerov_cycle_starter(spanning_tree)
cycle = pasted_nodes

if debug:
    print('Эйлеров цикл по остовному дереву, начиная с 0 вершины: ', cycle)

kommivoyajer_path = find_kommivoyajer_path(cycle)
print('Путь коммивояжжера: ', kommivoyajer_path)

print('Длина пути: ', length_kommivoyajer_path(matrixA, kommivoyajer_path))

print('Время выполнения: ', time.time() - start_time)
