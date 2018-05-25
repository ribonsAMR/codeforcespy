i = int(input())

moves = 0

if i % 5 == 0: moves = i / 5
else: moves = i // 5 + 1

print(int(moves))
