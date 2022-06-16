
numbers = [1, 2, 3, 4, 5]
itrObj = iter(numbers)

while True:
    try:
        elem = next(itrObj)
        print(elem)
    except StopIteration:
        break

print("-" * 40)
