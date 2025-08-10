def transpose[T: (int, float)](A: list[list[T]]) -> list[list[T]]:
    rows, cols = len(A), len(A[0])
    C: list[list[T]] = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            C[j][i] = A[i][j]
    return C


if __name__ == "__main__":
    A = [[1, 2], [3, 4]]

    A_t = [[1, 3], [2, 4]]

    assert transpose(A) == A_t

    A = [[1, 2]]

    A_t = [[1], [2]]

    assert transpose(A) == A_t

    assert transpose(transpose(A)) == A
