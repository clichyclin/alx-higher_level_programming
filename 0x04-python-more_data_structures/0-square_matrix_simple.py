#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
n_matrix = []

for row in matrix:
n_matrix.append(list(map(lambda row: row**2, row)))
return (n_matrix)
