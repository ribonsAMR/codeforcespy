i = int(input())
x = 0
for n in range(i):
	j = input()
	if '+' in j:
		x += 1
	elif '-' in j:
		x -= 1
print(x) 
