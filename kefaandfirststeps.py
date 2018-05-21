input()
intList = list(map(int, input().split()))

count = 1
maxc = 1

for i in range(len(intList) - 1):
	a, b = intList[i], intList[i + 1]
	if b >= a:
		count += 1
		if count > maxc:
			maxc = count
	else: #break
		count = 1

if count > maxc:
	print(count)
else:
	print(maxc)