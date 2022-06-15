
glbX = 100

def OuterFun(name):                     # local variables
    gname = f"Mr. {name}"               # local variables

    def InnerFun():
        nonlocal gname                  # only local variables can be converted into non local
        gname = "Mr. Virat"             # local variable
        print("Hello World")
        print(f"Hello {gname}")
        print("Inner :",glbX)

    # from outerfun
    InnerFun()
    print(f"OuterFun :{gname}")

OuterFun("Rahul")