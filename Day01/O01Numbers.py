
"""
int
float
complex
"""

a = 10
b = -10

print(f"a :{a}")
print(type(a))                      # RTTI - runtime type indentification
print(f"b :{b}")
print(type(b))

c = 1.0
d = -1.0

print('-' * 40)
print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))

print('-' * 40)
e = 2e3
f = -2e3

print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(f))

print('-' * 40)
g = 3 + 2j
h = 3 - 2j

print(f'g :{g}')
print(type(g))
print(f"h :{h}")
print(type(h))

print('-' * 40)
x = 2 + 3.5             # x is flaot
print(f"x  :{type(x)}")

# conversion of number
a = 100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

# number system
print('-' * 40)
print(11)
print(0b11)         # binary
print(0b101)        # binary
print(0o11)         # octal
print(0o101)        # octal
print(0xe)          # hexa
print(0xa)          # hexa

print("Number system conversion".center(40, "-"))
a = 100
print(bin(a))
print(hex(a))
print(oct(a))
