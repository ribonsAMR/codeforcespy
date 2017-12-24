word = 'hello'
inp = input()
index = 0
for i in inp:
	if index == len(word):
		break
	if i == word[index]:
		index += 1
if index == len(word):
	print("YES")
else:
	print("NO")