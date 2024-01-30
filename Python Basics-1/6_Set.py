# Set (Unordered collection of unique objects)
# Set is the last datatype and the last data structure as well.

my_set = {1, 2, 3, 4, 5}
my_set.add(100)  # 100 will be added to the set
my_set.add(2)
# 2 will not be added because '2' is already present in the set and we know
# that set contains only unique elements
print(my_set)

# We can convert a list into a set so that all the duplicate values are removed
my_list = [1, 2, 3, 4, 4, 1]
print(set(my_list))
# We can also do vice-versa
print(list(my_set))

# As the elements in the set are not in the ordered manner, we cannot access them
# using indexing. Instead we can do:
set2 = {1, 5, 7, 9, 12}
print(20 in set2)

# len
print(len(set2))

new_set = set2.copy()
set2.clear()
print(new_set)
print(set2)

# Set methods:
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9}

# intersection
print(my_set.intersection(your_set))  # returns common elements
print(my_set & your_set)  # shortcut method

# union
print(my_set.union(your_set))  # adds all the elements but no duplicates
print(my_set | your_set)  # shortcut method

print(my_set.isdisjoint(your_set))
print(my_set.issubset(your_set))
print(my_set.issuperset(your_set))

print(my_set.difference(your_set))
# This just gives the difference without modifying the original set

my_set.difference_update(your_set)  # This modifies my_set
print(my_set)

