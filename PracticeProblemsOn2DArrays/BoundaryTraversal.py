# Your code here


def boundaryTraversal(matrix, N, M): #N = 3, M = 4
	start_row = 0
	start_col = 0
	count = 0
	if N != 1 and M != 1:
		total = 2 * (N - 1) + 2 * (M - 1)
	else:
		total = max(M, N)

	#First row
	for i in range(start_col, M, 1): #0,1, 2, 3
		count += 1
		print(matrix[start_row][i], end = " ")
	
	if count == total:
		return
	
	start_row += 1

	#Last column
	for i in range(start_row, N, 1): # 1, 2
		count += 1
		print(matrix[i][M - 1], end = " ")
	
	if count == total:
		return
	
	M -= 1
	
	#Last Row
	for i in range(M - 1, start_col - 1, -1): # 2, 1, 0
		count += 1
		print(matrix[N - 1][i], end = " ")
	
	if count == total:
		return
	
	#First Column
	N -= 1 # 2
	for i in range(N - 1, start_row - 1, -1):
		count += 1
		print(matrix[i][start_col], end = " ")
	
	start_col += 1
	
	

testcase = int(input().strip())
for test in range(testcase):
	dim = input().strip().split(" ")
	N = int(dim[0])
	M = int(dim[1])

	matrix = []
	elements = input().strip().split(" ") #N * M
	start = 0
	for i in range(N):
		matrix.append(elements[start : start + M]) # (0, M - 1) | (M, 2*m-1)
		start = start + M

	boundaryTraversal(matrix, N, M)
	print()