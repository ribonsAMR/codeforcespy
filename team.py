i = int(input())
c = 0
for n in range(i):
	check = 0
	j = list(map(int, input().split()))
	for k in j:
		if k == 1: check += 1
	if check >= 2:
		c += 1
print(c)
