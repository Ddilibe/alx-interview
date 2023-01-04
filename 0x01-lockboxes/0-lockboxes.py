#!/usr/bin/python3

""" Script that holds a lockbox function """

def canUnlockAll(boxes):
	"""
		Method that determines if all the boxes can be open

		Arguments:
			boxes: A list of list of boxes

		Return:
			Boolean Value: It returns True if all the boxes can be opened
			else ot will return False
	"""
	other, nother = [], {}
	[other.append(r) for r in boxes[0]]
	for i in range(1, len(boxes)):
		if i not in other:
			nother[str(i)] = boxes[i]
			continue
		[other.append(r) for r in boxes[i]]
	ans, i , edit = True, 0, []
	if nother:
		while i < 10 and len(nother) != 0:
			edit = []
			for keys, value in nother.items():
				i += 1
				if int(keys) in other:
					[other.append(r) for r in value]
					edit.append(keys)
			for e in edit:
				del nother[e]
	if nother:
		ans = False
	return ans
