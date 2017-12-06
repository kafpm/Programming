#A = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

def input_matrix():
    m = int(input('m = ')); n = int(input('n = '))
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            prompt = 'M[{}][{}] = '.format(i, j)
            value = int(input(prompt))
            row.append(value)
        matrix.append(row)
    return matrix

def random_matrix():
    from random import randrange
    m = int(input('m = ')); n = int(input('n = '))
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            value = randrange(-10, 10)
            prompt = 'M[{}][{}] = {}'.format(i, j, value)
            print(prompt)
            row.append(value)
        matrix.append(row)
    return matrix

def to_string(matrix):
    out = '[\n'; m = len(matrix); n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            out += '{:3d} '.format(A[i][j])
        out += '\n'
    out += ']'
    return out

A = random_matrix()
print(to_string(A))
