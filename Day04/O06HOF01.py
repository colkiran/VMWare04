
def callMe():
    print("Apples from Ooty.....")

def fun(fnc):
    print("Hello....")
    fnc()               # call back
    print("Hi....")
    print("-" * 40)

    def defineMe():
        print("Oranges from Kanpur.......")

    return defineMe

def funCallBack(fnc):
    print("Mera Bharath Mahan.......")
    fnc()               # call back
    print("India is great........")


funCallBack(fun(callMe))

