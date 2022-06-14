
# Conversions
print("Conversions".center(40, "-"))
print("{val} {val} {val}".format(val="A"))
# s = string, r = raw string, a = ascii
print("{val!s} {val!r} {val!a}".format(val="A"))

print("=" * 40)
print("The number is :{num} {num} {num}".format(num = 36))
print("The number is :{num} {num:f} {num:b}".format(num = 36))
print("The number is :{num:10} {num:f} {num:b}".format(num = 36))
print("The number is :{num:5} {num:f} {num:b}".format(num = 36))
print("The number is :{num:5} {num:f} {num:b}".format(num = 367879754233))
print("The number is :{num:5} {num:f} {num:.0f}".format(num = 36.456))

# Alignment
print("Alignment".center(40, "-"))
print("{num:15}Tendulkar".format(num=3))
print("{num:15}Tendulkar".format(num="Sachin"))
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

print("-" * 40)
from math import pi
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))
print("{pi:10.5}".format(pi=pi))

print("=" * 40)
print("{pi:10.3}".format(pi=pi))
print("{pi:010.3}".format(pi=pi))
print("{pi:010.4}".format(pi=pi))
print("{pi:010.5}".format(pi=pi))

print("One googol is {}".format(10 ** 100))
print("One googol is {:,}".format(10 ** 100))

print("=" * 40)
print("{}".format(pi))
print("{:10.2f}".format(pi))
print("{:<10.2f}Sachin".format(pi))
print("{:^10.2f}Sachin".format(pi))
print("{:>10.2f}Sachin".format(pi))

print("=" * 40)
# Sachin Tendulkar      => Sachin should get left, center and right aligned

print("{:<15} Tendulkar".format("Sachin"))
print("{:^15} Tendulkar".format("Sachin"))
print("{:>15} Tendulkar".format("Sachin"))

print("-" * 40)
print("{:-^40}".format("Hello World"))
print("hello world".center(40, "-"))


