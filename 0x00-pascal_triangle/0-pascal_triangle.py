#!/usr/bin/python3

""" 
	Script that demonstrates the pascal's triangle
"""

import math

light = [1]

def pascal_triangle(n):
	"""
		Function for creating the pascal's triangle

		Arguments:
			n: Integer variable in the triangle

		Return:
			List if n > 0
			empty list if n <= 0
	"""
	i, other = 0, []
	while i < n:
		y, tri = 0, []
		while y <= i:
			tri.append(math.comb(i, y))
			y += 1
		other.append(tri)
		i += 1
	return other
	
