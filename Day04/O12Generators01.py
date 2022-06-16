
lst1 = [x ** 2 for x in range(1, 11)]                       # comprehension
lst2 = (x ** 2 for x in range(1, 11))                       # generator

print(f"lst1 :{lst1}")
print(f"lst2 :{lst2}")
print(lst2.__next__())
print(lst2.__next__())
print(lst2.__next__())

print("-" * 40)
print(sum([x ** 2 for x in range(1, 11)]))
print(sum((x ** 2 for x in range(1, 11))))

print("-" * 40)
from sys import getsizeof
lst1 = [x ** 2 for x in range(1, 1000)]
lst2 = (x ** 2 for x in range(1, 1000))

print("Comprehension size of lst1 :", getsizeof(lst1))
print("Generator size of lst2 :", getsizeof(lst2))
