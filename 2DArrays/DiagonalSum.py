# Your code here
n = int(input().strip())
matrix = []
for i in range(n):
    row = list(map(int, input().strip().split(" ")))
    matrix.append(row)

primary_diag = 0
secondary_diag = 0

for i in range(n):
	for j in range(n):
		if i == j:
			primary_diag += matrix[i][j]
		if i + j == n-1:
			secondary_diag += matrix[i][j]

print(primary_diag, secondary_diag)