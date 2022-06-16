
"""
1. outerFun is the parent of innerFun
2. code written in the innerFun is abstracted
3. we can call the innerFun code when needed

"""

# closures

def outerFun(name):                 # local variable
    gname = f"Mr.{name}"

    def innerFun():

        print("Hello World")
        print(f"Greetings {gname}")

    innerFun()

outerFun("Rahul")
