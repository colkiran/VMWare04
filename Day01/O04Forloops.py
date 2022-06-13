
for i in range(1, 10):
    print(i, end=" ")
print()

print("hello world")
# print(data, sep="", end="\n")

print("-" * 40)

for i in range(1, 21):
    if i % 2 == 1:
        continue
    else:
        if i >= 15: break
        print(i, end=" ")

print()
print("-" * 40)

for i in range(1, 10):
    print(i)
else:
    print("iteration completed......")