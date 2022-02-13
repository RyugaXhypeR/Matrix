# Matrix
Class to perform the following matrix operations:

## Addition
```
>>> matrix1 = Matrix([[1, 2], [3, 4]])
>>> matrix2 = Matrix([[5, 6], [7, 8]])
>>> matrix + matrix2
Matrix([[6, 8], [10, 12]])
```

## Subtraction
```
>>> matrix1 = Matrix([[1, 2], [3, 4]])
>>> matrix2 = Matrix([[5, 6], [7, 8]])
>>> matrix1 - matrix2
Matrix([[-4, -4], [-4, -4]])
```

## Multiplication
```
>>> matrix1 = Matrix([[1, 2], [3, 4]])
>>> matrix2 = Matrix([[5, 6], [7, 8]])
>>> matrix1 * matrix2
Matrix([[19, 22], [43, 50]])
```

## Transpose
```
>>> matrix1 = Matrix([[1, 2], [3, 4]])
>>> matrix1.transpose()
Matrix([[1, 3], [2, 4]])
```

## Determinant
```
>>> matrix1 = Matrix([[1, 2], [3, 4]])
>>> matrix1.determinant()
-2
```

## Count
```
>>> matrix1 = Matrix([[1, 2], [3, 4]])
>>> matrix1.count()
{1:1, 2:1, 3:1, 4:1}
```

## Randomize
```
>>> matrix1 = Matrix([[1, 2], [3, 4]])
>>> matrix1.randomize()
[[0.9, 0.1], [0.1, 0.9]]
```
