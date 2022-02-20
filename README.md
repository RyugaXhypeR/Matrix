# Matrix
Class to perform the following matrix operations:

## Addition
Adds two matrix objects.
```
>>> matrix1 = Matrix([[1, 2], [3, 4]])
>>> matrix2 = Matrix([[5, 6], [7, 8]])
>>> matrix + matrix2
Matrix([[6, 8], [10, 12]])
```

## Subtraction
Subtracts two matrix objects.
```
>>> matrix1 = Matrix([[1, 2], [3, 4]])
>>> matrix2 = Matrix([[5, 6], [7, 8]])
>>> matrix1 - matrix2
Matrix([[-4, -4], [-4, -4]])
```

## Multiplication
Multiplies two matrix objects.
```
>>> matrix1 = Matrix([[1, 2], [3, 4]])
>>> matrix2 = Matrix([[5, 6], [7, 8]])
>>> matrix1 * matrix2
Matrix([[19, 22], [43, 50]])
```

## Transpose
Returns transpose of matrix.
```
>>> matrix1 = Matrix([[1, 2], [3, 4]])
>>> matrix1.transpose()
Matrix([[1, 3], [2, 4]])
```

## Determinant
Returns determinant of matrix.
```
>>> matrix1 = Matrix([[1, 2], [3, 4]])
>>> matrix1.determinant()
-2
```

## Count
Returns a count of elements in matrix.
```
>>> matrix1 = Matrix([[1, 2], [3, 4]])
>>> matrix1.count()
{1:1, 2:1, 3:1, 4:1}
```

## Randomize
Randomizes the matrix.
```
>>> matrix1 = Matrix([[1, 2], [3, 4]])
>>> matrix1.randomize()
[[0.9, 0.1], [0.1, 0.9]]
```

## Adjoint
Returns the adjoint of the matrix.
```
>>> matrix1 = Matrix([[1, 2], [3, 4]])
>>> matrix1.adjoint()
Matrix([[4, -3], [-2, 1]])
```

## Inverse
Returns the inverse of the matrix.
```
>>> matrix1 = Matrix([[1, 2], [3, 4]])
>>> matrix1.inverse()
[[-0.5, -1.5], [-1.0, -2.0]]
```