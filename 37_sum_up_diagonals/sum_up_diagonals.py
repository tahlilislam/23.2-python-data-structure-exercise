def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    # 2 diagnoals from left to right bottom and right top to left bottom

    daigonal1_sum = 0
    daigonal2_sum = 0

    for i in range(len(matrix)):
        # Add elements of the top-left to bottom-right diagonal
        daigonal1_sum += matrix[i][i]

        daigonal2_sum+= matrix[i][len(matrix)-1-i]

    return daigonal1_sum + daigonal2_sum
