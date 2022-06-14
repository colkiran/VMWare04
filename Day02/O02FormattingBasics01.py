
# emulate c style - printf
format = "Welcome %s, what a %s player"
print(f"format :{format}")
values = ("Sachin", "class")                # tuple
print(f"values :{values}")
print("-" * 40)

print(format % values)
print("-" * 40)

format = "Welcome %s, what a %s player with a rating of %.3f"
print(format % ("Sachin", "class", 4))
print(format % ("Sachin", "class", 4.789023))
print(format % ("Sachin", "class", 4.7999999))
print("-" * 40)

print("Welcome %s, what a %s player with a rating of %.3f" % ("Sachin", "class", 4.8))

# emulate unix shell syntax
from string import Template
import string as s
tmpl = Template("Welcome $name. what a $adj player")
print(f"tmpl :{tmpl}")
print(tmpl.substitute(name="Sachin", adj="super"))

# format of strings in python
print("=" * 40)
print("Welcome {}, what a {} player".format("Sachin", "class"))

print("Welcome {0}, what a {1} player from {2}".format("Sachin", "class", "India"))

print("Welcome {1}, what a {2} player from {0}".format("India","Sachin", "class"))

print("Welcome {pname}, what a {adj} player from {ctry}".format(ctry="India", pname="Sachin", adj="class"))

print("Welcome {pname}, Your rating of {rating}, what a {adj} player".format(pname="Sachin", rating=4, adj="class"))

print("Welcome {pname}, Your rating of {rating:.3f}, what a {adj} player".format(pname="Sachin", rating=4.7, adj="class"))

# Interpolation
print("Interpolation".center(40, "-"))
from math import pi, e
print(f"PI = {pi} and Eulers Constant = {e}")

print("PI = {} and Eulers Constant = {}".format(pi, e))
print("PI = {} and Eulers Constant = {} and Magic Number = {magic}".format(pi, e, magic=40585))
print("PI = {0} and Eulers Constant = {1} and Magic Number = {magic}".format(pi, e, magic=40585))

print("=" * 40)
full_name = ["Sachin", "Tendulkar"]                  # list
print(f"fullname :{full_name}")

print("Mr.{name}".format(name = full_name))
print("Mr.{name[0]}".format(name = full_name))
print("Mr.{name[0]} {name[1]}".format(name = full_name))

