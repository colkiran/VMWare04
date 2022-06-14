
print("index".center(40, "-"))
l1 = [1, 2, 1, 1, 1, 2, 3, 1, 1, 2, 1, 2, 2, 3, 1, 1, 1, 2, 3]
print(f"l1 :{l1}")

print(f"3 :{l1.index(3)}")
print(f"3 :{l1.index(3, 7)}")
print(f"3 :{l1.index(3, 14)}")

# print(f"4, {l1.index(4)}")
print("{:-^40}".format("count"))
l1 = [1, 2, 1, 1, 1, 2, 3, 1, 1, 2, 1, 2, 2, 3, 1, 1, 1, 2, 3]
print(f"l1 :{l1}")

print(f"1 :{l1.count(1)}")
print(f"2 :{l1.count(2)}")
print(f"3 :{l1.count(3)}")
print(f"4 :{l1.count(4)}")

print("copy".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 Before :{l1}")
l2 = l1                 # shallow copy - not only copies the data but also shares the addresses
print(f"l2 Before :{l2}")
l2.append(6)
l2.append(7)
l2.append(8)
print(f"l1 After :{l1}")
print(f"12 After :{l2}")

print("=" * 40)
l1 = [6, 7, 8, 9, 10]
print(f"l1 Before :{l1}")
l2 = l1.copy()                  # deep copy
print(f"l2 Befre :{l2}")

l2.extend([11, 12, 13, 14])
print(f"l1 After :{l1}")
print(f"l2 After :{l2}")

print("=" * 40)
l3 = [1, 2, 3, 4, [11, 22, 33, 44, 55], 5]
print(f"l3 Before :{l3}")
l4 = l3.copy()
print(f"l4 Before :{l4}")

l4[4].remove(33)
l4[4].remove(55)
print(f"l4 After :{l4}")
print(f"l3 After :{l3}")

print("=" * 40)
l6 = [11, 12, 13, [10, 20, 30, 40, 50], 14, 15]
print(f"l6  Before :{l6}")
from copy import deepcopy
l7 = deepcopy(l6)
print(f"l7 Before :{l7}")

l7[3].append(60)
l7[3].append(70)
print(f"l6 After :{l6}")
print(f"l7 After :{l7}")

