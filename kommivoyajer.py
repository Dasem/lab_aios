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
            print(new_pasted)
            komm(sum_nodes + matrix[current_node][next_node],
                 new_pasted,
                 next_node)


komm(0, [0], 0)
print(result)
