k, l, m, n, d = [int(input()) for x in range(5)]

li = list(	range(1, d+1)	)

mi = [k, l, m, n]
def damager(x):

	for i in range(0, d, x):
		if li[i] != None:
			li[i] = None


for i in mi:
	if li.count(None) == d: 
		break
	if i > d:
		continue
	
	damager(i)
print(li.count(None))

'''k, l, m, n, d = [int(input()) for x in range(5)]
count = 0
for i in range(1, d+1):
	if i%k == 0 or i%l == 0 or i%m == 0 or i%n == 0:
		count += 1
print(count)'''