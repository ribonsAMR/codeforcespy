#3 17 4 - 13
cost, budget, n = list(map(int, input().split()))[:]
m = cost*(n*(n+1))/2
if m >= budget:
	print(int(m-budget))
else:
	print(0)