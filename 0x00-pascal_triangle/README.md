# Pascal's triangle


### Introduction

Paschal's triangle is a triangular array of the binomial coefficients that arises in probability theory, combinatorics and algebra, It is named after the french mathematician Blaise Paschal although a lot of other mathematicians has studied the concept before him. 

### Formula
The formula is `nCr = (n-1)C(r-1) + (n-1)Cr`

### Task

Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

- Returns an empty list if n <= 0
- You can assume n will be always an integer

### Test
*Main Test Function*

`
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle
def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))
if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
`

### Resources

1. [Wikipedia](https://en.wikipedia.org/wiki/Pascal's_triangle)