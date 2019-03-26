import random

# #Part that belongs to input from txt
# file = open('input.txt', 'r')
#
# row = file.readline().split()
# n = len(row)
# a=[]
# for i in range(len(row)):
#     row[i] = int(row[i])
#
# for i in range(n):
#     for i in range(len(row)):
#         row[i] = int(row[i])
#     a.append(row)
#     row = file.readline().split()
#
# for i in range(n):
#     for j in range(n):
#         print(a[i][j])
# # End of input

a = []
row = []

n = 11
print(n)

for i in range(n):
    for j in range(n):
        # if random.randrange(1, 2) == 1 :
        row.append(random.randrange(1, 9))
    # else:
    #   row.append(0)
    a.append(row)
    row = []

for i in range(n):
    a[i][i] = 0

for i in range(n):
    for j in range(i, n):
        a[i][j] = a[j][i]

for i in range(n):
    print('[', end='')
    for j in range(n):
        if j != n - 1:
            print(str(a[i][j]) + ', ', end='')
        else:
            print(str(a[i][j]), end='')
    if i != n - 1:
        print('],')
    else:
        print(']')
