def matrix_multiply(A, B):
    """
    Multiplies two matrices A and B.
    Args:
        A: List of lists, where each sublist is a row of matrix A.
        B: List of lists, where each sublist is a row of matrix B.
    Returns:
        Resultant matrix as a list of lists.
    Raises:
        ValueError: If matrices cannot be multiplied due to incompatible dimensions.
    """
    # Number of columns in A must be equal to number of rows in B
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal number of rows in B.")

    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(B)):
                sum += A[i][k] * B[k][j]
            row.append(sum)
        result.append(row)
    return result

# Example usage:
if __name__ == "__main__":
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    B = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]
    result = matrix_multiply(A, B)
    for row in result:
        print(row)