
cntr = 0
for n in range(50, 151):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            print(n, end=" ")
            cntr += 1
print()
print(f"There are {cntr} prime numbers between 150 and 50")

print("#" * 40)
print("#" * 40)
print()

for i in range(6, 2, -1):
    for k in range(1, 7-i):
        print(" ", end="")
    for j in range(1, i):
        print(j, end=" ")
    print()
for i in range(6, 1, -1):
    for k in range(1, i-1):
        print(" ", end="")
    for j in range(7-i, 0, -1):
        print(j, end=" ")
    print()

print("#" * 40)

i = 0
while True:
    if i > 10:
        break
    print(i, end=" ")
    i += 2



