N = int(input().strip())
matrix = []
for i in range(N):
	row = input().strip().split(" ")
	matrix.append(row)

N_ROWS = N
N_COLS = N

start_row = 0
start_col = 0

# 1 2 3 4 
# 5 6 7 8 
# 9 10 11 12 
# 13 14 15 16 

# 1 2 3
# 4 5 6
# 7 8 9

count = 0
while True:
	#First Column
	for i in range(start_row, N_ROWS, 1):
		count += 1
		print(matrix[i][start_col], end = " ")
	start_col += 1
	if count == N * N:
		break
	
	#Last Row
	for i in range(start_col, N_COLS, 1):
		count += 1
		print(matrix[N_ROWS - 1][i], end = " ")
	
	N_ROWS -= 1 #3
	if count == N * N:
		break
	
	#Last Column
	for i in range(N_ROWS - 1, start_row - 1, -1): # i -> 2, 1, 0
		count += 1
		print(matrix[i][N_COLS - 1], end = " ")
	
	N_COLS -=1
	if count == N * N:
		break
	
	#First Row
	for i in range(N_COLS - 1, start_col - 1, -1):
		count += 1
		print(matrix[start_row][i], end = " ")
	
	start_row += 1
	if count == N * N:
		break


	#start_row = 0 -> 1
	#start_col = 0 -> 1
	#N_ROWS = 4 -> 3
	#N_COLS = 4 -> 3