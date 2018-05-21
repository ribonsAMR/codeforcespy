x = int(input())
count = 0
for i in range(x):
	inp = list(map(int, input().split()))
	p, c = inp[:]
	if (c-p) >= 2:
		count += 1
print(count)