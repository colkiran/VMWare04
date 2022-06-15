
def greet():
    print("Greetings Mr.Sachin, Welcome to te event.......")

def greetGst(gname):
    print(f"Greetings {gname}, Welcome to the event.......")

# gname is non default argument, city is a default argument
def greetGstCity(gname, city="Mumbai"):
    print(f"Greetings {gname} from {city}, Welcome to the event.........")

greet()
greetGst("Mr.Sachin")
greetGst("Mr.Rahul")

print("-" * 40)
greetGstCity("Sachin")
greetGstCity("Rohit")
greetGstCity(city="Delhi", gname="Virat")

print("-" * 40)
def admission(sname, dob, fname, conno, addr, city, edqlf):
    print(f"Name is {sname}")
    print(f"DOB :{dob}")
    print(f"fname :{fname}")
    print(f"contact no :{conno}")
    print(f"address :{addr}")
    print(f"City :{city}")
    print(f"qualification :{edqlf}")

admission(city="Pune", addr="8th Cross, 3rd Main, Indiranagar", sname="Jack", conno="992920020",
          fname="Gibson", edqlf="10th Std", dob="12/05/2001")

print("-" * 40)
def multiplyMe(x, y):
    return x * y

res = multiplyMe(20, 40)
print(f"res :{res}")

# recursive calls
# find the factorial of a number, fibanocci series
print("-" * 40)
def fun(x):
    if x > 0:
        fun(x - 1)
        print(x, end=" ")

fun(10)
print()

# factorial of a number
print("-" * 40)
def factorial (n):
    if n ==1:
        return n
    else:
        return n * factorial(n-1)

# x = int(input("Enter a number to find its factorial :"))
# print(f"The factorial of {x} is  :{factorial(x)}")

# fibanocci series
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

# terms = int(input("Enter the terms to generated :"))
print("Fibanocci Series :")
# for i in range(terms):
#     print(fibo(i), end=" ")
# print()

# variable length arguments
print("-" * 40)
print("-" * 40)

values = range(10, 101, 10)
a, b, *c = values
print(a, b, c, sep=", ")

print("-" * 40)
def productAll(*numbers):
    print(numbers)
    prod = 1
    for num in numbers:
        prod *= num         # prod = prod * num
    return prod

res = productAll(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 40)
def extract_details(**details):
    print(details)
    print(f"Name     :{details['name']}")
    print(f"Opponent :{details['oppn']}")

extract_details(name="Sachin", score=98, oppn="Sri Lanka", venue="Gale")

print("-" * 40)
def enrollment(name, *tech, **marks):
    print(f"Name :{name}")
    print(f"tech :{tech}")
    print(f"Marks :{marks}")


enrollment("David", 'C', 'C++', 'C#', 'vb.net', 'asp.net', 'angularJS', 'ReactJS',
           Xth='87%', XIIth='89%', degree='72%', pg='85%')
