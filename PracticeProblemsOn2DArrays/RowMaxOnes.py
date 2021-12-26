m, n = map(int, input().strip().split(" "))
matrix = []
for i in range(m):
    row = list(map(int, input().strip().split(" ")))
    matrix.append(row)

ans = 0
max_count = 0
for i in range(m):
    count = 0
    for num in matrix[i]: 
        if num == 1:
            count += 1
    if max_count < count:
        max_count = count
        ans = i
print(ans)