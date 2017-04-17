import numpy as np
from itertools import repeat
import random

def div(x, y):
	return x/y

def sub(x, y):
	return (x-y)

def normalize_matrix(M):
	mean = np.mean(M)
	std = np.std(M)
	tmp = map(sub, M, repeat(mean))
	return map(div, tmp, repeat(std))

def print_mat(M):
	for i in M:
		print(i)

def main():
	N = 3
	M = [[random.random() for i in range(N)] for j in range(N)]
	print(list(normalize_matrix(M)))

if __name__ == '__main__':
	main()