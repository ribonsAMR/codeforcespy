rang, time = list(map(int, input().split()))[:]
_q = list(input().lower())


for _f in range(time):
	pos = rang - 1

	while pos > 0:
		a, b = pos, pos - 1
		if _q[a] != _q[b] and _q[a] == 'g':
			_q[a], _q[b] = _q[b], _q[a]
			pos -= 2
		else:
			pos -= 1

print(''.join(x.upper() for x in _q))