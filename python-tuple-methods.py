# Two built-in tuple methods: count() and index()

t = ( 1, 2, "happy", True, "happy", [], (), {})

print(t.count("happy"))

print(t.count({}))



print(t.index(2))

print(t.index("happy")) # prints the index of first incidence of a duplicate value
