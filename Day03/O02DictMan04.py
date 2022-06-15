
print("Copy".center(40, "-"))
player1 = {'name': 'Rahul', 'runs': 80, 'oppn': 'Aus', 'venue': 'Gabba'}
print(f"player1 Before :{player1}")
player2 = player1               # shallow copy
print(f"player2 Before :{player2}")

print("-" * 40)
player2['year'] = 2009
player2['age'] = 36

print(f"player1 After :{player1}")
print(f"player2 After :{player2}")

print("copy".center(40, "-"))
player3 = {'name': 'Rahul', 'runs': 80, 'oppn': 'Aus', 'venue': 'Gabba'}
print(f"player3 :{player3}")
player4 = player3.copy()                # deep copy
print(f"player4 :{player4}")

print("-" * 40)
player4['age'] = 34
player4['name'] = 'Sehwag'

print(f"player4 After :{player4}")
print(f"player3 After :{player3}")

print("multidimensional".center(40, "-"))
player5 = {'name': 'Rahul', 'runs': {'first':80, 'second':145, 'third': 60} , 'oppn': 'Aus',
           'venue': ['Gabba', 'Perth', 'MCG']}
print(f"player5 Before :{player5}")
player6 = player5.copy()
print(f"player6 Before :{player6}")

print("-" * 40)
player6['runs']['fourth'] = 15
player6['runs']['fifth'] = 90
player6['venue'].append('SCG')
player6['venue'].append('Adelaide')

print(f"player6 After :{player6}")
print(f"player5 After :{player5}")

print("deepcopy".center(40, "-"))
player7= {'name': 'Rahul', 'runs': {'first':80, 'second':145, 'third': 60} , 'oppn': 'Aus',
           'venue': ['Gabba', 'Perth', 'MCG']}
print(f"player7 Before :{player7}")
from copy import deepcopy
player8 = deepcopy(player7)
print(f"player8 Before :{player8}")

print("-" * 40)
player8['runs']['fourth'] = 15
player8['runs']['fifth'] = 90
player8['venue'].append('SCG')
player8['venue'].append('Adelaide')

print(f"player8 After :{player8}")
print(f"player7 After :{player7}")
