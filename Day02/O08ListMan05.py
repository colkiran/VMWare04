
"""
l1 = list(range(1, 11))
print(f"l1 Before :{l1}")

l1.clear()
print(f"l1 After :{l1}")


print("reverse".center(40, "-"))
l1 = list(range(1, 11))
print(f"l1 Before :{l1}")

# reverse - reverse the original list
# reversed - reverse the list and returns a copy of it, original list will remain the same

l1.reverse()
print(f"l1 :{l1}")

print("-" * 40)
res = reversed(l1)
print(f"res :{list(res)}")

print('sort'.center(40, "-"))

# sort, sorted

l1 = [5, 7, 9, 3, 6, 10, 4]
print(f"l1 :{l1}")

srtLst = sorted(l1)
print(f"sorted list :{srtLst}")

srtLst1 = sorted(l1, reverse=True)
print(f"reverse sorted list :{srtLst1}")

print("-" * 40)
l1 = [5,'zebra', 'apple', 7, 'xmas', 'blue', 9, 'yellow', 'green', 3,'violet', 'pink',6,
      'dog', 'kite', 10, 'hen', 'mango', 4, 'egg', 1, 'frog', 2, 8, 195, 1120, 10851, 29, 203,
      2145, 37, 310, 3241]
print(f"l1 :{l1}")

print("-" * 40)
srtLst = sorted(l1, key=ascii)
print(f"sorted list :{srtLst}")

cities = ['kanyakumari', 'bangalore', 'hyderabad', 'delhi', 'ooty', 'vishakapatnam', 'pune', 'mumbai',
          'kolkota', 'thiruvananthapuram', 'mysore', 'coimbatore', 'chandigarh']

print("-" * 40)
srtCities = sorted(cities, key=len)
print(f"Sorted :{srtCities}")

srtCities = sorted(cities, key=len, reverse=True)
print(f"Sorted :{srtCities}")

print("-" * 40)

"""
from calendar import month_name
# print(list(month_name))

def sortMonth(mon):
    l = []
    for m in list(month_name):
        l.append(m[0:3].lower())
    if mon in l:
        return l.index(mon)


months = ['aug', 'oct', 'dec', 'feb', 'sep', 'jan', 'apr', 'nov', 'mar', 'jun', 'may', 'jul']
# sort these months according to the calendar
print(f"months       :{months}")

sortedMonths = sorted(months, key=sortMonth)
print(f"sortedMonths :{sortedMonths}")

print(sortMonth("naj"))

# [1, 2, 3, None, 4, 5]