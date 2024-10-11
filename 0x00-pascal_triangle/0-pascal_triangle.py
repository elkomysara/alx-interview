#!/usr/bin/python3
"""
0-pascal_triangle.py
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of size n.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]  # First row is always [1]
    
    for i in range(1, n):
        prev_row = triangle[-1]  # Get the previous row
        row = [1]  # Start the new row with 1
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])  # Sum of two above elements
        row.append(1)  # End the row with 1
        triangle.append(row)
    
    return triangle
