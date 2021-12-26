m, n = map(int, input().strip().split(" "))
matrix = []
for i in range(m):
	row = list(map(int, input().strip().split(" ")))
	matrix.append(row)

count = 0
for i in range(1, m - 1, 1): #i = 0 to m - 1
	for j in range(1, n - 1, 1):
		#matrix[i][j] ---> current cell
		if matrix[i - 1][j] == 1 and matrix[i + 1][j] == 1 and matrix[i][j-1] == 1 and matrix[i][j+1] == 1:
			count += 1

print(count)