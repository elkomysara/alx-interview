# Pascal's Triangle

## Description
This project implements a function that returns Pascal's triangle of a given size `n`. Pascal's triangle is a triangular array of numbers where each number is the sum of the two directly above it. The project is part of the ALX software engineering curriculum and demonstrates fundamental Python concepts such as lists, list comprehensions, loops, and basic arithmetic operations.

## Requirements
- The function should return a list of lists of integers representing Pascal’s triangle of size `n`.
- The function should return an empty list if `n <= 0`.
- The input `n` will always be a non-negative integer.

## Files
- `0-pascal_triangle.py`: Contains the implementation of the `pascal_triangle` function.
- `0-main.py`: A test file that prints the output of the `pascal_triangle` function for `n = 5`.

## Function
### `pascal_triangle(n)`
This function returns a list of lists of integers representing Pascal’s triangle of size `n`. If `n` is less than or equal to 0, it returns an empty list.

#### Example
```python
>>> pascal_triangle(5)
[
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]
