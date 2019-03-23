def is_more_than_1_edge(row):
    critical_value = 3
    current_value = 0
    for distance in row:
        if distance != -1:
            current_value += 1
    if current_value >= critical_value:
        return True
    else:
        return False


def delete_node(node, matrix):
    for cell in matrix:
        matrix[cell][node] = -1
        matrix[node][cell] = -1


def find_start_node(matrix):
    for node in range(len(matrix)):
        if matrix[node][node] != -1:
            return node
    return -1


# ================================================

# -1
def delete_check(row):
    current_nodes = 0
    for i in range(len(row)):
        if row[i] != -1 and row[i] != 0:
            current_nodes = current_nodes + 1
    if current_nodes == 2:
        return -1
    return 1


def kar(matrix):
    for row_num in range(len(matrix)):
        if delete_check(matrix[row_num]) == -1:
           for i in range(len(matrix)):
               matrix[row_num][i] = -1
