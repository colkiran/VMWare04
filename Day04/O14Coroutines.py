
def get_name(surname):
    print(f"Surname is  {surname}")
    while True:
        name = yield
        print(f"received {name}")
        print("-" * 40)
        if surname in name:
            print(f"surname {surname} matched in {name}.......")

coObj = get_name("Pillai")
print(coObj)
coObj.__next__()
coObj.send("Sachin Tendulkar")
coObj.send("Rahul Dravid")
coObj.send("Virat Kholi")
coObj.send("Dhanraj Pillai")

