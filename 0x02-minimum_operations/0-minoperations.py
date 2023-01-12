#!/usr/bin/python3
""" Script that tests and visualizes minimum operations """

def minOperations(n: int) -> int:
	if n == 2:
		return 1
	if n == 1:
		return 0
	i, h = 2, "H"
	while True:
		if n % i == 0:
			break
		i += 1
	first = int(n/i) + i
	i, h = 3, "H"
	while True:
		if n % i == 0:
			break
		i += 1
	second = int(n/i) + i
	if first < second:
		return first
	return second
