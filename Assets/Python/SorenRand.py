"""Lite version of Python random module utilizing Soren random number generator.
credits: embryodead, Guido van Rossum et al
"""

from CvPythonExtensions import *

def random():
	return float(CyGame().getSorenRandNum(10000, 'Random float')) / 10000

def randint(a, b):
	"""Return a random integer N such that a <= N <= b."""
	return a + CyGame().getSorenRandNum(b - a + 1, 'Random integer')

def dice(sides=100):
	"""Generates a random integer N such that 1 <= N <= sides."""
	return randint(1, sides)

def sample(population, k=1):
	"""Return a k length list of unique elements chosen from the population sequence."""
	if len(population) < k:
		k = len(population)
	output = []
	while len(output) < k:
		e = choice(population)
		if e not in output:
			output.append(e)
	return output

def choice(seq):
	"""Return a random element from the non-empty sequence."""
	if seq:
		return seq[CyGame().getSorenRandNum(len(seq), 'Random element')]

def shuffle(x):
	"""Shuffle the list x in place; based on random.py"""
	for i in reversed(range(1, len(x))):
		j = randint(0, i)
		x[i], x[j] = x[j], x[i]

def getRand(a):
	"""Return a random integer N such that 0 <= N < a. C compatibility."""
	return CyGame().getSorenRandNum(a, 'Random integer')

def getASyncRand(a):
	"""Asynchronous version of getRand."""
	return CyGlobalContext().getASyncRand().get(a, 'Random integer')