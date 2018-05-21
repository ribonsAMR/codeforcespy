word_s = list(input())
word_t = list(input())

if word_t[::-1] == word_s:
	print("YES")
else:
	print("NO")