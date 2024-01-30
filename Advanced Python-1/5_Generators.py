# 1) Generators:
# Generators are available in python and it allow us to generate a sequence of values over time.

# 2) In Python, a generator is a special type of iterable, similar to lists, tuples, and dictionaries,
# but with a key difference: it generates values one at a time on-the-fly rather than storing them
# in memory all at once. This makes generators memory-efficient and particularly useful when
# dealing with large datasets or when you want to generate values dynamically.

# 3) Hence generators reduces the memory space and are more faster than iterables.

# 4) Generators are nothing but iterables. All generators are iterables but all iterables are not generators.
# Ex: range() is a generator and hence it is considered as an iterable, but
# list() is an iterable and it is not considered as a generator.


def simple_function(num):
    result = []
    for i in range(num):
        result.append(i)
    return result


s = simple_function(10)
print(s)  # This will print the values

# The above function is not very useful, but we can use generators instead!


# We can create our own generators, The common syntax to create generators is:
def generator_function(num):
    for i in range(num):
        yield i


g = generator_function(10)
print(g)  # This will not print the values, it will give/create the generator object.

# We can use the above created generator in 'for' loop to display the values.
for item in generator_function(10):
    print(item)  # This will print the values

# The yield statement is crucial because it allows the generator function to pause its execution,
# remember its state, and resume from where it left off when the next value is requested.
# This is what makes generators so powerful for working with sequences and potentially infinite data.


# In Python, the next() function returns the next value from an iterator or a generator.
# When you call next() on an iterator or a generator, it advances the iterators internal state
# and returns the next item in the sequence. If there are no more items to retrieve, it raises
# a StopIteration exception by default.
g = generator_function(5)
next(g)  # 0
next(g)  # 1
next(g)  # 2
next(g)  # 3
next(g)  # 4
# print(next(g))  # This will give error, because generator is exhausted.

# _____________________________________________________________________________________
# Let's see how generators perform better than iterables:
from time import time


# Decorator:
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        fn(*args, **kwargs)
        t2 = time()
        print(f"Took {t2-t1}")

    return wrapper


@performance
def func1():
    for i in range(100000000):
        i * 5


# func1()


@performance
def func2():
    for i in list(range(100000000)):
        i * 5


# func2()
# so we can see through the output that func1 performs better than func2.

# _____________________________________________________________________________________


# Let's see how for-loops work under the hood: (lets create our own)
def special_for_loop(iterable):
    iterator = iter(iterable)  # Or we can also do iterable.__iter__()
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break


special_for_loop([1, 2, 3, 4])


# Now lets see how range function works:
class MyGen:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(0, 15)
for i in gen:
    print(i)


# _____________________________________________________________________________________
# Excercise: (Fibonnaci number)
def fibonacci(num):
    a = 0
    b = 1
    for _ in range(num):
        yield a
        temp = a
        a = b
        b = temp + b


for i in fibonacci(21):
    print(i)


# Lets do using list instead of generator:
def fibonacci2(num):
    a = 0
    b = 1
    result = []
    for _ in range(num):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result


print(fibonacci2(21))

# _____________________________________________________________________________________
"""
Difference between Iterable/Iterator/Generator:

1. Iterable:
- An iterable is any Python object capable of returning its elements one at a time.
- You can iterate over an iterable using a loop (like `for`) or by explicitly converting it to an iterator using the `iter()` function.
- Common iterable objects include lists, tuples, strings, dictionaries.

Ex:
   my_list = [1, 2, 3, 4, 5]
   for item in my_list:
       print(item)

2. Iterator:
- An iterator is an object representing a stream of data, allowing you to traverse through its elements one at a time.
- Iterators have two essential methods: `__iter__()` (to return itself) and `__next__()` (to retrieve the next element).
- When you use a `for` loop, Python automatically converts an iterable into an iterator and 
  calls `__iter__()` and `__next__()` behind the scenes.

Ex:
   my_iter = iter(my_list)
   print(next(my_iter))  # Output: 1
   print(next(my_iter))  # Output: 2
   

3. Generator:
- A generator is a type of iterator, but it is defined using a function with the `yield` keyword. Generator functions return a generator iterator.
- Generators allow you to create iterators on-the-fly and generate values lazily (one at a time) instead of generating and storing all values in memory.
- They are particularly useful for handling large data sets or infinite sequences.

Ex:
   def countdown(n):
       while n > 0:
           yield n
           n -= 1

   gen = countdown(3)
   print(next(gen))  # Output: 3
   print(next(gen))  # Output: 2


- Relationship:

- All generators are iterators, but not all iterators are generators. 
Generators are a specific type of iterator that is created using generator functions.

- All iterables are not necessarily iterators. Iterables are objects that you can iterate over,
but they may not necessarily implement the `__next__()` method required to be an iterator.
For example, a list is iterable, but you can't call `next()` directly on it.

To summarize, iterables are objects you can loop over, iterators are objects that allow you to
traverse elements one at a time, and generators are a type of iterator created using generator 
functions, which enable lazy and efficient generation of values.
"""

# Last example to show the use of generators:


# Normal function
def my_func(n):
    list = []
    for i in range(n):
        list.append(i**2)
    return list


print(my_func(10))


# Generator function
def my_func2(n):
    for i in range(n):
        yield i**2


fn = my_func2(10)
print(next(fn))
print(next(fn))
print(next(fn))
print(next(fn))
print(next(fn))
print(next(fn))

# So using generators we can access the items one at a time

