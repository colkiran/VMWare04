
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 40)
t2 = (1, 2, 3, 4, 5)
print(f"t2 :{t2}")
print(type(t2))

print("-" * 40)
t3 = tuple(range(1, 11))
print(f"t3 :{t3}")
print(type(t3))

print("-" * 40)
t4 = 1,
print(f"t4 :{t4}")
print(type(t4))

print("-" * 40)
t5 = 1, 2, 3
print(f"t5 :{t5}")
print(type(t5))

# tuple are immutable
t1 = (1, 2, 3, 4, 5)
print(f"t1 :{t1}")
print(f"t1[1] :{t1[1]}")
# t1[1] = 200

# count, index
# print(dir(t2))
t2 = (1, 2, 1, 2, 1, 1, 1, 2, 3, 1, 1, 2, 2, 1, 3, 1, 1, 1, 2, 3, 1)
print(f"t2 :{t2}")
print("1 :", t2.count(1))
print("2 :", t2.count(2))
print("3 :", t2.count(3))

print("index".center(40, "-"))
print("2 :", t2.index(2))
print("3 :", t2.index(3))
print("3 :", t2.index(3, 9))
print("3 :", t2.index(3, 15))
