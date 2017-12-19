x = 0
pos = None
for r in range(5):
	i = input()
	if '1' in i:
		pos = (x, i.split().index('1'))
	x += 1

count = 0

count += abs(2 - pos[0])
count += abs(2 - pos[1])

print(count)