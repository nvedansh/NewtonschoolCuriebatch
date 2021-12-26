n, k = map(int, input().strip().split(" "))
numbers = list(map(int, input().strip().split(" ")))

count = 0
num_dict = dict()

# k = 6
# 1 5 7 1 5
# num_dict = {1:2, 5:1, 7:1}, count = 1 + 1 + 2 = 4
for num in numbers:
	if k - num in num_dict:
		count += num_dict[k - num]
	#inserting num inside dict
	if num in num_dict:
		num_dict[num] += 1
	else:
		num_dict[num] = 1

print(count)