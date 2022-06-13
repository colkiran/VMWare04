"""
1. Arithmetic
2. Comparison or relational
3. Logical
4. Bitwise
5. Ternary

"""

print("Arithmetic operators".center(40, "-"))
print(f"Add :{10 + 3}")
print(f"Sub :{10 - 3}")
print(f"Mul :{10 * 3}")
print(f"Div :{10 / 3}")
print(f"Flr Div :{10 // 3}")
print(f"Mod :{10 % 3}")
print(f"Exp :{10 ** 3}")

print('-' * 40)
print("Augmentor".center(40, "-"))
# =, +=, -=, *=
x = 10
print(f"x :{x}")
x += 5
print(f"x :{x}")
x /= 3
print(f"x :{x}")


print("Comparisom".center(40, "-"))
# ==,  >=, <=, !=
a = 10
b = 20
print(f"a :{a}, b :{b}")
print(f"a == b :{a == b}")
print(f"a >= b :{a >= b}")
print(f"a <= b :{a <= b}")
print(f"a != b :{a != b}")

print("Logical operators".center(40, "-"))
a = 10
b = 20

print(a < b and  a != b)
print(a > b and  a != b)
print(a > b and  a == b)
print(a < b or  a != b)
print(a < b or  a > b)
print(a > b or  a < b)
print(a > b or  a == b)

print(not(a <= b))
print(not(a >= b))

print('-' * 40)
print(f"a :{ord('a')}")
print(f"z :{ord('z')}")
print(f"A :{ord('A')}")
print(f"Z :{ord('Z')}")

print("Bitwise operators".center(40, "-"))
print(f"5 | 3 = {5 | 3}")
print(f"5 & 3 = {5 & 3}")
print(f"5 ^ 3 = {5 ^ 3}")
print(f"5 << 1 = {5 << 1}")
print(f"8 << 1 = {8 << 1}")
print(f"5 << 2 = {5 << 2}")
print(f"16 >> 1 = {16 >> 1}")
print(f"5 >> 1 = {5 >> 1}")

print(f"~0 :{~0}")
print(f"~5 :{~5}")

print("Ternary".center(40, "-"))
age = 19
print("Eligible" if age >= 18 else "Not Eligible")
