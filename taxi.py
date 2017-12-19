input()
inp = sorted(list(map(int, input().split())))[::-1]
taxi = 0
while len(inp) > 0:
	#print(inp, taxi)
	taxi += 1
	temp = 4 - inp.pop(0)
	if temp == 0:
		continue
	else:
		while temp > 0 and len(inp) >= 1:
			if temp - inp[-1] >= 0:
				temp -= inp[-1]
				inp.pop()
			else:
				break
print(taxi)