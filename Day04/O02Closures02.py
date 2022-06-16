
# closure
def outerFun(name):                # HOF - Higher order function
    gname = f"Mr.{name}"

    def innerFun():

        print("Hello World")
        print(f"Greetings {gname}")

    return innerFun

outerFun("Rahul")                  # nothing will happen
print("-" * 40)

print(outerFun.__name__)
print(outerFun("Sachin").__name__)

print("-" * 40)
outerFun("Sachin")()               # calling the innerFun directly

print("-" * 40)
infun = outerFun("Rahul")

print("Before executing the innerFun.....")
infun()

print("-" * 40)

def addMe(x, y):
    return x + y

res = addMe(20, 30)
print(f"res :{res}")

