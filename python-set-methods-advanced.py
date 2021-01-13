# Advanced Set Methods

# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not



# intersection()	Returns a set that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets

# symmetric difference ===> the union of two sets, minus their intersection
# intersection ===> where they match

# ---- Joining sets ----

# Two ways to join sets:

# union() ---> creates a new set; does not mutate the sets to be joined
# update() ---> mutates the first set by adding the items in the new set to it

s = { "one", "two", 3, False, "duplicate", ()}

s2 = { "a", "b", None, 2.3, "duplicate"}


newS = s.union(s2)
print(s.union(s2))
print(newS)
print(s)
print(s2)

mutatedS = s.update(s2)
print(s.update(s2))
print(mutatedS)
print(s)
print(s2)

# intersection() and intersection_update() both include the duplicates in the resulting set (returned itself with intersection() but None returned with intersection_update)
# "Only what intersects (matches) between the two sets"

# Such as with union() and update(), intersection() makes a new set but intersection_update() mutates the original set so that only the duplicate members are included in the original set:

# intersection()

# "A safe way to find the unique values in two sets to be joined"

notMutatedIntersectedSet = { "one", "two", 3, False, "duplicate", ()}
notMutatedIntersectedSet2 = { "a", "b", None, 2.3, "duplicate"}

notMutated = notMutatedIntersectedSet.intersection(notMutatedIntersectedSet2)
print(notMutated)
print(notMutatedIntersectedSet) # Shows original first set unchanged


# intersection_update()

mutatedIntersectedUpdatedSet = { "one", "two", 3, False, "duplicate", ()}
mutatedIntersectedUpdatedSet2 = { "a", "b", None, 2.3, "duplicate"}

mutated = mutatedIntersectedUpdatedSet.intersection_update(mutatedIntersectedUpdatedSet2)
print(mutated)
print(mutatedIntersectedUpdatedSet) # Shows original first set changed



# symmetric_difference(): mutates the first array to include all EXCEPT the duplicates

# "keep only what is unique between the two sets and returns this in a new set"


notMutatedUniqueItemsOnly = { "one", "two", 3, False, "duplicate", ()}

notMutatedUniqueItemsOnly_2 = { "a", "b", None, 2.3, "duplicate"}

notMutatedUnique = notMutatedUniqueItemsOnly.symmetric_difference(notMutatedUniqueItemsOnly_2)
print(notMutatedUnique)
print(notMutatedUniqueItemsOnly) # Shows original first set unchanged


# symmetric_difference_update(): mutates the first array to include all EXCEPT the duplicates

# "keep only what is unique in the two sets but just change the first set to do so, without returning a new set"

mutatedUniqueItemsOnly = { "one", "two", 3, False, "duplicate", ()}

mutatedUniqueItemsOnly_2 = { "a", "b", None, 2.3, "duplicate"}

mutatedUnique = mutatedUniqueItemsOnly.symmetric_difference_update(mutatedUniqueItemsOnly_2)
print(mutatedUnique)
print(mutatedUniqueItemsOnly) # Shows original first set changed
