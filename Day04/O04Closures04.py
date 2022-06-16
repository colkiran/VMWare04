
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(name):
            import emojis
            emojized = emojis.encode(greet + " :" + sep + ": " + name)
            print(emojized)

        return innerMostFun

    return innerFun

KanGrt = outerFun("Namaskara")
TigerEmj = KanGrt("tiger")

TigerEmj("Prabhakar")


EngGrt = outerFun("Welcome")
GodEmj = EngGrt("lion")

GodEmj("Sachin")

"""
infun = outerFun("Welcome")
inmfun = infun("----->")
inmfun("Sachin")

kanGrt = outerFun("Namaskara")
tamilGrt = outerFun("Vanakam")

siglelnArwt = tamilGrt("----->")
dbllnArwt = tamilGrt("======>>")

siglelnArwk = kanGrt("----->")
dbllnArwk = kanGrt("======>>")

siglelnArwk("Kumble")
dbllnArwt("Ashwin")
"""