i = int(input())
li = list()
for n in range(i):
	li.append(input())
for n in li:
	if len(n) > 10:
		print('{}{}{}'.format(  n[0], len(n)-2 ,n[-1]   ))
	else:
		print(n)
