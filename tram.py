i = int(input())
current = 0
m = 0
for j in range(i):
	inp = input()
	inp = list(map(int, inp.split()))
	enter, exit = inp[:]
	current += (exit - enter)
	if current > m: m = current
print(m)
