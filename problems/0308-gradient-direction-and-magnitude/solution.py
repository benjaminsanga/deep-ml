import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	for i in gradient:
		if i == 0:
			return {'magnitude': 0, 'direction': [0, 0]}
	
	magnitude = 0
	direction = []
	descent_direction = []

	for i in range(len(gradient)):
		magnitude += gradient[i] ** 2
	
	magnitude = np.sqrt(magnitude)
	
	for i in range(len(gradient)):
		direction.append(gradient[i]/magnitude)
		descent_direction.append(-(gradient[i]/magnitude))

	return {
		'magnitude': magnitude, 
		'direction': direction, 
		'descent_direction': descent_direction
	}