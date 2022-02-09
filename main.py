class Matrix:
    """
To perform basic Matrix operations
Matrix(<nested list>) To get started.
    """

    def __init__(self, matrix: list):
        """ Defining few things! """
        self.matrix = matrix
        self.row = len(matrix)

        for i in self.matrix:
            _col = len(self.matrix[0])
            col = len(i)
            if col != _col:
                raise Exception('Not a valid matrix, inconsistent columns')
        self.column = len(self.matrix[0])
        self.order = f'{self.row}x{self.column}'

    def __repr__(self):
        """ Nothing fancy here! """
        return str(self.matrix)

    def __add__(self, matrix: list):
        """
Adds two matrix objects
Params -> Matrix Objects only!
Retruns -> A Matrix Onject!
        """
        if self.order != matrix.order:
            raise Exception(f'Expected order {self.order} got {matrix.order}')
        else:
            new_matrix = []
            for i in range(self.row):
                _col = []
                for j in range(self.column):
                    _col.append(self.matrix[i][j] + matrix.matrix[i][j])
                new_matrix.append(_col)
            return Matrix(new_matrix)

    def __sub__(self, matrix: list):
        """
Subtracts two matrix objects
Params -> Matrix Objects only!
Retruns -> A Matrix Onject
        """
        if self.order != matrix.order:
            raise Exception(f'Expected order {self.order} for {matrix.order}')
        else:
            new_matrix = []
            for i in range(self.row):
                _col = []
                for j in range(self.column):
                    _col.append(self.matrix[i][j] - matrix.matrix[i][j])
                new_matrix.append(_col)
            return Matrix(new_matrix)

    def __mul__(self, matrix: list):
        """
Multiplying two matrix objects
Params -> Matrix objects only!
Return -> A Matrix Object
        """
        if self.order[2] != matrix.order[0]:
            raise Exception(f'Cannot multiply these matrices!')
        else:
            new_matrix = [[0 for _ in range(matrix.column)] for _ in range(self.row)]
            for i in range(self.row):
                _col = []
                for j in range(matrix.column):
                    for k in range(matrix.row):
                        new_matrix[i][j] += self.matrix[i][k] * matrix.matrix[k][j]
            return Matrix(new_matrix)

    def __truediv__(self, matrix: list):
        """
Dividing two matrix objects
Params -> Matrix objects only!
Return -> A Matrix Object
        """
        if self.order[2] != matrix.order[0]:
            raise Exception('Cannot divide these matrices!')
        else:
            new_matrix = [[0 for _ in range(matrix.column)] for _ in range(self.row)]
            matrix.matrix = [[round(1 / matrix.matrix[i][j], 1) for j in range(matrix.column)] for i in
                             range(matrix.row)]
            for i in range(self.row):
                _col = []
                for j in range(matrix.column):
                    for k in range(matrix.row):
                        new_matrix[i][j] += self.matrix[i][k] * matrix.matrix[k][j]

            new_matrix = [[round(new_matrix[i][j], 1) for j in range(matrix.column)] for i in range(self.row)]

            return Matrix(new_matrix)

    def __floordiv__(self, matrix: list):
        """
Floor Division of two matrix objects
Params -> Matrix Objects only!
Returns -> A Matrux Object
        """
        if self.order[2] != matrix.order[0]:
            raise Exception('Cannot divide these matrices!')
        else:
            new_matrix = [[0 for _ in range(matrix.column)] for _ in range(self.row)]
            matrix.matrix = [[round(1 // matrix.matrix[i][j], 1) for j in range(matrix.column)] for i in
                             range(matrix.row)]
            for i in range(self.row):
                _col = []
                for j in range(matrix.column):
                    for k in range(matrix.row):
                        new_matrix[i][j] += self.matrix[i][k] * matrix.matrix[k][j]

            new_matrix = [[round(new_matrix[i][j], 1) for j in range(matrix.column)] for i in range(self.row)]

            return Matrix(new_matrix)

    def __len__(self) -> int:
        """
Returns number elements present in the matrix!
        """
        return self.row * self.column

    def __iter__(self):
        """
Returns all rows of the matrix
        """
        for i in self.matrix:
            yield i

    def determinant(self) -> float:
        """
Get Determinant of matrix objects
        """
        if self.row != self.column:
            raise Exception('Cannot get determinant of this matrix! Must be a square Matrix')
        else:
            for i in range(self.row - 1):
                _col = []
                for j in range(self.column):
                    _col.append(self.matrix[i][j])
                self.matrix.append(_col)

            add_pointers = [(i, i) for i in range(self.row)]
            det = 0
            for pointer in range(self.row):
                temp = 1
                for tup in add_pointers:
                    i, j = tup
                    temp *= self.matrix[i + pointer][j]
                det += temp

            sub_pointers = [((self.row - 1) - i, 0 + i) for i in range(self.row)]
            for pointers in range(self.row):
                temp = 1
                for tup in sub_pointers:
                    i, j = tup
                    temp *= self.matrix[i + pointers][j]
                det -= temp
        return det

    def count(self, element: int=None):
        """
Counts occurences of elements
Params -> interger, must be present in matrix
Returns -> Dict
        """
        if element is not None:
            count = sum(i.count(element) for i in self.matrix)
            return count

        else:
            count = {}
            for i in self.matrix:
                for j in i:
                    if j not in count:
                        count[j] = 0
                    count[j] += 1
            return count


if __name__ == '__main__':
    from random import randint

    matrix1 = Matrix([[randint(1, 2) for i in range(3)] for i in range(3)])
    print(matrix1)
    print(*matrix1)
    print(matrix1.count())
    print(matrix1.determinant())
