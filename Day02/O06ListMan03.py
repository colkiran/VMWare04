
l1 = list(range(1, 6))
print(f"l1 :{l1}")

# adding elements into a list
# append

print(f"l1 :l1")
l1.append(6)
l1.append(7)
l1.append(8)

print(f"l1 :{l1}")
l1.append([9, 10, 11, 12, 13])
print(f"l1 :{l1}")
print(f"l1[8][1:4] :{l1[8][1:4]}")

print("{:-^40}".format("extend"))
l2 = list (range(1, 4))
print(f"l2 :{l2}")

l2.extend([4, 5, 6])
l2.extend([7, 8, 9])
print(f"l2 :{l2}")

print("insert".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)

print(f"l1 :{l1}")

# remove elements from a list
print("{:-^40}".format("pop"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")
res = l1.pop(7)
print(f"res :{res}")
print(f"l1 :{l1}")

res = l1.pop()
print(f"res :{res}")
print(f"l1 :{l1}")

print("remove".center(40, "-"))
l1 = [1,2,3, 1, 2, 1, 2, 3, 2, 3, 2, 3, 4]
print(f"l1 :{l1}")

res = l1.remove(1)
# print(f"res :{res}")

print(f"l1 :{l1}")
l1.remove(2)
l1.remove(2)
print(f"l1 :{l1}")
# l1.remove(5)

l1 = [1, 2, 2, 1, 1, 1, 3, 1, 2, 3, 1, 1, 1, 1, 1, 1,1 , 2, 3, 1, 1, 1, 2]
# remove 1's from the list

print(f"l1 :{l1}")

res = set(l1)
print(f"res :{list(res)}")


while True:
    try:
        l1.remove(1)
    except ValueError:
        break

print(f"l1 :{l1}")



