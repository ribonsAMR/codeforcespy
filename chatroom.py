word = 'hello'
inp = input()
index = 0
count = 0
for i in inp:
	if index == len(word):
		break
	if i == word[index]:
		count += 1
		index += 1
if count == len(word):
	print("YES")
else:
	print("NO")