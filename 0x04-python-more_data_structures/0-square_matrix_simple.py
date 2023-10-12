#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return []
    # Create a new matrix with the same size as the input matrix.
    new_matrix = []

    for row in matrix:
        new_row = []  # Create a new row for the new matrix.
        for value in row:
            new_row.append(value * value)  # Compute the square of each value and add it to the new row.
        new_matrix.append(new_row)  # Add the new row to the new matrix.

    return new_matrix
