
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)
d2 = {1 :"one", 2 :"two", 3 :"three", 4 :"four", 5 :"five"}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 40)
d3 = dict([('name', 'sachin'), ('runs', 125), ('oppon', 'Nzl'), ('venue', 'Auckland')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 40)
d4 = dict(name = 'Rahul', runs = 185, oppon = 'Eng', venue = 'Tent Bridge')
print(f"d4 :{d4}")
print(type(d4))


print("-" * 40)
# create
player = {'name': 'Sachin', 'runs': 85, 'oppn': 'Srilanka', 'venue': 'chepauk'}
print(f"player :{player}")

# read
print("-" * 40)
print(f"Name     :{player['name']}")
print(f"Opponent :{player['oppn']}")
print(f"Venue    :{player['venue']}")

# update
print("-" * 40)
player['runs'] = 89
player['year'] = 2003
print(f"player :{player}")

# delete
print("-" * 40)
print(f"player :{player}")
del player['oppn']
del player['year']
print(f"player :{player}")

print("-" * 40)
print(f'player :{player}')
player['age'] = None                # None is same as null
print(f'player :{player}')

print("-" * 40)
player = {'name': 'Sachin', 'age' :32, 'runs': 85, 'oppn': 'Srilanka', 'venue': 'chepauk', 'year': 2003}
print(f"player :{player}")

# iterate through the dictionary
for x in player:
    # print(x, end=" ")
    print(x, " => ", player[x])
print()

print("-" * 40)
# print(player["strike_rate"])
print(player.get('strike_rate', "Invalid key mentioned,Please enter a valid key"))
print(player.get('runs', "Invalid key mentioned,Please enter a valid key"))

print("-" * 40)
print(dir(player))
