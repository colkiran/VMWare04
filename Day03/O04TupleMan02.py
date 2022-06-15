
from collections import namedtuple

nmdTpl = namedtuple("Employee", "name age salary dept")
emp = nmdTpl(name="Micheal", age=32, salary=65000, dept='Finance')
print(f"emp :{emp}")

print(f"Name        :{emp.name}")
print(f"Age         :{emp.age}")
print(f"Salary      :{emp.salary}")
print(f"Department  :{emp.dept}")

# emp.name = "Jordan"
