#Part that belongs to input from txt
file = open('INPUT.txt', 'r')

row = file.readline().split()
n = len(row)
a=[]
for i in range(len(row)):
    row[i] = int(row[i])

for i in range(n):
    for i in range(len(row)):
        row[i] = int(row[i])
    a.append(row)
    row = file.readline().split()

for i in range(n):
    for j in range(n):
        print(a[i][j])
# End of input
