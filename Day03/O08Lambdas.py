
def add(x, y):
    return x + y

a = add
res = a(10, 20)
print(f"res :{res}")

print("-" * 40)
x = lambda a, b: a + b
res = x(30, 40)
print(f"res :{res}")

# map, filter and reduce
# map - expression will be implemented on every element of a list
l = list(range(1, 11))
print(f"l :{l}")

squares = list(map(lambda x: x ** 2, l))
print(f"squares :{squares}")

# temp in celsius, convert it into farenheit
temp = [10, 18, 20, 24.5, 28.7, 29.9, 32, 34, 38]

far = map (lambda x:(x * 1.8 + 32), temp)
print(f"Farenheit :{list(far)}")

print("-" * 40)
# sort these months according to the calendar
from calendar import month_name
months = ['aug', 'oct', 'dec', 'feb', 'sep', 'jan', 'apr', 'nov', 'mar', 'jun', 'may', 'jul']

print(f"months :{months}")
sortedMonths = sorted(months, key=list(map(lambda x: x.lower()[0:3], list(month_name))).index)
print(f"sortedMonths :{sortedMonths}")

print("-" * 40)
# Filters - expression should return a True or a False
l = list(range(1, 25))
print(f"l :{l}")

res = list(filter(lambda x: x % 3 == 0, l))
print(f"res :{res}")

print("-" * 40)
# reduce - import from functools module
from functools import reduce
l = [5, 8, 3, 6, 9, 7, 10, 4]
print(f"l :{l}")

res = reduce(lambda x, y: x if x > y else y, l)
print(f"res :{res}")

res = reduce(lambda x, y: x if x < y else y, l)
print(f"res :{res}")

res = reduce(lambda x, y: x + y, l)
print(f"res :{res}")









