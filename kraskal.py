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

