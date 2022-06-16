
lst  =  [1, 2, 3]
# for i in lst:
#     print(i)
print(f"lst :{lst}")
print("lst :", type(lst))

# print(dir(lst))
iterObj = lst.__iter__()            # iter(lst)
# print(dir(iterObj))
elem01 = iterObj.__next__()
print(f"elem01 :{elem01}")
elem02 = iterObj.__next__()
print(f"elem02 :{elem02}")
elem03 = iterObj.__next__()
print(f"elem03 :{elem03}")

# elem04 = iterObj.__next__()
# print(f"elem04 :{elem04}")


# elem1 = iterObj