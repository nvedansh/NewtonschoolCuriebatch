m, n, q = map(int, input().strip().split(" "))
matrix_set = set()
for i in range(m):
    row = list(map(int, input().strip().split(" ")))
    for element in row:
        matrix_set.add(element)

for query in range(q):
    num = int(input().strip())
    if num in matrix_set:
        print("Yes")
    else:
        print("No")