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
	g = np.asarray(gradient, dtype=float)

	if not np.any(g):
		return {
			'magnitude': 0.0,
			'direction': np.zeros_like(g),
			'descent_direction': np.zeros_like(g)
		}
	
	magnitude = np.linalg.norm(g)
	direction = g / magnitude
	descent_direction = -direction

	return {
		'magnitude': magnitude, 
		'direction': direction, 
		'descent_direction': descent_direction
	}