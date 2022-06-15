
fruits = [
    ('apple', 280),
    ('orange', 160),
    ('pine', 85),
    ('Watermelon', 70),
    ('Gauva', 120),
    ('grapes', 105),
    ('banana', 65)
]

prices = ['fruits' for fruit in fruits]
print(f"prices :{prices}")
print("-" * 40)

prices = [fruit for fruit in fruits]
print(f"prices :{prices}")
print("-" * 40)

prices = [fruit[0] for fruit in fruits]
print(f"prices :{prices}")
print("-" * 40)

prices = [fruit[1] for fruit in fruits]
print(f"prices :{prices}")
print("-" * 40)

prices = [fruit[1] * 0.9 for fruit in fruits]
print(f"prices :{prices}")
print("-" * 40)

prices = [fruit[1] * 0.75 for fruit in fruits]
print(f"prices :{prices}")
print("-" * 40)

expensiveItm = [fruit for fruit in fruits if fruit[1] >= 100]
print(f"Expensive Item :{expensiveItm}")
print("-" * 40)

expensiveItm = [[fruit[0], fruit[1], fruit[1] * 0.75, fruit[1] * 0.9]
                    for fruit in fruits if fruit[1] >= 100]
print(f"expensive item :{expensiveItm}")

print("-" * 40)
sentence  = "the quick brown fox jumps over the lazy dog"
words = [word for word in sentence.split()]
print(f"words :{words}")
print("-" * 40)

words = [word for word in sentence.split() if word != "the"]
print(f"words :{words}")
print("-" * 40)

words = [(word, len(word)) for word in sentence.split() if word != 'the']
print(f"words :{words}")
print("-" * 40)