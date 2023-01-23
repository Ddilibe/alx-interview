#!/usr/bin/python3
""" Script that validate UTF-8 encoding """
from typing import List


def validUTF8(data: List[int]) -> bool:
	"""
		Function thst determines if a given data set
		represents valid UTF-8 encoding

		Args:
			:params @data [List[int]] - The first argument contains
			a list of ints that will be validated

		Return:
			The return value is a boolean
	"""
	bin_data = [str(bin(i)).split('0b')[1] for i in data]
	check = True
	for i in bin_data:
		j = 0
		for w in i:
			if w == '1':
				j +=1
			else:
				break
		if j > 4:
			check = False
			break
	return check
