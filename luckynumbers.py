lis = sorted([4, 7, 44, 77, 47, 744, 447, 474, 747, 74, 777, 444, 477])
i = int(input())
for l in lis:
	if i % l == 0:
		print('YES')
		exit()
print('NO')