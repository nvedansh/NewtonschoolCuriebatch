n = int(input().strip())
ans = 0
var = list(map(float, input().strip().split(" ")))
for i in var:
	ans += (1 / i)
print(int(1/ans))