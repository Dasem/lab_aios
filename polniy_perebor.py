import time

matrix = [
    [0, 80, 160, 172, 201, 144, 120, 60, 72, 100, 135],
    [80, 0, 80, 100, 144, 120, 144, 100, 72, 60, 72],
    [160, 80, 0, 60, 120, 144, 201, 172, 135, 100, 72],
    [172, 100, 60, 0, 60, 100, 172, 160, 120, 80, 40],
    [201, 144, 120, 60, 0, 80, 160, 172, 135, 100, 72],
    [144, 120, 144, 100, 80, 0, 80, 100, 72, 60, 72],
    [120, 144, 201, 172, 160, 80, 0, 60, 72, 100, 135],
    [60, 100, 172, 160, 172, 100, 60, 0, 40, 80, 120],
    [72, 72, 135, 120, 135, 72, 72, 40, 0, 40, 80],
    [100, 60, 100, 80, 100, 60, 100, 80, 40, 0, 40],
    [135, 72, 72, 40, 72, 72, 135, 120, 80, 40, 0]
]

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
