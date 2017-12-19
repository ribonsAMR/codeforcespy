a = input()
b = sorted(list(map(int, input().split())))[::-1]

me, him = 0, sum(b)
count = 0

while me <= him:
	if len(b) == 1 and me > him: break
	p = b.pop(0)
	me += p
	him -= p
	count += 1
	#print(me, him, count)
	#input()
print(count)