
glbX = 100              # global variable

def fun(a):             # local variable
    global glbX
    glbX = 500
    print(f"glbX Inside :{glbX}")
    # glbX = 500          # local variable
    print(f"a :{a}")

print(f"glbX Before :{glbX}")

fun(50)

print(f"glbX After :{glbX}")
