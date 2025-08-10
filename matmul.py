from typing import overload


@overload
def matmul(A: list[list[int]], B: list[list[int]]) -> list[list[int]]: ...


@overload
def matmul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]: ...


@overload
def matmul(A: list[list[int]], B: list[list[float]]) -> list[list[float]]: ...


@overload
def matmul(A: list[list[float]], B: list[list[int]]) -> list[list[float]]: ...


def matmul(
    A: list[list[float]] | list[list[int]], B: list[list[float]] | list[list[int]]
) -> list[list[float]] | list[list[int]]:
    C: list[list[float]] | list[list[int]] = [
        [0] * len(B[0]) for _ in range(len(A))
    ]
    for i in range(len(A)):
        for j in range(len(B[0])):
            C[i][j] = sum(
                a_i * b_j for a_i, b_j in zip(A[i], (b_row[j] for b_row in B)) # type: ignore[misc]
            )
    return C


if __name__ == "__main__":
    A_int = [[1], [3]]
    B_int = [[1, 2]]
    C_int = matmul(A_int, B_int)
    assert C_int == [[1, 2], [3, 6]]

    A_int = [[1], [3]]
    B_int = [[1]]
    C_int = matmul(A_int, B_int)
    assert C_int == [[1], [3]]

    # Test float × float = float
    A_float = [[1.0, 2.0], [3.0, 4.0]]
    B_float = [[1.0, 2.0], [3.0, 4.0]]
    C_float = matmul(A_float, B_float)
    assert C_float == [[7.0, 10.0], [15.0, 22.0]]

    # Test int × float = float
    A_int = [[1, 2], [3, 4]]
    B_float = [[1.0, 2.0], [3.0, 4.0]]
    C_float = matmul(A_int, B_float)
    assert C_float == [[7.0, 10.0], [15.0, 22.0]]
