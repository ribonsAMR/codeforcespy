x = input()
if x[0].islower() and x[1:].isupper():
	x = x[0].upper() + x[1:].lower()
	print(x)
elif x.isupper():
	print(x.lower())
elif x.islower():
	if len(x) > 1:
		print(x.lower())
	else:
		print(x.upper())
else:
	print(x)