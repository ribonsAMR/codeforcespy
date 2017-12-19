repeats = int(input())
x, y, z = 0, 0, 0
for i in range(repeats):
	i, j, k = list(map(int, input().split()))[:]
	x += i
	y += j
	z += k
if not x and not y and not z:
	print("YES")
else:
	print("NO")