inp = input()
chars = list()
for i in inp:
	if i not in chars:
		chars.append(i)

if len(chars) % 2 == 0: #even
	print("CHAT WITH HER!")
else:
	print("IGNORE HIM!")