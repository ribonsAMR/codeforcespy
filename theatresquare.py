import math
i = input()
n, m, a = list(map(int, i.split()))[:]
answer = math.ceil(n/a) * math.ceil(m/a)
print(answer)
