from __future__ import annotations
from random import randint


class Matrix:
    """
    To perform basic Matrix operations
    Matrix(<nested list>) To get started.

    Parameters
    ----------
    matrix : list

    Example
    ---------
    >>> _matrix = [[1, 2, 3], [4, 5, 6]]
    >>> _matrix = Matrix(_matrix)
    >>> _matrix
    [[1, 2, 3], [4, 5, 6]]
    >>> _matrix.row
    2
    >>> _matrix.column
    3
    >>> _matrix.order
    '2x3'
    """

    def __init__(
            self,
            matrix: list[list[int | float]]
    ) -> None:
        """
        Initializes the matrix object
        """
        self.matrix = matrix
        self.row = len(matrix)
        self.column = len(matrix[0])
        self.order = f'{self.row}x{self.column}'

    @property
    def matrix(self):
        return self._matrix
    
    @matrix.setter
    def matrix(self, _matrix):
        """
        This is going to do two checks
        1. if matrix contains anything other than int/floats
        2. if the matrix is consistent i.e it can't be represented as nxm
        """

        for i in _matrix:
            for j in i:
                if not isinstance(j, int | float):
                    raise ValueError('Unsupported type, use only int/float')
       
        _col = len(_matrix[0])
        for i in _matrix:
            if _col != len(i):
                raise ValueError('Inconsistent columns!')
        self._matrix = _matrix
    
    def __repr__(self) -> str:
        """ String Instance """
        return str(self.matrix)

    def __add__(self, matrix: Matrix) -> Matrix:
        """
        Adds two _matrix objects

        Parameters
        ----------
        matrix : Matrix object

        Returns
        -------
        Matrix object

        Example
        -------
        >>> _matrix = [[1, 2, 3], [4, 5, 6]]
        >>> _matrix = Matrix(_matrix)
        >>> matrix1 = [[1, 2, 3], [4, 5, 6]]
        >>> matrix1 = Matrix(matrix1)
        >>> _matrix + matrix1
        [[2, 4, 6], [8, 10, 12]]

        """
        if self.order != matrix.order:
            raise ValueError(f'Expected order {self.order} got {matrix.order}')
        else:
            return Matrix([
                [matrix.matrix[i][j] + self.matrix[i][j] for j in range(self.column)]
                for i in range(self.row)
            ])

    def __sub__(self, matrix: Matrix) -> Matrix:
        """
        Subtracts two matrix objects

        Parameters
        ----------
        matrix : Matrix object

        Returns
        -------
        Matrix object

        Example
        -------
        >>> _matrix = [[1, 2, 3], [4, 5, 6]]
        >>> _matrix = Matrix(_matrix)
        >>> matrix1 = [[1, 2, 3], [4, 5, 6]]
        >>> matrix1 = Matrix(matrix1)
        >>> _matrix - matrix1
        [[0, 0, 0], [0, 0, 0]]

        """
        if self.order != matrix.order:
            raise ValueError(f'Expected order {self.order} for {matrix.order}')
        else:
            return Matrix([
                [matrix.matrix[i][j] - self.matrix[i][j] for j in range(self.column)]
                for i in range(self.row)
            ])

    def __mul__(self, matrix: Matrix) -> Matrix:
        """
        Multiplying two matrix objects

        Parameters
        ----------
        matrix : Matrix object

        Returns
        -------
        Matrix object

        Example
        -------
        >>> _matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> _matrix = Matrix(_matrix)
        >>> matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> matrix1 = Matrix(matrix1)
        >>> _matrix * matrix1
        [[30, 36, 42], [66, 81, 96], [102, 126, 150]]

        """
        if self.order[2] != matrix.order[0]:
            raise ValueError(f'Cannot multiply these matrices!')
        else:
            new_matrix = [[0 for _ in range(matrix.column)] for _ in range(self.row)]
            for i in range(self.row):
                for j in range(matrix.column):
                    for k in range(matrix.row):
                        new_matrix[i][j] += self.matrix[i][k] * matrix.matrix[k][j]
            return Matrix(new_matrix)

    def __len__(self) -> int:
        """
        Calculates number elements present in the matrix!

        Parameters
        ----------
        self

        Returns
        -------
        int

        Example
        -------
        >>> _matrix = [[1, 2, 3], [4, 5, 6]]
        >>> _matrix = Matrix(_matrix)
        >>> len(_matrix)
        6
        """
        return self.row * self.column

    def __iter__(self):
        """
        Sends all rows of the matrix

        Parameters
        ----------
        self

        Returns
        -------
        iterator

        Example
        -------
        >>> _matrix = [[1, 2, 3], [4, 5, 6]]
        >>> _matrix = Matrix(_matrix)
        >>> print(*_matrix)
        [1, 2, 3] [4, 5, 6]

        """
        for i in self.matrix:
            yield i

    def __getitem__(self, index: int) -> list | int | float:
        """
        Returns a row of the matrix

        Parameters
        ----------
        index : int

        Returns
        -------
        list | int | float

        Example
        -------
        >>> _matrix = [[1, 2, 3], [4, 5, 6]]
        >>> _matrix = Matrix(_matrix)
        >>> _matrix[0]
        [1, 2, 3]

        """
        return self.matrix[index]

    def __contains__(self, elem: int | float) -> bool:
        """
        Checks if element is in the matrix.

        Parameters
        ----------
        elem : int | float

        Returns
        -------
        bool

        Example
        -------
        >>> _matrix = [[1, 2, 3], [4, 5, 6]]
        >>> _matrix = Matrix(_matrix)
        >>> 1 in _matrix
        True
        """
        for i in self.matrix:
            if elem in i:
                return True
        return False

    def __eq__(self, matrix: Matrix) -> bool:
        """
        Checks if two matrices are equal

        Parameters
        ----------
        matrix : Matrix object

        Returns
        -------
        bool

        Example
        -------
        >>> _matrix = [[1, 2, 3], [4, 5, 6]]
        >>> _matrix = Matrix(_matrix)
        >>> matrix1 = [[1, 2, 3], [4, 5, 6]]
        >>> matrix1 = Matrix(matrix1)
        >>> _matrix == matrix1
        True

        """
        if self.order != matrix.order:
            return False
        else:
            return self.matrix == matrix.matrix

    @staticmethod
    def _el_items(
            row: int, column: int,
            matrix: list[list[int | float]]
    ) -> list[list[int | float]]:

        x = len(matrix)
        y = len(matrix[0])
        return [[matrix[i][j] for j in range(y) if j != column] for i in range(x) if i != row]

    def determinant(self) -> int:
        """
        Calculates the Determinant of matrix objects.

        Parameters
        ----------
        self

        Returns
        -------
        int

        Example
        -------
        >>> _matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> _matrix = Matrix(_matrix)
        >>> _matrix.determinant()
        0
        """
        if self.row != self.column:
            raise ValueError('Cannot get determinant of this matrix! Must be a square Matrix')
        else:
            def det(matrix):
                row = len(matrix)
                col = len(matrix[0])

                if (row, col) == (1, 1):
                    return matrix[0][0]

                # hard coding for 2x2
                elif (row, col) == (2, 2):
                    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

                # using sarrus method to solve for 3x3, it's a little faster.
                elif (row, col) == (3, 3):
                    matrix1 = matrix[:]

                    # Extending matrix to use Sarrus Rule.
                    for i in range(row - 1):
                        _col = []
                        for j in range(col):
                            _col.append(matrix1[i][j])
                        matrix1.append(_col)

                    # Calculating Determinant
                    # Adding part
                    add_pointers = [(i, i) for i in range(row)]
                    result = 0
                    for pointer in range(row):
                        temp = 1
                        for tup in add_pointers:
                            i, j = tup
                            temp *= matrix1[i + pointer][j]
                        result += temp

                    # Subtracting part
                    sub_pointers = [((row - 1) - i, 0 + i) for i in range(row)]
                    for pointers in range(row):
                        temp = 1
                        for tup in sub_pointers:
                            i, j = tup
                            temp *= matrix1[i + pointers][j]
                        result -= temp
                    return result

                else:
                    sign = -1
                    result = 0
                    row1 = [matrix[0][i] * (sign ** i) for i in range(col)]
                    for x, y in enumerate(row1):
                        mat = matrix[:][1:]
                        sub_matrix = [[mat[i][j] for j in range(col) if j != x] for i in range(row - 1)]
                        result += y * det(sub_matrix)
                    return result

            return det(self.matrix)

    def count(self, element: int = None) -> dict[int | float, int]:
        """
        Counts occurences of elements

        Parameters
        ----------
        element : int = None

        Returns
        -------
        dict

        Example
        -------
        >>> _matrix = [[1, 2, 3], [4, 5, 6]]
        >>> _matrix = Matrix(_matrix)
        >>> _matrix.count()
        {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}
        >>> _matrix.count(2)
        {2: 1}
        """
        if element is not None:
            cnt = 0
            for i in self.matrix:
                for j in i:
                    if j == element:
                        cnt += 1
            return {element: cnt}

        else:
            count = {}
            for i in self.matrix:
                for j in i:
                    if j not in count:
                        count[j] = 0
                    count[j] += 1
            return count

    def transpose(self) -> Matrix:
        """
        Calculates the transpose of the matrix.

        Parameters
        ----------
        self

        Returns
        -------
        Matrix

        Example
        -------
        >>> _matrix = [[1, 2, 3], [4, 5, 6]]
        >>> _matrix = Matrix(_matrix)
        >>> _matrix.transpose()
        [[1, 4], [2, 5], [3, 6]]

        """
        new_matrix = [[0 for _ in range(self.row)] for _ in range(self.column)]
        for i in range(self.row):
            for j in range(self.column):
                new_matrix[j][i] += self.matrix[i][j]

        return Matrix(new_matrix)

    def randomize(self, low: int = 0, high: int = 100) -> Matrix:
        """
        Radomizes the elements of an already existing matrix.

        Parameters
        ----------
        low : int = 0
        high : int = 100

        Returns
        -------
        Matrix object

        Example
        -------
        >>> _matrix = [[1, 2, 3], [4, 5, 6]]
        >>> _matrix = Matrix(_matrix)
        >>> _matrix.randomize()
        [[23, 35, 35], [2, 28, 86]]
        >>> _matrix.randomize(low=0, high=10)
        [[9, 5, 6], [7, 10, 9]]

        """
        new_matrix = [[randint(low, high) for _ in range(self.column)] for _ in range(self.row)]
        return Matrix(new_matrix)

    def adjoint(self) -> Matrix:
        """
        Calculates the adjoint of the matrix.

        Parameters
        ----------
        self

        Returns
        -------
        Matrix object

        Example
        -------
        >>> _matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> _matrix = Matrix(_matrix)
        >>> _matrix.adjoint()
        [[-3, 6, -3], [6, -12, 6], [-3, 6, -3]]

        """

        if self.row != self.column:
            raise ValueError('Cannot get adj of this matrix! Must be a square Matrix')
        else:
            def adj(matrix):
                row = len(matrix)
                col = len(matrix[0])

                if (row, col) == (1, 1):
                    return matrix

                elif (row, col) == (2, 2):
                    matrix[0][0], matrix[1][1] = matrix[1][1], matrix[0][0]
                    matrix[1][0] *= -1
                    matrix[0][1] *= -1
                    return matrix

                else:
                    mat = matrix[:]
                    new_matrix = [[0 for _ in range(row)] for _ in range(col)]
                    for i in range(row):
                        for j in range(col):
                            sub_mat = self._el_items(i, j, mat)
                            sub_matrix = Matrix(sub_mat)
                            new_matrix[i][j] += sub_matrix.determinant() * ((-1) ** (i + j))
                    return new_matrix

            return Matrix(adj(self.matrix)).transpose()

    def inverse(self) -> Matrix:
        """
        Calculates the inverse of the matrix.

        Parameters
        ----------
        self

        Returns
        -------
        Matrix object

        Example
        -------
        >>> _matrix = [[1, 2, 3], [6, 6, 6], [7, 7, 9]]
        >>> _matrix = Matrix(_matrix)
        >>> _matrix.inverse()
        [[-1.0, -0.25, 0.5], [1.0, 1.0, -1.0], [0.0, -0.5833, 0.5]]

        """
        if self.row != self.column:
            raise ValueError('Cannot get inverse of this matrix! Must be a square Matrix')
        else:
            det = self.determinant()
            if det == 0:
                raise ValueError('Cannot determine inverse, determine is 0')
                
            adj = list(self.adjoint())
            inverse_matrix = [[0 for _ in range(self.row)] for _ in range(self.column)]
            for i in range(self.row):
                for j in range(self.column):
                    inverse_matrix[i][j] += round(adj[i][j]*(1**(i+j)) / det, 4)

            return Matrix(inverse_matrix)

    def symmetric(self, matrix: Matrix) -> bool:
        """
        Parameters
        ----------
        Matrix object

        Returns
        -------
        bool

        Examples
        -------
        >>> _matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> _matrix = Matrix(_matrix)
        >>> matrix1 = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        >>> matrix1 = Matrix(matrix1)
        >>> _matrix.symmetric(matrix1)
        True

        """
        return self.transpose() == matrix
