
d1 = [(x, y) for x in range(3) for y in range(3)]
print(f"d1 :{d1}")
print("-" * 40)

d2 = [(x, y) for x in range(1, 6) for y in range(1, x+1)]
print(f"d2 :{d2}")
print("-" * 40)

for x, y in d2:
    print(x, y)

print([x ** 2 if x % 2 == 0 else x ** 3 for x in range(1, 11)])

players = {
    'sachin': (280, 345, 250, 410, 320),
    'sourav': (310, 225, 180, 265, 385),
    'rahul': (230, 260, 350, 150, 198),
    'sehwag': (175, 375, 450, 340, 230),
    'yuvraj':(120, 180, 280, 250, 150)
}

print(f"players :{players}")
print("-" * 40)

print("Sachin :", sum(players['sachin']))
print("-" * 40)

scores = {k :sum(v) for k, v in players.items()}
print(f"scores :{scores}")
print("-" * 40)

scores = {k :(lambda scores: sum(scores) / len(scores))(v)
           for k, v in players.items()}
print(f"scores :{scores}")
print("-" * 40)

scores = [score for score in players.values()]
print(f"scores :{scores}")
print("-" * 40)

scores = [scr for score in players.values() for scr in score]
print(f"scores :{scores}")
print("-" * 40)

scores = [scr for score in players.values() for scr in score if scr >= 200]
print(f"scores :{scores}")
print("-" * 40)

scores = {name : [scr for scr in score if scr >= 200]
          for name, score in players.items()}
print(f"scores :{scores}")
