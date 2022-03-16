# [Matrix](https://github.com/RyugaXhypeR/Matrix/blob/main/matrix/main.py#L5)
Class to perform the various matrix operations

## [Addition](https://github.com/RyugaXhypeR/Matrix/blob/main/matrix/main.py#L67-L96)
Adds two matrix objects.
```python
>>> matrix1 = Matrix([[1, 2], [3, 4]])
>>> matrix2 = Matrix([[5, 6], [7, 8]])
>>> matrix + matrix2
Matrix([[6, 8], [10, 12]])
```

## [Subtraction](https://github.com/RyugaXhypeR/Matrix/blob/main/matrix/main.py#L97-L126)
Subtracts two matrix objects.
```python
>>> matrix1 = Matrix([[1, 2], [3, 4]])
>>> matrix2 = Matrix([[5, 6], [7, 8]])
>>> matrix1 - matrix2
Matrix([[-4, -4], [-4, -4]])
```

## [Multiplication](https://github.com/RyugaXhypeR/Matrix/blob/main/matrix/main.py#L127-L158)
Multiplies two matrix objects.
```python
>>> matrix1 = Matrix([[1, 2], [3, 4]])
>>> matrix2 = Matrix([[5, 6], [7, 8]])
>>> matrix1 * matrix2
Matrix([[19, 22], [43, 50]])
```

## [Transpose](https://github.com/RyugaXhypeR/Matrix/blob/main/matrix/main.py#L401-L427)
Returns transpose of matrix.
```python
>>> matrix1 = Matrix([[1, 2], [3, 4]])
>>> matrix1.transpose()
Matrix([[1, 3], [2, 4]])
```

## [Determinant](https://github.com/RyugaXhypeR/Matrix/blob/main/matrix/main.py#L286-L362)
Returns determinant of matrix.
```python
>>> matrix1 = Matrix([[1, 2], [3, 4]])
>>> matrix1.determinant()
-2
```

## [Count](https://github.com/RyugaXhypeR/Matrix/blob/main/matrix/main.py#L363-L427)
Returns a count of elements in matrix.
```python
>>> matrix1 = Matrix([[1, 2], [3, 4]])
>>> matrix1.count()
{1:1, 2:1, 3:1, 4:1}
```

## [Randomize](https://github.com/RyugaXhypeR/Matrix/blob/main/matrix/main.py#L428-L453)
Randomizes the matrix.
```python
>>> matrix1 = Matrix([[1, 2], [3, 4]])
>>> matrix1.randomize()
[[0.9, 0.1], [0.1, 0.9]]
```

## [Adjoint](https://github.com/RyugaXhypeR/Matrix/blob/main/matrix/main.py#L454-L502)
Returns the adjoint of the matrix.

```python
>>> matrix1 = Matrix([[1, 2], [3, 4]])
>>> matrix1.adjoint()
Matrix([[4, -3], [-2, 1]])
```

## [Inverse](https://github.com/RyugaXhypeR/Matrix/blob/main/matrix/main.py#L503-L537)
Returns the inverse of the matrix.
```python
>>> matrix = [[1, 2, 3], [6, 6, 6], [7, 7, 9]]
>>> matrix = Matrix(matrix)
>>> matrix.inverse()
[[-1.0, -0.25, 0.5], [1.0, 1.0, -1.0], [0.0, -0.5833, 0.5]]
```

## [Symmetric](https://github.com/RyugaXhypeR/Matrix/blob/main/matrix/main.py#L538-L558)
Checks if two matrices are symmetric
```python
>>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> matrix = Matrix(matrix)
>>> matrix1 = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
>>> matrix1 = Matrix(matrix1)
>>> matrix.symmetric(matrix1)
True
```
