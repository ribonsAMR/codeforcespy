i = input()
x = 0 #0
y = 0 #1
for n in i:
	if x >= 7 or y >= 7:
		break
	if n == '0':
		x += 1
		y = 0
	else:
		y += 1
		x = 0
if x >= 7 or y >= 7:
	print("YES")
else:
	print("NO")