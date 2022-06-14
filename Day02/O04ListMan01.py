
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, 'four', 'five', 'six', 7.1, 8.5, 9.0, 10j, 11+0j, True, False]
print(f"l2 :{l2}")
for i in l2:
    print(i, type(i))

print(type(l2))

print("-" * 40)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 40)
l4 = [1, 2, 3, 'four', 'five', 'six', 7.1, 8.5, 9.0, 10j, 11+0j, True, False]

# extract the elements of the list
print(f"l4[0] :{l4[0]}")
print(f"l4[10] :{l4[10]}")

l4[3] = 3.5
print(f"l4 :{l4}")
print("Length :", len(l4))

print("-" * 40)
l5 = [1, 2, 3, 4, 5, 'six', 'seven', 'eight', 'eight']
print(f"l5: {l5}")

print(f"l5[0] :{id(l5[0])}")
print(f"l5[1] :{id(l5[1])}")
print(f"l5[2] :{id(l5[2])}")

print("-" * 40)
# memory allocation is not contigious
print(f"{l5[4]} :{id(l5[4])}")
print(f"{l5[5]} :{id(l5[5])}")
print(f"{l5[7]} :{id(l5[7])}")
print(f"{l5[8]} :{id(l5[8])}")


l5 = [1, 2, 3, 4, 5, 'six', 'seven', 'eight']

print("-" * 40)
# memory allocation is not contigious
print(f"{l5[4]} :{id(l5[4])}")
print(f"{l5[5]} :{id(l5[5])}")
print(f"{l5[7]} :{id(l5[7])}")

print("-" * 40)
values = list(range(10, 40, 10))
print(f'values :{values}')

# unpack
a, b, c = values
print(a, b, c, sep=", ")

print("-" * 40)
values = list(range(10, 101, 10))
print(f"values :{values}")
a, b, *c = values
print(a, b, c, sep=", ")

a, *b, c = values
print(a, b, c, sep=", ")

*a, b, c = values
print(a, b, c, sep=", ")

print("-" * 40)
l1 = [1, 2, 3, 4, 5]
l2 = [11, 22, 33, 44, 55]

print(f"l1 :{l1}")
print(f"l2 :{l2}")

l3 = [l1, l2]
print(f"l3 :{l3}")

print("-" * 40)
l4 = [*l1, *l2]
print(f"l4 :{l4}")
