tup = (1, 2, 78, 342, 32, "green", True)
# tup[0] = 9
print(type(tup), tup)

print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

if 3421 in tup:
    print("yes 342 present in the tuple")

tup2 = tup[1:4]
print(tup2)