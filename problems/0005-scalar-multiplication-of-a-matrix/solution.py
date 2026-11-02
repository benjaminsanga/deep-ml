def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	if len(matrix) == 0:
		return -1
	
	result = []
	current_row = []
	for row in matrix:
		for value in row:
			current_row.append(value * scalar)
		result.append(current_row)
		current_row = []
	
	return result
