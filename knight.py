import numpy as np

def knight_moves_builder():
	"""
	the 5x5 convolution kernel mapping
	the knight's valid moves from the 
	central square
	"""

	# --- start with upper right corner
	corner = np.identity(2, dtype=bool)

	# --- add upper left corner (misses center) 
	upper = np.hstack((~corner, corner)) 

	# --- reflect to add bottom section (misses center)
	four_by_four = np.vstack((upper, ~upper))

	# --- add center row and column
	valid_moves = np.insert(arr=four_by_four, obj=2, values=False, axis=0)
	valid_moves = np.insert(arr=valid_moves, obj=2, values=False, axis=1)

	return valid_moves.astype(int)/np.sum(valid_moves)
