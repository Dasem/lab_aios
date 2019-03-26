import time

matrix = [
    [0, 5, 6, 5, 3, 8, 6, 2, 1, 6, 3],
    [5, 0, 5, 6, 2, 3, 8, 8, 3, 7, 2],
    [6, 5, 0, 6, 2, 3, 7, 2, 2, 2, 3],
    [5, 6, 6, 0, 4, 1, 2, 5, 5, 8, 5],
    [3, 2, 2, 4, 0, 4, 7, 8, 5, 1, 5],
    [8, 3, 3, 1, 4, 0, 4, 5, 7, 7, 5],
    [6, 8, 7, 2, 7, 4, 0, 2, 8, 2, 6],
    [2, 8, 2, 5, 8, 5, 2, 0, 4, 4, 6],
    [1, 3, 2, 5, 5, 7, 8, 4, 0, 6, 6],
    [6, 7, 2, 8, 1, 7, 2, 4, 6, 0, 4],
    [3, 2, 3, 5, 5, 5, 6, 6, 6, 4, 0]
]

result = -1

start_time = time.time()


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


komm(0, [0], 0)
print(result)

print('Время выполнения: ', time.time() - start_time)
