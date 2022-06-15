
from collections import namedtuple
def ArithmeticCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    nmdTpl = namedtuple("ArithmaticCalc", "sum diff prod quot")
    arthCalc = nmdTpl(sum, diff, prod, quot)
    return arthCalc

res = ArithmeticCalc(20, 8)
print(f"res :{res}")
print(f"Sum :{res.sum}")
print(f"Diff :{res.diff}")
print(f"Prod :{res.prod}")
print(f"Quot :{res.quot}")

print("-" * 40)
def fun1():
    """ this is a comment
    This is the docstring for function fun1"""
    print("Hello World")

fun1()
print(fun1.__doc__)             # document String

print("-" * 40)
def fun2(x, y):
    """
        fun2 (x, y)

        sum_of_x_and_y = fun2(x, y)

        x and y are integers
        function fun2 takes two integer arguments and
        returns the sum of the numbers passed

    """
    return x + y

res = fun2(40, 70)
print(f"res :{res}")
print("-" * 40)

help(fun2)
