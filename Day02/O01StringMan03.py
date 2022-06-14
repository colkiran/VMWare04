
st = 'hello world'
print(f"st :{st}")

print("-" * 40)
st1 = "the quick brown fox jumps over the lazy dog"
print(f"st1 :{st1}")

# find
pos = st.find("l")
print(f"Index :{pos}")

pos = st.find("l", 4)
print(f"Index :{pos}")

print("-" * 40)
pos1 = st1.find("the")
print(f"Index :{pos1}")

pos1 = st1.find("the", 5)
print(f"Index :{pos1}")

pos1 = st1.find("Dog")
print(f"Index :{pos1}")

print("-" * 40)

# Replace

print(f"st :{st}")
print(f"st1 :{st1}")

print("-" * 40)
res = st.replace("h", "H")
print(f"res :{res}")

res = st.replace("l", "L")
print(f"res :{res}")

res = st.replace("l", "L", 2)
print(f"res :{res}")

print("-" * 40)
res1 = st1.replace("fox", "tiger")
print(f"res1 :{res1}")

res1 = st1.replace("the", "The")
print(f"res1 :{res1}")

res1 = st1.replace("the", "The", 1)
print(f"res1 :{res1}")

print("-" * 40)
st2 = "My ticket id is 5656225667567"
print(f"st2 :{st2}")

res2 = st2.replace("6", "0")
print(f"res2 :{res2}")

print("-" * 40)