
def timeCalc(fnc):

    def innerFun():
        from datetime import datetime
        st = datetime.now()
        fnc()
        et = datetime.now()
        print(f"The total time taken by function '{fnc.__name__}' to execute is {(et - st)}")

    return innerFun

@timeCalc
def fun():
    l = []
    for i in range(1, 8000):
        for j in range(1, i+1):
            l.append(j ** 2)

fun()
