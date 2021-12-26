t = int(input().strip())
for testcase in range(t):
	n, k = map(int, input().strip().split(" "))
	numbers = list(map(int, input().strip().split(" ")))

	num_dict = {0:1}
	sum_numbers = 0
	count = 0

	for num in numbers:
		sum_numbers += num
		if sum_numbers - k in num_dict:
			count += num_dict[sum_numbers - k]
		if sum_numbers in num_dict:
			num_dict[sum_numbers] += 1
		else:
			num_dict[sum_numbers] = 1
	
	print(count)