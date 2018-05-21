i1 = input()
n, k = list(map(int, i1.split()))[:]

i2 = input()
i2 = list(map(int, i2.split()))

c = 0

for i in range(n):
	if i2[i-1] >= i2[k-1] and i2[i-1] > 0:
		c += 1
print(c)
