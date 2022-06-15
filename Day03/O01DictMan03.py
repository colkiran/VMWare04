
# convert a list into a dictionary, elements of the list should be taken as keys of dictionary

cities = ['blr', 'che', 'mum', 'del', 'hyd', 'kol', 'pun']
print(f"cities :{cities}")
print(type(cities))

print("-" * 40)
res = dict.fromkeys(cities)
print(f"res :{res}")

res = dict.fromkeys(cities, 22)
print(f"res :{res}")

print("{:-^40}".format("sefdefault"))
player = {'name': 'Rahul', 'age': 34, 'year': 2003}
print(f"player :{player}")

player.setdefault('runs', 65)
res = player.setdefault("year", 2008)
print(f"player :{player}")
print(f"res :{res}")

print("items".center(40, "-"))
# items = keys + values

players = {
    'ply1' :{'pname': 'Virat', 'age': 34, 'odi': 12450, 'test': 8500, 't20': 5400, 'team': 'RCB'},
    'ply2' :{'pname': 'Rohit', 'age': 33, 'odi': 10150, 'test': 4100, 't20': 5000, 'team': 'MI'},
    'ply3' :{'pname': 'Dhoni', 'age': 39, 'odi': 11300, 'test': 6500, 't20': 4800, 'team': 'CSK'}
}

print(f"Players :{players}")
print("-" * 40)

print(f"pyl1 :{players['ply1']}")
print(f"pyl2 :{players['ply2']}")
print(f"pyl3 :{players['ply3']}")

print("-" * 40)
for ky, info in players.items():
    print(ky)
    print("-----")
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 40)

print("update".center(40, "-"))

ply1 =  {'pname': 'Virat', 'age': 34, 'odi': 12450, 'test': 8500, 'team': 'RCB'}
ply2  = {'pname': 'Rohit', 'age': 33, 'odi': 10150, 'test': 4100, 't20': 5000}

print(f"ply1 :{ply1}")
print(f"ply2 :{ply2}")
# Updating ply1 with ply2 details
ply1.update(ply2)
print(f'ply1 :{ply1}')

print("clear".center(40, "-"))
ply1 =  {'pname': 'Virat', 'age': 34, 'odi': 12450, 'test': 8500, 'team': 'RCB'}

print(f"ply1 Before:{ply1}")

ply1.clear()

print(f"ply1 After :{ply1}")






