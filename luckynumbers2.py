lis = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
i = list(map(int, input()))
count = i.count(4) + i.count(7)
for x in lis:
	if count == x:
		print("YES")
		exit()
print("NO")

'''li = list()
for i in range(1, 1001):
	y = list(str(i))
	count = y.count('4') + y.count('7')
	if count == len(y):
		li.append(i)
print(sorted(li))'''

"""for i in range(1, 1000000000):
	targetFormat = '{0:0>9}'.format(i)
	print(targetFormat, file=open('db.txt', 'a'))
"""
"""with open('db.txt', 'r') as afile:
	for i in afile.readlines():
		print(i.strip()) #use your code here, i used to print it, using .strip() to remove the new line from the end of the number, try without .strip().
	    #int( i.strip() ) - converting to int"""