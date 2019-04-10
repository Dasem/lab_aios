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
            result_matrix[j][i] = result_matrix[i][j]
    return result_matrix
