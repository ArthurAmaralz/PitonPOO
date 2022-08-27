def mult_matriz(a, b):
    num_lin_a, num_col_a = len(a), len(a[0])
    num_lin_b, num_col_b = len(b), len(b[0])
    assert num_col_a == num_lin_b

    c = []
    for i in range(num_lin_a):
        c.append([])  # add uma nova linha
        for j in range(num_col_b):
            c[i].append(0)  # Um nova coluna dentro da linha
            for l in range(num_col_a):
                c[i][j] += a[i][l] * b[l][j]  # faz a operação entre as matrizes
    return c


a = [[1, 2, 3], [4, 5, 6]]
b = [[7, 8], [10, 11], [12, 13]]
print(mult_matriz(a, b))
