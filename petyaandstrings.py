a = input().lower()
b = input().lower()

if len(a) > len(b):
	print(1)
elif len(a) == len(b):
	ans = 0
	for i in range(len(a)):
		if ord(a[i]) > ord(b[i]):
			ans = 1
			break
		elif ord(a[i]) < ord(b[i]):
			ans = -1
			break
		else:
			continue
	print(ans)
else:
	print(-1)