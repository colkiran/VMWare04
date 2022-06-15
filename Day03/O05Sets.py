
s1 = set()
print(f"s1 :{s1}")
print(type(s1))

print("-" * 40)
s2 = {1, 2, 3}
print(f"s2 :{s2}")
print(type(s2))

print("-" * 40)
s3 = set(range(1, 11))
print(f"s3 :{s3}")
print(type(s3))

print("-" * 40)
s1 = {1, 2, 3}
print(f"s1 :{s1}")

print("add".center(40, "-"))
s1.add(2)
s1.add(5)
s1.add(4)
s1.add(1)
s1.add(3)
print(f"s1 :{s1}")

print("update".center(40, "-"))
print(f"s1 :{s1}")
s1.update([3, 4, 5])
s1.update([6, 7, 8])
s1.update([3, 6, 9])
s1.update([2, 4, 6, 8])
print(f"s1 :{s1}")

# remove elements from a set => pop, remove, discard
for i in s1:
    print(i, end=" ")
print()

print("pop".center(40,"-"))
res = s1.pop()
print(f"res :{res}")
res = s1.pop()
print(f"res :{res}")

print(f"s1 :{s1}")

print("remove".center(40, "-"))
print(f"s1 :{s1}")
res = s1.remove(4)
print(f'res :{res}')
s1.remove(8)
print(f"s1 :{s1}")
# s1.remove(2)

print("discard".center(40, "-"))
print(f"s1 :{s1}")
s1.discard(5)
s1.discard(7)
s1.discard(2)
print(f"s1 :{s1}")

print("-" * 40)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print("A union B :", A | B)
print("B union A :", B.union(A))

print("-" * 40)
print("A intersection B :", A & B)
print("B intersection A :", B.intersection(A))

print("-" * 40)
print("A difference B :", A - B)
print("B difference A :", B.difference(A))

print("-" * 40)
print("A symmetric difference B :", A ^ B)
print("B symmetric difference A :", B.symmetric_difference(A))

# frozen sets -> immutable
f = frozenset((1, 2, 3))
print(f"f :{f}")
print(type(f))

s1 = {1, 2, 3}
s2 =  s1.copy()
print(f"s1 :{s1}")
print(F"s2 :{s2}")

s1.add(4)
s1.add(5)
print(f"s1 :{s1}")
print(f"s2 :{s2}")

