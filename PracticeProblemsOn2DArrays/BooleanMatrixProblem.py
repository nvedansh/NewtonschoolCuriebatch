t = int(input())
for testcase in range(t):
	line = input().strip().split(" ")
	m = int(line[0])
	n = int(line[1])
	matrix = []
	for i in range(m):
		row = input().strip().split(" ")
		matrix.append(row)
	
	rows = []
	for i in range(m):
		for j in range(n):
			if matrix[i][j] == "1":
				rows.append(i)
				break

	for index in rows:
		matrix[index] = ["1" for j in range(n)]
	
	for i in range(m):
		for j in range(n):
			print(matrix[i][j], end = " ")
		print()