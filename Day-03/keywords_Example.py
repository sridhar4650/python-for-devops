# as
import numpy as np

#and
x = 10
y = 5
print(x > 5 and y < 10)   # True

# or
x = 3
y = 10
print(x > 5 or y > 5)    # True

# not
is_active = False
print(not is_active)    # True

# if
age = 20
if age >= 18:
    print("Adult")

# else
age = 15
if age >= 18:
    print("Adult")
else:
    print("Minor")

# elif
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")

#while
count = 1
while count <= 3:
    print(count)
    count += 1

#for
for i in [1, 2, 3]:
    print(i)

#in
fruits = ["apple", "banana"]
print("apple" in fruits)   # True

#try
#except
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

#finally
try:
    x = 10 / 2
finally:
    print("This always executes")

#def
def add(a, b):
    return a + b

#return
def square(x):
    return x * x

print(square(4))   # 16

#class
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Sridhar")
print(p.name)

#import
import math
print(math.sqrt(16))   # 4.0

#from
from math import sqrt
print(sqrt(25))   # 5.0

#True
is_valid = True
print(is_valid)

#False
is_admin = False
print(is_admin)

#None
result = None
print(result)

#is
a = None
print(a is None)   # True

#lambda
add = lambda x, y: x + y
print(add(3, 4))   # 7

#with
with open("file.txt", "w") as f:
    f.write("Hello DevOps")

#global
x = 10

def update():
    global x
    x = 20

update()
print(x)   # 20

#nonlocal
def outer():
    x = 5
    def inner():
        nonlocal x
        x = 10
    inner()
    print(x)

outer()   # 10