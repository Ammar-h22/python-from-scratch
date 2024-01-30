# Tuple
# Tuple are the third type of data structure in python.
# A tuple is an immutable list means it is like a list but which cannot be changed
# So why do we need tuple?
# --> Tuples are more faster and have a greater performance as compared to lists.
# Also as tuples cannot be changed, they are more safer/secure compared to lists.

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[2])
print(5 in my_tuple)

# We can also use tuples inside dictionary:
user = {(1, 2): [1, 2, 3], "greet": "hello"}
print(user[(1, 2)])

# We can also do tuple slicing similar to lists:
print(my_tuple[1:4])

# Tuple unpacking similar to list unpacking:
x, y, z, *other = (1, 2, 3, 4, 5, 6, 7)
print(x)
print(other)

# Tuple methods
t1 = (1, 2, 3, 4, 5, 4, 2)
print(t1.count(4))
print(t1.index(5))
print(len(t1))
