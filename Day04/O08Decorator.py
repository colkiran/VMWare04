
def doubleMesh(fnc):
    def helper(*args):
        print("=" * 40)
        fnc(*args)
        print("#" * 40)
    return helper

def startSingle(fnc):
    def helper(*args):
        print("*" * 40)
        fnc(*args)
        print("-" * 40)
    return helper

@startSingle
@doubleMesh
def fun(x, y):
    print(f"Hello World....{x}, {y}")

fun(10, 20)
