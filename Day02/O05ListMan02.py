
letters = ['a', 'b', 'c','d', 'e']
print(f"letters :{letters}")

letter = enumerate(letters)
print(f"letter :{list(letter)[0]}")


for letter in letters:
    print(letter, end=" ")
print()

print("-" * 40)
for letter in enumerate(letters):
    print(letter, end=" ")

print("-" * 40)
for letter in enumerate(letters):
    print(letter[0], letters)

print("-" * 40)
for index, letter in enumerate(letters):
    print(index, letter)

print("-" * 40)
for letter in enumerate(letters):
    print(letter[0], letter[1])

print("-" * 40)
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"my_list :{my_list}")

for lst in my_list:
    print(lst)

print("-" * 40)

for ind, lst in enumerate(my_list):
    print(f"{ind} \t {lst}")

print("-" * 40)
for ind, lst in enumerate(my_list):
    print(f"List({ind})")
    for indx, num in enumerate(lst):
        print(f"\t {indx} \t {num}")
print()

print("-" * 40)
for lst in my_list:
    for num in lst:
        print(num, end=" ")
    print()

print(dir(letters))

