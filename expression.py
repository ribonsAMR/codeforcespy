'''
a + (b.c)
a . (b+c)
a . b . c
(a+b) . c
a + b + c
'''
a, b, c = [int(input()) for i in range(3)]

# Evaluate all the formulas, and gather them inside a list
formulas = [a + (b*c),
            a * (b+c),
            (a+b) * c,
            a * b * c,
            a + b + c]

# Ascending sort, from the smallest to the biggest.
formulas = sorted(formulas)

# The last item in the list, which is the biggest sum of the forumlas.
print(formulas[-1])
