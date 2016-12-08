import re

with open('Day8.in', 'r') as f:
    data = f.readlines()

mat = [["." for i in range(50)] for j in range(6)]

def swap(m, i1, j1, i2, j2):
    m[i1][j1], m[i2][j2] = m[i2][j2], m[i1][j1]

def rect(m, x, y, val=1):
    for i in range(0, y):
        for j in range(0, x):
            m[i][j] = val

def shift(m, x=0, column=True, dir=1):
    i = x
    size = len(m) if column else len(m[i])

    if dir == 1:
        for j in range(size-1, -1, -1):
            if j > 0:
                if column:
                    swap(m, j, i, j-1, i)
                else:
                    swap(m, i, j, i, j-1)
    else:
        for j in range(0, size):
            if j < size-1:
                if column:
                    swap(m, j, i, j-1, i)
                else:
                    swap(m, i, j, i, j+1)

def print_matrix(m):
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            print(mat[i][j], end="")
        print()

for line in data:
    command = line.split()
    if command[0] == "rect":
        params = command[1].split("x")
        x = int(params[0])
        y = int(params[1])
        rect(mat, x, y, "#")
    elif command[0] == "rotate":
        amount = int(command[-1])
        column = command[1] == "column"
        index = int(command[2].split("=")[1])
        for i in range(0, amount):
            shift(mat, index, column, 1)

c = [mat[i].count("#") for i in range(len(mat))]
print(sum(c))
print_matrix(mat)