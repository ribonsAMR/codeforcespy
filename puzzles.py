n, m = list( map(int, input().split() ))[:]
list_in_int = list( map(int, input().split() ))

sortedList = sorted(list_in_int)

diff = sortedList[n-1] - sortedList[0]
sortedList.pop(0)

while len(sortedList) >= n:
	if (sortedList[n-1] - sortedList[0]) < diff:
		diff = sortedList[n-1] - sortedList[0]
	sortedList.pop(0)

# for i in range(1, (m - n)+1):
# 	if sortedList[n-1+i] - sortedList[i] < diff:
# 		diff = sortedList[n-1+i] - sortedList[i]

print(diff)