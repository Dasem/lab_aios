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


matrix = parse()

result = -1
path = []

start_time = time.time()


def komm(sum_nodes, pasted, current_node):
    global result
    global path
    if len(pasted) == len(matrix):
        # print(sum_nodes)
        pasted.append(0)
        sum_nodes += matrix[current_node][0]
        if result == -1 or result > sum_nodes:
            result = sum_nodes
            path = pasted
        return
    for next_node in range(len(matrix)):
        if next_node not in pasted:
            new_pasted = pasted.copy()
            new_pasted.append(next_node)
            # print(new_pasted)
            komm(sum_nodes + matrix[current_node][next_node],
                 new_pasted,
                 next_node)


komm(0, [0], 0)
print('Путь коммивояжжера: ', path)
print(result)

print('Время выполнения: ', time.time() - start_time)
