
print("{:-^40}".format("keys"))
player = {'name': 'Sachin', 'age' :32, 'runs': 85, 'oppn': 'Srilanka', 'venue': 'chepauk', 'year': 2003}
print(f"player :{player}")
print("-" * 40)

# keys
k = player.keys()
print(k)
print("-" * 40)
for k in player.keys():
    print(k +  " => " + str(player[k]))

print("values".center(40, "-"))
player = {'name': 'Sachin', 'age' :32, 'runs': 85, 'oppn': 'Srilanka', 'venue': 'chepauk', 'year': 2003}
print(f"player :{player}")

print("-" * 40)
v = player.values()
print(f"v :{v}")

# delete values of a dictionary
print("pop".center(40, "-") )
player = {'name': 'Sachin', 'age' :32, 'runs': 85, 'oppn': 'Srilanka', 'venue': 'chepauk', 'year': 2003}
print(f"player :{player}")

print("-" * 40)
res = player.pop('venue')
print(f"res :{res}")

res = player.pop('year')
print(f"res :{res}")

print(f"Player :{player}")

print('popitem'.center(40, "-"))
player = {'name': 'Sachin', 'age' :32, 'runs': 85, 'oppn': 'Srilanka', 'venue': 'chepauk', 'year': 2003}
print(f"player :{player}")

print("-" * 40)
res = player.popitem()
print(f"res :{res}")

res = player.popitem()
print(f"res :{res}")

print(f"player :{player}")
