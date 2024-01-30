# List (An ordered sequence of elements)
# In python lists are nothing but arrays
# List is a datatype and also the first data structure in python

li = [1, 2, 3, 4, 5]
li2 = ["a", "b", "c"]
li3 = [1, 2.5, True]

# list slicing   (Similar to string slicing)
print(li[0:4:1])

# We can also access the elements of lists similarly using index like we
# do in strings, but the main difference b/w strings and lists is that
# strings are immutable and lists are mutable.

amazon_cart = ["notebooks", "smart watch", "sunglasses", "grapes"]
amazon_cart[0] = "laptop"
print(amazon_cart)

# Difference b/w copying and modifying the lists:
new_cart = amazon_cart[:]  # This is copying the list
new_cart[0] = "baloons"
print(amazon_cart)
print(new_cart)
# vs
new_cart = amazon_cart  # This is modifying the list
new_cart[0] = "baloons"
print(amazon_cart)
print(new_cart)

# Matrix
matrix = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
print(matrix[0][1])

# List methods
# 1) Adding
basket = [1, 2, 3, 4, 5]
basket.append(6)
basket.insert(4, 100)
basket.extend([7, 8, 9])
print(basket)

# 2) Removing
basket.pop(1)  # Here, 1 is the index in array
basket.remove(3)  # Here, 3 is the element in array
basket.clear()
print(basket)

# index()
basket2 = ["a", "b", "c", "d", "e", "d"]
print(basket2.index("d"))

# This is very useful to check if an element is present in the list or not
print("c" in basket2)

# We can similarly do for strings:
print("e" in "Hii, my name is Ammar")

# count()
print(basket2.count("d"))

# sort()
basket2.sort()
print(basket2)
# This method sorts the original existing list, whereas there is a function which
# copy the original list and then sorts the new list
print(sorted(basket2))

new_basket = basket2[:]
# As we know we do this to copy a list, we can also do by using a method
new_basket = basket2.copy()

# reverse()
basket2.reverse()  # This reverses the list in place
print(basket2)

# We can also reverse a list using list slicing
print(basket2[::-1])  # This reverses the list by creating a new one

# Also if we want to create a list very fast then we can do it using "range":
print(list(range(0, 100)))
# This will create a list of numbers from 0 to 99

# Mostly we can see that people wants to create a string out of a list:
sentence = " ".join(["Computer", "engineering", "is", "amazing"])
print(sentence)

# List unpacking: (The process of splitting the packed values into individual elements)
a, b, c, *other = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
