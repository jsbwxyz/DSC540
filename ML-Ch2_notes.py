import math
from sys import getsizeof
from itertools import repeat

#####
#   ITERATORS
#####

# Using a conventional for loop
# big_list_of_numbers = [1 for x in range (0, 10000000)]

# Returning number size in bytes
# print(getsizeof(big_list_of_numbers))

# Using repeat() method from intertools to save memory
# small_list_of_numbers = repeat(1, times=10000000)
# print(getsizeof(small_list_of_numbers))

##### 
# STACKS
#####

# Stacks are similar to lists, but with the restriction called Last In First Out (LIFO)
#   This means an element that comes in last goes out first whena  value is read from a stack

import pandas as pd

stack = []


# # We can use append() to add elements to the stack
# stack.append('my_test@test.edu')
# stack.append('rahul.subhramanian@test.edu')
# stack.append('sania.test@test.edu')
# stack.append('alec_baldwin@test.edu')
# stack.append('albert90@test.edu')
# stack.append('stewartj@test.edu')
# # print(stack)

# stack.append("Hello@test.com")

# # Use pop() to read values from the stack
# tos = stack.pop()
# print(tos)
# print(stack)

# Implementiung a stack with User-Defined methods
def stack_push (s, value):
    return s + [value]
def stack_pop (s):
    tos = s[-1]
    del s[-1]
    return tos
url_stack = []

# Ensure the variables exist
print(url_stack)

wikipedia_datascience = """Data science is an interdisciplinary
field that uses scientific methods, processes, algorithms and systems
to extract knowledge [https://en.wikipedia.org/wiki/Knowledge] and
insights from data [https://en.wikipedia.org/wiki/Data] in various
forms, both structured and unstructured,similar to data mining
[https://en.wikipedia.org/wiki/Data_mining]"""

# print(len(wikipedia_datascience))

# Splitting the STRING into a LIST with the .split() method
wd_list = wikipedia_datascience.split()
# print(len(wd_list)) # Should be 34

# To check whether an element on the list as a URL
#   we will use .startswith("[https://]"):
for word in wd_list:
    if word.startswith("[https://]"):
        url_stack = stack_push(url_stack, word[1:-1])
        print(word[1:-1])

# print(url_stack)

# Lambda creates an anonymous function without a name
def my_sine():
    return lambda x: math.sin(math.radians(x))
def my_cosine():
    return lambda x: math.cos(math.radians(x))

# "return" is not needed in a lambda function
#   because returning is assumed
sine = my_sine()
cosine = my_cosine()

print(math.pow(sine(30), 2) + math.pow(cosine(30), 2))

# LAMBDA for sorting

# Lambdas can take on or more inputs
#   Can be used to reverse sort 

capitals = [("USA", "Washington"), ("India", "Delhi"), ("France",
"Paris"), ("UK", "London")]

print(capitals)

# MULTI ELEMENT MEMBERSHIP CHECKING

# Validate that all elements in the first list are present in the second list
list_of_words = ["Hello", "there.", "How", "are", "you", "doing?"]
print(list_of_words)


check_for = ["How", "are"]
check_for

# THE "ALL()" FUNCTION
# All function returns True if all element of the iterable are True

all(w in list_of_words for w in check_for)

#####
# QUEUE
#####

# Creating a queue
queue = []
for i in range(0, 100000):
    queue.append(i)
print("Queue created")
# print(queue)

# Emptying the queue
for i in range(0, 100000):
    queue.pop(0)
print("Queue emptied")
queue

