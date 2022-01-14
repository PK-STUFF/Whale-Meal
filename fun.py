import numpy as np


# This is a drop-wave function to be optimised by the neural network
def drop_wave(x):
	x1, x2 = x

	tmp = x1 ** 2 + x2 ** 2
	return -((1 + np.cos(12 * np.sqrt(tmp))) / (0.5 * (tmp) + 2)) + 1
