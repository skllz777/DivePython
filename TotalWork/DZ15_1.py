"""
Возьмите любые 1-3 задания из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из командной строки
с передачей параметров.

Задача N4 из 11го домаашнего задания:

"""
import itertools
import logging
import argparse

logging.basicConfig(level=logging.INFO)


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"

    def __eq__(self, other):
        return self.data == other.data

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            logging.error("Matrix dimensions do not match for addition.")
            raise ValueError("Matrices have different dimensions!")
        result = Matrix(self.rows, self.cols)
        for i, j in itertools.product(range(self.rows), range(self.cols)):
            result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            logging.error(
                "Number of columns in the first matrix is not equal to the number of rows in the second matrix."
            )
            raise ValueError(
                "Number of columns in the first matrix is not equal to the number of rows in the second matrix!"
            )
        result = Matrix(self.rows, other.cols)
        for i, j in itertools.product(range(self.rows), range(other.cols)):
            for k in range(self.cols):
                result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result


def main():
    parser = argparse.ArgumentParser(description="Matrix Operations")
    parser.add_argument("operation", choices=["add", "multiply"], help="Matrix operation to perform")
    parser.add_argument("matrix1_rows", type=int, help="Number of rows in the first matrix")
    parser.add_argument("matrix1_cols", type=int, help="Number of columns in the first matrix")
    parser.add_argument("matrix2_rows", type=int, help="Number of rows in the second matrix")
    parser.add_argument("matrix2_cols", type=int, help="Number of columns in the second matrix")

    args = parser.parse_args()

    matrix1 = Matrix(args.matrix1_rows, args.matrix1_cols)
    matrix2 = Matrix(args.matrix2_rows, args.matrix2_cols)

    if args.operation == "add":
        try:
            result = matrix1 + matrix2
            print("Result of addition:")
            print(result)
        except ValueError as e:
            print(f"Error: {e}")
    elif args.operation == "multiply":
        try:
            result = matrix1 * matrix2
            print("Result of multiplication:")
            print(result)
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # Example 1: Matrix Addition
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]

    matrix2 = Matrix(2, 3)
    matrix2.data = [[7, 8, 9], [10, 11, 12]]

    result_addition = matrix1 + matrix2
    print("Result of addition:")
    print(result_addition)

    # Example 2: Matrix Multiplication
    matrix3 = Matrix(3, 2)
    matrix3.data = [[1, 2], [3, 4], [5, 6]]

    matrix4 = Matrix(2, 4)
    matrix4.data = [[7, 8, 9, 10], [11, 12, 13, 14]]

    result_multiplication = matrix3 * matrix4
    print("\nResult of multiplication:")
    print(result_multiplication)


# Из командной строки
# python DZ15_1.py add 2 3 2 3
# python DZ15_1.py multiply 3 2 2 4