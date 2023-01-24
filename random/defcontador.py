def counter(start, end, step):
	"""
	A counting function that output result on screen
	:param start: beginning of counter
	:param end: end of couting
	:param step: step of counting
	:return: no return
	Function created by FelixOakz
	"""
	c = start
	while c <= end:
		print(f'{end}', end=', ')
		c += step
	print('Finished.')
 
counter(1, 1000, 2)
 