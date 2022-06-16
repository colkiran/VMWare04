
def outerFun(greet):

    def innerFun(name):
        print(greet, name)

    return innerFun

outerFun("Welcome")("Sachin")
print("-" * 40)

# curry
# simple curry
kanGrt = outerFun("Namaskara")
tamilGrt = outerFun("Vanakam")
spanGrt = outerFun("Hola")

# Dish
kanGrt("Rahul")
tamilGrt("Dhoni")
spanGrt("Messi")