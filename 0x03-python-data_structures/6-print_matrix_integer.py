#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
if len(matrix) == 0:
print()
return
for row in matrix:
print(' '.join('{:d}'.format(j) for j in row))
