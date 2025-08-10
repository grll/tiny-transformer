def matmul(
    A: list[list[float | int]], B: list[list[float | int]]
) -> list[list[float | int]]:
    C = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            C[i][j] = sum(
                [a_i * b_j for a_i, b_j in zip(A[i], [b_row[j] for b_row in B])]
            )
    return C


if __name__ == "__main__":
    A = [[1, 2], [3, 4]]

    B = [[1, 2], [3, 4]]

    C = [[7, 10], [15, 22]]

    assert matmul(A, B) == C

    A = [[1], [3]]

    B = [[1, 2]]

    C = [[1, 2], [3, 6]]

    assert matmul(A, B) == C

    A = [[1], [3]]

    B = [[1]]

    C = [[1], [3]]

    assert matmul(A, B) == C
