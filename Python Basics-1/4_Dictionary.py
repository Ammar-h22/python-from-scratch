# Dictionary (An unordered key value pair)
# In other languages Dictionary is mostly known as hash table or map.
# It is the second data structure in python after lists.

dictionary = {"a": 1, "b": 2}

# We can insert list inside a dictionary
dictionary2 = {"a": [1, 2, 3], "b": "Hello", "c": True}
print(dictionary2["a"][1])

# Similarly we can also insert dictionary inside a list
my_list = [
    {"a": [1, 2, 3], "b": "Hello", "c": True},
    {"a": [4, 5, 6], "b": "Byeee", "c": False},
]
print(my_list[0]["a"][2])


# Note that dictionary keys always need to be immutable and it should be unique,
# If you try to add duplicate keys then only last one will get stored into dictionary.
# We can keep keys as strings, integers, booleans, tuples as all of these are immutable,
# hence we cannot use list as a key because they are mutable.
# Most of the time we always use string to be as a key.
dict1 = {123: [1, 2, 3], True: "Hello", "Name": "Ammar"}
print(dict1[123])

# We can also create a dictionary using dict() built-in function
user = dict(name="Ammar", age=21)
print(user)
# But this is not widely used

# Dictionary methods
user2 = {"basket": [1, 2, 3], "greet": "hello", "age": 21}
print(user2.get("greet"))  # This will return the value of that particular key
print(user2.keys())  # This will return all the keys
print(user2.values())  # This will return all the values
print("basket" in user2.keys())
print("hello" in user2.values())
print(user2.items())

print(user2.pop("age"))
# This will remove the 'age' key:value pair and will return its value
print(user2.popitem())
# This will by-default remove the last key:value pair and will return the pair

# This will update the value and if the given key is not present in the dictionary
# then it will insert the given key
user2.update({"age": 41})
print(user2)

user2.clear()
print(user2)

