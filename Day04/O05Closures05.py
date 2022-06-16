
def fun(*args):
    print(args)
    print("-" * 40)

fun()
fun(1)
fun(1, 2)
fun(1, 2, 3)
print("-" * 40)

def sum(x, y):
    print(f"adding {x} and {y}")
    return x + y

def diff(x, y):
    print(f"subtracting {x} and {y}")
    return x - y

def log_details(fnc):
    logInfo = "Logging into the service....."

    def innerFun(*args):
        print(logInfo)
        print(fnc(*args))
        print("-" * 40)

    return innerFun

sum_logger = log_details(sum)
diff_logger = log_details(diff)

sum_logger(10, 20)
diff_logger(30, 14)
