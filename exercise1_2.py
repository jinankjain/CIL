import numpy as np
import random
import math

def pair_wise(coord1, coord2):
	return math.sqrt(pow((coord1[0]-coord2[0]),2) + pow((coord1[0]-coord2[0]),2))


def main():
	N = 3
	O = 4
	P = [[random.random() for i in range(2)] for j in range(N)]
	Q = [[random.random() for i in range(2)] for j in range(O)]

	print([[pair_wise(i, j) for i in P] for j in Q])


if __name__ == '__main__':
	main()