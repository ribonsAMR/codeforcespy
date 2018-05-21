vi = input()
vi = list(map(int, vi.split()))

rides, freerides, cost, freecost = vi[:]

if (cost/1) > (freecost/freerides):
	final_cost = 0
	a = (rides//freerides)
	rides -= a * freerides
	final_cost += a * freecost
	if (freecost) < rides * cost:
		final_cost += freecost
	else:
		final_cost += rides * cost
else:
	final_cost= rides * cost
print(final_cost)