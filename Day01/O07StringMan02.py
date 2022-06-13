
st = "EMP-102, Mike Tyson, 54, Boxing, 25000"
print(f'st :{st}')

# convert the string into a list
emp = st.split(", ")
dept = st.split(", ")[3]

print(f"emp :{emp}")
print(f"dept :{dept}")

print("-" * 40)
print(f"EmpID       :{emp[0]}")
print(f"EmpName     :{emp[1]}")
print(f"EmpAge      :{emp[2]}")
print(f"Department  :{emp[3]}")
print(f"Salary      :{emp[4]}")

print("-" * 40)
print(f"emp :{emp}")
print(type(emp))
emp_str  = ", ".join(emp)
print(f"emp_str :{emp_str}")
print(type(emp_str))

print("-" * 40)
# maketrans, translate

# maketrans
st = "hello world"
print(f"st :{st}")

a = 'helowrd'
b = 'HELOWRD'

# length of a and b should be the same

strTbl = st.maketrans(a, b)
print(f"strTbl :{strTbl}")

res = st.translate(strTbl)
print(f"res :{res}")

print("-" * 40)
st = "hello"
a = "helo"
b = 'abcd'

strTbl = st.maketrans(a, b)
res = st.translate(strTbl)
print(f"res :{res}")
