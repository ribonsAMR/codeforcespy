i = input()
i = list(i.lower())
vowels = 'aoyeui'

for index, char in enumerate(i):
	if char in vowels:
		i[index] = ''
	else:
		i[index] = '.' + char

i = ''.join(a for a in i)
print(i)