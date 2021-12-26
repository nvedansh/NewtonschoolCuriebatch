# Your code here
def transpose(matrix, n):
	for i in range(1, n):
		for j in range(i):
			temp = matrix[i][j]
			matrix[i][j] = matrix[j][i]
			matrix[j][i] = temp
	return matrix

def rotate(matrix, n):
	matrix = transpose(matrix, n)
	for i in range(n):
		for j in range(n // 2):
			temp = matrix[i][j]
			matrix[i][j] = matrix[i][n - 1 - j]
			matrix[i][n - 1 - j] = temp
	return matrix

n = int(input().strip())
matrix = []
for i in range(n):
	row = list(map(int, input().strip().split(" ")))
	matrix.append(row)

matrix = rotate(matrix, n)
for row in matrix:
	print(*row)
print()
matrix = rotate(matrix, n)
for row in matrix:
	print(*row)