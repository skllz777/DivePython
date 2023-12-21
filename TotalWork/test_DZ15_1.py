import pytest
from DZ15_1 import Matrix


# tests
@pytest.mark.parametrize(
    "matrix1_data, matrix2_data, expected_data, test_id",
    [
        ([[1, 2], [3, 4]], [[5, 6], [7, 8]], [[6, 8], [10, 12]], "addition_simple"),
        ([[1]], [[2]], [[3]], "addition_single_element"),
        ([[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[8, 10, 12], [14, 16, 18]], "addition_3x2"),
    ],
)
def test_matrix_addition(matrix1_data, matrix2_data, expected_data, test_id):
    matrix1 = Matrix(len(matrix1_data), len(matrix1_data[0]))
    matrix1.data = matrix1_data
    matrix2 = Matrix(len(matrix2_data), len(matrix2_data[0]))
    matrix2.data = matrix2_data
    expected_matrix = Matrix(len(expected_data), len(expected_data[0]))
    expected_matrix.data = expected_data

    result_matrix = matrix1 + matrix2

    assert result_matrix == expected_matrix, f"Failed test_id: {test_id}"


# Edge cases
@pytest.mark.parametrize(
    "matrix1_data, matrix2_data, test_id",
    [
        ([[0, 0], [0, 0]], [[0, 0], [0, 0]], "addition_zero_matrices"),
    ],
)
def test_matrix_addition_edge_cases(matrix1_data, matrix2_data, test_id):
    matrix1 = Matrix(len(matrix1_data), len(matrix1_data[0]))
    matrix1.data = matrix1_data
    matrix2 = Matrix(len(matrix2_data), len(matrix2_data[0]))
    matrix2.data = matrix2_data

    result_matrix = matrix1 + matrix2

    assert result_matrix.data == matrix1_data, f"Failed test_id: {test_id}"


# Error cases for addition
@pytest.mark.parametrize(
    "matrix1_data, matrix2_data, test_id",
    [
        ([[1, 2]], [[3, 4, 5]], "addition_mismatched_dimensions"),
    ],
)
def test_matrix_addition_error_cases(matrix1_data, matrix2_data, test_id):
    matrix1 = Matrix(len(matrix1_data), len(matrix1_data[0]))
    matrix1.data = matrix1_data
    matrix2 = Matrix(len(matrix2_data), len(matrix2_data[0]))
    matrix2.data = matrix2_data

    with pytest.raises(ValueError):
        _ = matrix1 + matrix2


# tests for multiplication
@pytest.mark.parametrize(
    "matrix1_data, matrix2_data, expected_data, test_id",
    [
        ([[1, 2], [3, 4]], [[2, 0], [1, 2]], [[4, 4], [10, 8]], "multiplication_simple"),
        ([[1]], [[2]], [[2]], "multiplication_single_element"),
    ],
)
def test_matrix_multiplication(matrix1_data, matrix2_data, expected_data, test_id):
    matrix1 = Matrix(len(matrix1_data), len(matrix1_data[0]))
    matrix1.data = matrix1_data
    matrix2 = Matrix(len(matrix2_data), len(matrix2_data[0]))
    matrix2.data = matrix2_data
    expected_matrix = Matrix(len(expected_data), len(expected_data[0]))
    expected_matrix.data = expected_data

    result_matrix = matrix1 * matrix2

    assert result_matrix == expected_matrix, f"Failed test_id: {test_id}"


# Error cases for multiplication
@pytest.mark.parametrize(
    "matrix1_data, matrix2_data, test_id",
    [
        ([[1, 2]], [[3], [4], [5]], "multiplication_mismatched_dimensions"),
    ],
)
def test_matrix_multiplication_error_cases(matrix1_data, matrix2_data, test_id):
    matrix1 = Matrix(len(matrix1_data), len(matrix1_data[0]))
    matrix1.data = matrix1_data
    matrix2 = Matrix(len(matrix2_data), len(matrix2_data[0]))
    matrix2.data = matrix2_data

    with pytest.raises(ValueError):
        _ = matrix1 * matrix2


if __name__ == "__main__":
    pytest.main([f"{__file__}", "-v"])