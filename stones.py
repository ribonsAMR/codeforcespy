a = int(input())
b = input().lower()
count = 0
for i in range(a):
	if i != a-1 and b[i] == b[i+1]:
		count += 1
print(count)